# streamlit/settly_main.py

import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import plotly.express as px
import pandas as pd
from itertools import zip_longest
import plotly.graph_objects as go
import colorsys
from colormap import rgb2hex, hex2rgb
import os
from dotenv import load_dotenv
from gnews import GNews
import base64
from streamlit_theme import st_theme # <-- Importar st_theme

from utils import datasets, get_best_filter_handler, get_all_alcaldias_data_handler
from localization import get_localizer
from genai import AlcaldiaRecommender, UserPreferences, load_json_data

load_dotenv()

@st.cache_data
def get_image_as_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        st.warning(f"Archivo de logo no encontrado en la ruta: {path}")
        return None

# --- FUNCIÓN DE CONFIGURACIÓN DE PÁGINA ACTUALIZADA Y CORREGIDA ---
def setup_page(t):
    """Configura los ajustes de la página, el ícono y el logo dinámico según el tema."""
    icon_path = "../docs/logo_settly_light.svg"
    
    try:
        st.set_page_config(
            page_title="Settly", 
            page_icon=icon_path,
            layout="wide"
        )
    except Exception:
        st.set_page_config(page_title="Settly", page_icon="🏠", layout="wide")

    # Detecta el tema actual usando streamlit_theme
    theme = st_theme()
    is_dark_theme = theme and theme.get('base') == 'dark'

    # Selecciona la ruta del logo basándose en el tema detectado
    logo_path = "../docs/logo_settly_dark.svg" if is_dark_theme else "../docs/logo_settly_light.svg"
    
    logo_b64 = get_image_as_base64(logo_path)

    if logo_b64:
        # Muestra el logo correcto usando st.image o markdown
        logo_html = f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="data:image/svg+xml;base64,{logo_b64}" alt="Settly Logo" width="15%">
            </div>
        """
        st.markdown(logo_html, unsafe_allow_html=True)
    else:
        # Fallback a texto si el logo no se encuentra
        st.title(t("ui.title"))

    st.markdown(t("ui.subtitle"))

# --- El resto del archivo permanece sin cambios ---

@st.cache_data
def load_map_data(url):
    try:
        gdf = gpd.read_file(url)
        return gdf.to_crs(epsg=4326)
    except Exception as e:
        st.error(f"Error loading map data: {e}")
        return None

def render_sidebar(t):
    with st.sidebar:
        language_key = st.selectbox("Language / Idioma", ["en", "es"], format_func=lambda x: "English" if x == "en" else "Español")
        if st.session_state.get('lang') != language_key:
            st.session_state.lang = language_key
            st.rerun()
        st.header(t("sidebar.header"), divider=True)
        work_options = {t(f"options.work_{i}"): i for i in range(5)}; work_options[t("options.doesnt_matter")] = 5
        school_options = {t("options.doesnt_matter"): 0, t("options.basic_education"): 1, t("options.higher_education"): 2}
        religion_options = {t("options.doesnt_matter"): 0, t("options.judeo_christian"): 1, t("options.other_religions"): 2, t("options.no_religion"): 3}
        marriage_options = {t("options.doesnt_matter"): 0, t("options.not_married"): 1, t("options.married"): 2}
        budget_options = {t("options.doesnt_matter"): 0, t("options.buy"): 1, t("options.rent"): 2}
        sex_options = {t("options.doesnt_matter"): 0, t("options.male"): 1, t("options.female"): 2}
        transportation_options = {t("options.doesnt_matter"): 0, t("options.metro"): 1, t("options.metrobus"): 2, t("options.ecobici"): 3, t("options.rtp"): 4}
        yes_no_options = {t("options.no"): 0, t("options.yes"): 1}
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(t("sidebar.lifestyle_subheader"))
            work_choice_str = st.selectbox(t("filters.work_situation"), options=list(work_options.keys()))
            sport_choice_str = st.selectbox(t("filters.sports_centers"), options=list(yes_no_options.keys()))
            school_choice_str = st.selectbox(t("filters.education_level"), options=list(school_options.keys()), index=2)
            culture_choice_str = st.selectbox(t("filters.cultural_venues"), options=list(yes_no_options.keys()), index=1)
            recreation_choice_str = st.selectbox(t("filters.recreational_areas"), options=list(yes_no_options.keys()))
            restaurant_choice_str = st.selectbox(t("filters.restaurants"), options=list(yes_no_options.keys()))
            transportation_choice_str = st.selectbox(t("filters.public_transport"), options=list(transportation_options.keys()))
        with col2:
            st.subheader(t("sidebar.demographics_subheader"))
            sex_choice_str = st.selectbox(t("filters.gender"), options=list(sex_options.keys()), index=1)
            marriage_choice_str = st.selectbox(t("filters.marital_status"), options=list(marriage_options.keys()), index=1)
            religion_choice_str = st.selectbox(t("filters.religion"), options=list(religion_options.keys()), index=1)
            age_choice_str = st.selectbox(t("filters.filter_by_age"), options=list(yes_no_options.keys()), index=1)
            age = st.slider(t("filters.your_age"), 18, 100, 30, disabled=(yes_no_options[age_choice_str] == 0))
            people_choice_str = st.selectbox(t("filters.filter_by_household"), options=list(yes_no_options.keys()), index=1)
            number_people = st.slider(t("filters.household_size"), 1, 10, 1, disabled=(yes_no_options[people_choice_str] == 0))
        st.subheader(t("sidebar.bio_subheader"))
        bio_text = st.text_area(label="Bio", placeholder=t("sidebar.bio_placeholder"), height=150, label_visibility="collapsed")
        st.subheader(t("sidebar.housing_subheader"), divider=True)
        budget_choice_str = st.selectbox(t("filters.buy_or_rent"), options=list(budget_options.keys()), index=1)
        budget = st.number_input(t("filters.your_budget"), min_value=0, max_value=50000000, value=6000000, step=100000, disabled=(budget_options[budget_choice_str] == 0))
        green_choice_str = st.selectbox(t("filters.green_spaces"), options=list(yes_no_options.keys()), index=1)
        health_choice_str = st.selectbox(t("filters.health_centers"), options=list(yes_no_options.keys()))
        apply_button = st.button(t("sidebar.button_text"), use_container_width=True)
        filter_values = { "work_choice": work_options[work_choice_str], "sport_choice": yes_no_options[sport_choice_str], "school_choice": school_options[school_choice_str], "religion_choice": religion_options[religion_choice_str], "marriage_choice": marriage_options[marriage_choice_str], "culture_choice": yes_no_options[culture_choice_str], "budget_choice": budget_options[budget_choice_str], "budget": budget, "sex_choice": sex_options[sex_choice_str], "people_choice": yes_no_options[people_choice_str], "number_people": number_people, "age_choice": yes_no_options[age_choice_str], "age": age, "recreation_choice": yes_no_options[recreation_choice_str], "green_choice": yes_no_options[green_choice_str], "health_choice": yes_no_options[health_choice_str], "restaurant_choice": yes_no_options[restaurant_choice_str], "transportation_choice": transportation_options[transportation_choice_str] }
        return filter_values, bio_text, apply_button

def create_recommendation_map(gdf, color_map):
    m = folium.Map(location=[19.4326, -99.1332], zoom_start=10, tiles="CartoDB positron")
    def outline_style_function(feature):
        name = feature["properties"]["NOMGEO"]
        if name in color_map:
            return {"color": "white", "weight": 5, "fillOpacity": 0, "opacity": 0.8}
        else:
            return {"fillOpacity": 0, "opacity": 0}
    def main_style_function(feature):
        name = feature["properties"]["NOMGEO"]
        if name in color_map:
            return {"fillColor": color_map.get(name), "color": "black", "weight": 2, "fillOpacity": 0.8}
        else:
            return {"fillColor": "#D3D3D3", "color": "white", "weight": 1, "fillOpacity": 0.5}
    folium.GeoJson(gdf, style_function=outline_style_function).add_to(m)
    folium.GeoJson(gdf, style_function=main_style_function, tooltip=folium.GeoJsonTooltip(fields=["NOMGEO"], aliases=["Alcaldía:"])).add_to(m)
    return m

def create_results_chart(ranked_alcaldias, color_map, t):
    df = pd.DataFrame(ranked_alcaldias, columns=['Alcaldía', 'Score'])
    fig = px.bar(df, x='Score', y='Alcaldía', orientation='h', title=t("ui.chart_header"),
                 labels={'Score': t("ui.chart_header"), 'Alcaldía': ''},
                 color='Alcaldía', color_discrete_map=color_map, text_auto=True)
    fig.update_layout(yaxis={'categoryorder':'total ascending'}, showlegend=False, height=500)
    return fig

def desaturate_color(hex_color, amount=0.4, lighten=0.25):
    r, g, b = hex2rgb(hex_color)
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    s *= amount; v += (1.0 - v) * lighten
    r_new, g_new, b_new = [int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v)]
    return rgb2hex(r_new, g_new, b_new)

def create_stacked_bar_chart(plot_data, id_col, value_cols, title, ranked_alcaldias, t, plot_key):
    if not plot_data: return None
    df = pd.DataFrame(plot_data).copy()
    possible_id_cols = ['Alcaldia', 'ALCALDIA', 'NOM_MUN', 'Alcaldías']
    if id_col not in df.columns:
        actual_id_col = next((col for col in possible_id_cols if col in df.columns), None)
        if actual_id_col: df.rename(columns={actual_id_col: id_col}, inplace=True)
        else: return None
    valid_cols = [col for col in value_cols if col in df.columns]
    if not valid_cols: return None
    df_norm = df.set_index(id_col)[valid_cols].apply(lambda x: 100 * x / x.sum(), axis=1).reset_index()
    df_norm['is_ranked'] = df_norm[id_col].isin(ranked_alcaldias)
    df_norm = df_norm.sort_values(by=['is_ranked', id_col], ascending=[False, True])
    fig = go.Figure()
    base_colors = px.colors.qualitative.Plotly
    for i, metric in enumerate(valid_cols):
        color_saturado = base_colors[i % len(base_colors)]
        color_desaturado = desaturate_color(color_saturado)
        colors = [color_saturado if is_ranked else color_desaturado for is_ranked in df_norm['is_ranked']]
        legend_name = t(f"legend_labels.{plot_key}.{metric}")
        fig.add_trace(go.Bar(
            y=df_norm[id_col], x=df_norm[metric],
            name=legend_name, orientation='h', marker_color=colors,
            text=df_norm[metric].apply(lambda x: f'{x:.1f}%'),
            textposition='inside', insidetextanchor='middle'
        ))
    fig.update_layout(barmode='stack', title=title, 
                      yaxis={'categoryorder':'array', 'categoryarray': df_norm[id_col].tolist()},
                      legend_title_text='Categoría', xaxis_title="Porcentaje (%)", yaxis_title="",
                      uniformtext=dict(minsize=8, mode='show'))
    return fig

def create_comparison_plot(plot_data, id_col, value_cols, title, ranked_alcaldias, color_map, t, data_format=None):
    if not plot_data: return None
    df = pd.DataFrame(plot_data)
    possible_id_cols = ['Alcaldia', 'ALCALDIA', 'NOM_MUN', 'Alcaldías', 'Demarcación territorial', 'alcaldia']
    if id_col not in df.columns:
        actual_id_col = next((col for col in possible_id_cols if col in df.columns), None)
        if actual_id_col: df.rename(columns={actual_id_col: id_col}, inplace=True)
        else: return None
    valid_cols = [col for col in value_cols if col in df.columns]
    if not valid_cols: return None
    df['Status'] = df[id_col].apply(lambda x: x if x in ranked_alcaldias else t("plots.other_alcaldias"))
    plot_color_map = {**color_map, t("plots.other_alcaldias"): 'lightgray'}
    df_melted = df.melt(id_vars=[id_col, 'Status'], value_vars=valid_cols, var_name='Metric', value_name='Value')
    fig = px.bar(df_melted, y=id_col, x='Value', color='Status', orientation='h', title=title, color_discrete_map=plot_color_map)
    if data_format == 'percent':
        fig.update_traces(texttemplate='%{x:.1%}', textposition='inside')
        fig.update_xaxes(title_text="Porcentaje (%)")
    else:
        fig.update_traces(texttemplate='%{x:.3s}', textposition='inside')
    fig.update_layout(showlegend=True, yaxis={'categoryorder':'total ascending'}, legend_title_text='Ranking')
    fig.update_yaxes(title='')
    return fig

@st.cache_data(ttl=3600)
def fetch_news_for_alcaldias(alcaldias: tuple, language: str):
    if not alcaldias: return {}
    news_data = {}
    google_news = GNews(language=language, country='MX', max_results=3)
    for alcaldia in alcaldias:
        query = f'"{alcaldia}" Ciudad de México'
        try:
            articles = google_news.get_news(query)
            news_data[alcaldia] = articles if articles else []
        except Exception as e:
            print(f"Error fetching news for {alcaldia}: {e}")
            news_data[alcaldia] = []
    return news_data

def display_news_section(news_data, t):
    st.header(t("ui.news_header"), divider=True)
    if not news_data: return
    for alcaldia, articles in news_data.items():
        st.subheader(alcaldia)
        if articles:
            for article in articles:
                with st.container(border=True):
                    st.markdown(f"**[{article['title']}]({article['url']})**")
                    st.caption(f"Source: {article['publisher']['title']} | Published: {article['published date']}")
                    st.write(article['description'])
        else:
            st.info(t("ui.no_news_found"))

def display_genai_recommendation(recommendation, t):
    st.subheader(t("ui.genai_header"))
    with st.container(border=True):
        st.markdown(f"**{t('ui.genai_primary')}**"); st.write(recommendation.primary_recommendation)
        st.markdown(f"**{t('ui.genai_secondary')}**")
        for option in recommendation.secondary_options: st.markdown(f"- {option}")
        st.markdown(f"**{t('ui.genai_summary')}**"); st.info(recommendation.summary)

def main():
    if 'lang' not in st.session_state: st.session_state.lang = "en"
    t = get_localizer(st.session_state.lang)
    setup_page(t)

    api_key = os.getenv("GOOGLE_API_KEY")
    analysis_data = load_json_data("../data/general-analysis.json")
    recommender = None
    if api_key and analysis_data:
        try:
            recommender = AlcaldiaRecommender(api_key=api_key, analysis_data=analysis_data)
        except ValueError as e:
            st.error(e)
    else:
        st.warning("Google API Key not found or analysis data missing. AI features will be disabled.", icon="⚠️")

    GEOJSON_URL = "https://raw.githubusercontent.com/cvzmg/settly-front/main/public/geoJsonData/limite-de-las-alcaldas.json"
    gdf = load_map_data(GEOJSON_URL)
    
    if gdf is None or datasets is None:
        st.error("Failed to load necessary data.")
        return

    filter_values, bio_text, apply_button = render_sidebar(t)

    if 'results' not in st.session_state: st.session_state.results = []
    if 'genai_recommendation' not in st.session_state: st.session_state.genai_recommendation = None

    if apply_button:
        with st.spinner(t("ui.spinner_text")):
            st.session_state.results = get_best_filter_handler(datasets, filter_values)
        if recommender and st.session_state.results:
            with st.spinner(t("ui.genai_spinner")):
                user_prefs_data = {**filter_values, "bio": bio_text, "language": st.session_state.lang}
                user_prefs = UserPreferences(**user_prefs_data)
                st.session_state.genai_recommendation = recommender.generate_recommendation(
                    user_preferences=user_prefs,
                    ranked_alcaldias=st.session_state.results
                )
        elif st.session_state.results:
            st.session_state.genai_recommendation = None
            if not recommender: st.toast(t("ui.genai_warning"), icon="🤖")

    ranked_alcaldias_list = [item[0] for item in st.session_state.results]
    color_palette = px.colors.qualitative.Plotly
    alcaldia_color_map = {alcaldia: color for alcaldia, color in zip(ranked_alcaldias_list, color_palette)}

    col_map, col_chart = st.columns([0.6, 0.4])
    with col_map:
        st.subheader(t("ui.map_header")); st_folium(create_recommendation_map(gdf, alcaldia_color_map), use_container_width=True)
    with col_chart:
        st.subheader(t("ui.chart_header"))
        if not st.session_state.results: st.info(t("ui.chart_info"))
        else: st.plotly_chart(create_results_chart(st.session_state.results, alcaldia_color_map, t), use_container_width=True)

    if st.session_state.genai_recommendation:
        display_genai_recommendation(st.session_state.genai_recommendation, t)


    if st.session_state.results:
        st.header(t("plots.main_header"), divider=True)
        all_plot_data = get_all_alcaldias_data_handler(datasets)

        PLOT_CONFIGS = [
            {"type": "stacked", "key": "Workforce", "data_key": "Work", "id": "ALCALDIA", "vals": ["Funcionarios, profesionistas, técnicos y administrativos", "Trabajadores agropecuarios", "Trabajadores en la industria", "Comerciantes y trabajadores en servicios diversos"]},
            {"type": "stacked", "key": "Marital Status", "data_key": "Marital Status", "id": "NOM_MUN", "vals": ["P12YM_CASA_PORCENTAJE_MUN", "P12YM_SOLT_PORCENTAJE_MUN", "P12YM_SEPA_PORCENTAJE_MUN"]},
            {"type": "stacked", "key": "Age Distribution", "data_key": "Age Distribution", "id": "NOM_MUN", "vals": ["18_A_30_P", "30_A_60_P", "MAS_60_P"]},
            {"type": "stacked", "key": "Transportation", "data_key": "Transportation", "id": "Alcaldias", "vals": ["Lineas de metro_PORCENTAJE_MUN", "Lineas de metrobus_PORCENTAJE_MUN", "Estaciones Ecobici_PORCENTAJE_MUN", "LineasRTP_PORCENTAJE_MUN"]},
            {"type": "stacked", "key": "Schools", "data_key": "Schools", "id": "ALCALDIA", "vals": ["NO_ESCUELAS_BASICAS_PORCENTAJE_MUN", "NO_ESCUELAS_SUPERIORES_PORCENTAJE_MUN"]},
            {"type": "stacked", "key": "Religion", "data_key": "Religion", "id": "NOM_MUN", "vals": ["PCATOLICA_PORCENTAJE_MUN", "PRO_CRIEVA_PORCENTAJE_MUN", "POTRAS_REL_PORCENTAJE_MUN", "PSIN_RELIG_PORCENTAJE_MUN"]},
            {"type": "stacked", "key": "Gender Distribution", "data_key": "Gender Distribution", "id": "NOM_MUN", "vals": ["POBFEM_PORCENTAJE_MUN", "POBMAS_PORCENTAJE_MUN"]},
            {"type": "simple", "key": "Sports Centers", "data_key": "Sports Centers", "id": "ALCALDIA", "vals": ["HISTORIC_PERCENTAGE"], "format": "percent"},
            {"type": "simple", "key": "Cultural Venues", "data_key": "Cultural Venues", "id": "ALCALDIA", "vals": ["HISTORIC_PERCENTAGE"], "format": "percent"},
            {"type": "simple", "key": "Budget_Sale", "data_key": "Budget", "id": "Alcaldia", "vals": ["venta"]},
            {"type": "simple", "key": "Budget_Rent", "data_key": "Budget", "id": "Alcaldia", "vals": ["Renta"]},
            {"type": "simple", "key": "Household Size", "data_key": "Household Size", "id": "NOM_MUN", "vals": ["PROM_OCUP"]},
            {"type": "simple", "key": "Housing Quality", "data_key": "Housing Quality", "id": "NOM_MUN", "vals": ["BUEN_EDO"], "format": "percent"},
            {"type": "simple", "key": "Recreational Spaces", "data_key": "Recreational Spaces", "id": "ALCALDIA", "vals": ["HISTORIC_PERCENTAGE"], "format": "percent"},
            {"type": "simple", "key": "Security for Women", "data_key": "Security for Women", "id": "NOM_MUN", "vals": ["normalized"]},
            {"type": "simple", "key": "General Security", "data_key": "General Security", "id": "NOM_MUN", "vals": ["normalized"]},
            {"type": "simple", "key": "Green Spaces", "data_key": "Green Spaces", "id": "Alcaldía", "vals": ["Superficie (m²)_PORCENTAJE"], "format": "percent"},
            {"type": "simple", "key": "Health Centers", "data_key": "Health Centers", "id": "Demarcación territorial", "vals": ["NUMERO_CENTROS_PORCENTAJE"], "format": "percent"},
            {"type": "simple", "key": "Restaurants", "data_key": "Restaurants", "id": "alcaldia", "vals": ["tipo"], "format": "percent"},
        ]
        TABS_CONFIG = {
            "tab1": ["Workforce", "Transportation", "Schools", "Health Centers"],
            "tab2": ["Cultural Venues", "Recreational Spaces", "Restaurants", "Sports Centers", "Green Spaces"],
            "tab3": ["Marital Status", "Age Distribution", "Religion", "Gender Distribution"],
            "tab4": ["Budget_Sale", "Budget_Rent", "Household Size", "Housing Quality"],
            "tab5": ["Security for Women", "General Security"]
        }
        tab_titles = [t(f"tabs.{key}") for key in TABS_CONFIG.keys()]
        tabs = st.tabs(tab_titles)
        for i, (tab_key, plot_keys) in enumerate(TABS_CONFIG.items()):
            with tabs[i]:
                plot_configs_for_tab = [c for c in PLOT_CONFIGS if c['key'] in plot_keys]
                for config in plot_configs_for_tab:
                    title_key = config['key'].lower().replace(' ', '_')
                    data = all_plot_data.get(config["data_key"])
                    plot_key_for_labels = config['key'].lower().replace(' ', '_')
                    if config["type"] == "stacked":
                        fig = create_stacked_bar_chart(data, config["id"], config["vals"], t(f"plot_titles.{title_key}"), ranked_alcaldias_list, t, plot_key_for_labels)
                    else:
                        fig = create_comparison_plot(data, config["id"], config["vals"], t(f"plot_titles.{title_key}"), ranked_alcaldias_list, alcaldia_color_map, t, data_format=config.get("format"))
                    if fig: st.plotly_chart(fig, use_container_width=True)
        
        news_data = fetch_news_for_alcaldias(tuple(ranked_alcaldias_list), st.session_state.lang)
        display_news_section(news_data, t)

if __name__ == "__main__":
    main()