# streamlit/localization.py

LANGUAGES = {
    "en": {
        "tabs": {
            "tab1": "Work & Infrastructure",
            "tab2": "Leisure & Culture",
            "tab3": "Demographics",
            "tab4": "Housing",
            "tab5": "Security"
        },
        "plots": {
            "main_header": "Detailed Comparison of Alcaldías",
            "other_alcaldias": "Other Alcaldías"
        },
        "plot_titles": {
            "workforce": "Workforce Distribution by Sector",
            "marital_status": "Marital Status Distribution",
            "age_distribution": "Age Distribution",
            "transportation": "Distribution of Transportation Means",
            "schools": "School Level Distribution",
            "religion": "Religious Affiliation",
            "gender_distribution": "Distribution by Gender",
            "sports_centers": "Distribution of Sports Centers",
            "cultural_venues": "Distribution of Cultural & Historical Centers",
            "budget_sale": "Average Sale Price (MXN)",
            "budget_rent": "Average Rent Price (MXN)",
            "household_size": "Average Persons per Household",
            "housing_quality": "Level of Housing in Good Condition",
            "recreational_spaces": "Distribution of Recreational Centers",
            "security_for_women": "Perception of Safety for Women",
            "general_security": "General Perception of Safety",
            "green_spaces": "Distribution of Green Areas",
            "health_centers": "Distribution of Health Centers",
            "restaurants": "Distribution of Restaurants",
        },
        "legend_labels": {
            "schools": { "NO_ESCUELAS_SUPERIORES_PORCENTAJE_MUN": "Higher Education", "NO_ESCUELAS_BASICAS_PORCENTAJE_MUN": "Basic Education" },
            "age_distribution": { "MAS_60_P": "Over 60", "30_A_60_P": "30 to 60", "18_A_30_P": "18 to 30" },
            "marital_status": { "P12YM_SEPA_PORCENTAJE_MUN": "Separated", "P12YM_SOLT_PORCENTAJE_MUN": "Single", "P12YM_CASA_PORCENTAJE_MUN": "Married" },
            "gender_distribution": { "POBMAS_PORCENTAJE_MUN": "Male", "POBFEM_PORCENTAJE_MUN": "Female" },
            "religion": { "PCATOLICA_PORCENTAJE_MUN": "Catholic", "PRO_CRIEVA_PORCENTAJE_MUN": "Christian/Evangelical", "POTRAS_REL_PORCENTAJE_MUN": "Other Religions", "PSIN_RELIG_PORCENTAJE_MUN": "No Religion" },
            "workforce": { "Funcionarios, profesionistas, técnicos y administrativos": "Professionals/Admin", "Trabajadores agropecuarios": "Agricultural", "Trabajadores en la industria": "Industrial", "Comerciantes y trabajadores en servicios diversos": "Commerce & Services" },
            "transportation": { "Lineas de metro_PORCENTAJE_MUN": "Metro Lines", "Lineas de metrobus_PORCENTAJE_MUN": "Metrobus Lines", "Estaciones Ecobici_PORCENTAJE_MUN": "Ecobici Stations", "LineasRTP_PORCENTAJE_MUN": "RTP Lines" }
        },
        "ui": {
            "title": "SETTLY 🏠", "subtitle": "Your personal guide...", "spinner_text": "Analyzing your preferences...", "map_header": "Map of Recommendations", "chart_header": "Recommendation Score", "chart_info": "Apply filters to see your personalized ranking.", "expander_title": "View Raw Geographic Data",
            "genai_header": "✨ Your Personalized Summary",
            "genai_primary": "Top Recommendation",
            "genai_secondary": "Other Good Options",
            "genai_summary": "In a Nutshell",
            "genai_spinner": "🤖 Crafting your personalized summary...",
            "genai_warning": "Could not generate AI summary. Please check your API key.",
            "news_header": "📰 Latest News from Your Recommended Alcaldías",
            "no_news_found": "No recent news found for this alcaldía."
        },
        "sidebar": {
            "header": "Find Your Ideal Alcaldía", "button_text": "🚀 Find My Alcaldía",
            "bio_subheader": "About You (Optional)",
            "bio_placeholder": "Tell us a bit about yourself: your profession, hobbies, lifestyle, what you value in a neighborhood..."
        },
        "filters": {
            "work_situation": "Work Situation", "sports_centers": "Importance of Sports Centers", "education_level": "Education Level", "cultural_venues": "Importance of Cultural Venues", "recreational_areas": "Importance of Recreational Areas", "restaurants": "Importance of Restaurants", "public_transport": "Primary Public Transport", "gender": "Gender", "marital_status": "Marital Status", "religion": "Religious Preference", "filter_by_age": "Filter by Age?", "your_age": "Your Age", "filter_by_household": "Filter by Household Size?", "household_size": "People in Household", "buy_or_rent": "Buy or Rent?", "your_budget": "Your Budget (MXN)", "green_spaces": "Importance of Green Spaces", "health_centers": "Importance of Health Centers"
        },
        "options": {
            "yes": "Yes", "no": "No", "doesnt_matter": "Doesn't Matter", "work_0": "Officials, professionals, technicians and administrators", "work_1": "Agricultural workers", "work_2": "Industry workers", "work_3": "Merchants and workers in various services", "work_4": "Others", "basic_education": "Basic Education", "higher_education": "Higher Education", "judeo_christian": "Judeo-Christian", "other_religions": "Other Religions", "no_religion": "No Religion", "not_married": "Not Married", "married": "Married", "buy": "Buy", "rent": "Rent", "male": "Male", "female": "Female", "metro": "Metro", "metrobus": "Metrobus", "ecobici": "Ecobici", "rtp": "RTP"
        }
    },
    "es": {
        "tabs": {
            "tab1": "Trabajo e Infraestructura", "tab2": "Ocio y Cultura", "tab3": "Demografía", "tab4": "Vivienda", "tab5": "Seguridad"
        },
        "plots": {
            "main_header": "Comparación Detallada de Alcaldías", "other_alcaldias": "Otras Alcaldías"
        },
        "plot_titles": {
            "workforce": "Distribución de la fuerza laboral por sector",
            "marital_status": "Distribución por Estado Civil",
            "age_distribution": "Distribución por edad",
            "transportation": "Distribución de los medios de transporte",
            "schools": "Distribución por nivel escolar",
            "religion": "Afiliación religiosa",
            "gender_distribution": "Distribución por sexo",
            "sports_centers": "Distribución de centros deportivos",
            "cultural_venues": "Distribución de centros culturales e históricos",
            "budget_sale": "Precio Promedio de Venta (MXN)",
            "budget_rent": "Precio Promedio de Renta (MXN)",
            "household_size": "Personas promedio por vivienda",
            "housing_quality": "Nivel de buen estado de vivienda",
            "recreational_spaces": "Distribución de centros recreativos",
            "security_for_women": "Percepción de seguridad para mujeres",
            "general_security": "Percepción de seguridad general",
            "green_spaces": "Distribución por áreas verdes",
            "health_centers": "Distribución de los centros de salud",
            "restaurants": "Distribución de restaurantes",
        },
        "legend_labels": {
            "schools": { "NO_ESCUELAS_SUPERIORES_PORCENTAJE_MUN": "Escuelas Superiores", "NO_ESCUELAS_BASICAS_PORCENTAJE_MUN": "Escuelas Básicas" },
            "age_distribution": { "MAS_60_P": "Más de 60", "30_A_60_P": "30 a 60", "18_A_30_P": "18 a 30" },
            "marital_status": { "P12YM_SEPA_PORCENTAJE_MUN": "Separado/a", "P12YM_SOLT_PORCENTAJE_MUN": "Soltero/a", "P12YM_CASA_PORCENTAJE_MUN": "Casado/a" },
            "gender_distribution": { "POBMAS_PORCENTAJE_MUN": "Masculino", "POBFEM_PORCENTAJE_MUN": "Femenino" },
            "religion": { "PCATOLICA_PORCENTAJE_MUN": "Católica", "PRO_CRIEVA_PORCENTAJE_MUN": "Cristiana/Evangélica", "POTRAS_REL_PORCENTAJE_MUN": "Otras Religiones", "PSIN_RELIG_PORCENTAJE_MUN": "Sin Religión" },
            "workforce": { "Funcionarios, profesionistas, técnicos y administrativos": "Profesionales/Admin.", "Trabajadores agropecuarios": "Agropecuarios", "Trabajadores en la industria": "Industriales", "Comerciantes y trabajadores en servicios diversos": "Comercio y Servicios" },
            "transportation": { "Lineas de metro_PORCENTAJE_MUN": "Líneas de Metro", "Lineas de metrobus_PORCENTAJE_MUN": "Líneas de Metrobús", "Estaciones Ecobici_PORCENTAJE_MUN": "Estaciones Ecobici", "LineasRTP_PORCENTAJE_MUN": "Líneas RTP" }
        },
        "ui": {
            "title": "SETTLY 🏠", "subtitle": "Tu guía personal...", "spinner_text": "Analizando tus preferencias...", "map_header": "Mapa de Recomendaciones", "chart_header": "Puntuación de Recomendación", "chart_info": "Aplica los filtros para ver tu ranking personalizado.", "expander_title": "Ver Datos Geográficos Crudos",
            "genai_header": "✨ Tu Resumen Personalizado",
            "genai_primary": "Recomendación Principal",
            "genai_secondary": "Otras Buenas Opciones",
            "genai_summary": "En Resumen",
            "genai_spinner": "🤖 Creando tu resumen personalizado...",
            "genai_warning": "No se pudo generar el resumen de IA. Por favor, verifica tu clave de API.",
            "news_header": "📰 Últimas Noticias de tus Alcaldías Recomendadas",
            "no_news_found": "No se encontraron noticias recientes para esta alcaldía."
        },
        "sidebar": {
            "header": "Encuentra Tu Alcaldía Ideal", "button_text": "🚀 Encuentra Mi Alcaldía",
            "bio_subheader": "Sobre Ti (Opcional)",
            "bio_placeholder": "Cuéntanos un poco sobre ti: tu profesión, pasatiempos, estilo de vida, qué valoras en una colonia..."
        },
        "filters": {
            "work_situation": "Situación Laboral", "sports_centers": "Importancia de Centros Deportivos", "education_level": "Nivel Educativo", "cultural_venues": "Importancia de Espacios Culturales", "recreational_areas": "Importancia de Áreas Recreativas", "restaurants": "Importancia de Restaurantes", "public_transport": "Transporte Público Principal", "gender": "Género", "marital_status": "Estado Civil", "religion": "Preferencia Religiosa", "filter_by_age": "¿Filtrar por Edad?", "your_age": "Tu Edad", "filter_by_household": "¿Filtrar por Tamaño del Hogar?", "household_size": "Personas en el Hogar", "buy_or_rent": "¿Comprar o Rentar?", "your_budget": "Tu Presupuesto (MXN)", "green_spaces": "Importancia de Espacios Verdes", "health_centers": "Importancia de Centros de Salud"
        },
        "options": {
            "yes": "Sí", "no": "No", "doesnt_matter": "No importa", "work_0": "Funcionarios, profesionistas, técnicos y administrativos", "work_1": "Trabajadores agropecuarios", "work_2": "Trabajadores en la industria", "work_3": "Comerciantes y trabajadores en servicios diversos", "work_4": "Otros", "basic_education": "Educación Básica", "higher_education": "Educación Superior", "judeo_christian": "Judeocristiana", "other_religions": "Otras Religiones", "no_religion": "Sin Religión", "not_married": "No Casado/a", "married": "Casado/a", "buy": "Comprar", "rent": "Rentar", "male": "Masculino", "female": "Femenino", "metro": "Metro", "metrobus": "Metrobús", "ecobici": "Ecobici", "rtp": "RTP"
        }
    }
}

def get_localizer(language="en"):
    def t(key):
        keys = key.split('.')
        try:
            val = LANGUAGES[language]
            for k in keys:
                val = val[k]
            return val
        except (KeyError, TypeError):
            val = LANGUAGES.get("en", {})
            for k in keys:
                if isinstance(val, dict):
                    val = val.get(k, f"[{key}]")
                else:
                    return f"[{key}]"
            return val
    return t