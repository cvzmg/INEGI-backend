# streamlit/localization.py

# This dictionary holds all the text for each supported language.
# The structure mirrors the app's layout and components.
LANGUAGES = {
    "en": {
        # UI Elements
        "plots": {
            "main_header": "Detailed Comparison of Alcaldías",
            "other_alcaldias": "Other Alcaldías"
        },
        "plot_titles": {
            "workforce": "Workforce Distribution by Sector",
            "sports_centers": "Sports Centers per 10k Inhabitants",
            "schools": "School Availability (%)",
            "religion": "Religious Affiliation (%)",
            "marital_status": "Marital Status Distribution (%)",
            "cultural_venues": "Cultural Venues per 10k Inhabitants",
            "budget": "Average Housing Prices (MXN)",
            "gender_distribution": "Gender Distribution (%)",
            "age_distribution": "Age Distribution (%)",
            "household_size": "Average Household Size",
            "housing_quality": "Housing in Good Condition (%)",
            "recreational_spaces": "Recreational Spaces per 10k Inhabitants",
            "security_for_women": "Perception of Insecurity for Women (Score)",
            "general_security": "General Security (Score)",
            "green_spaces": "Green Space per Capita (m²)",
            "health_centers": "Health Centers per 10k Inhabitants",
            "restaurants": "Restaurants per 10k Inhabitants",
            "transportation": "Public Transportation Mix"
        },
        "ui": {
            "title": "SETTLY 🏠",
            "subtitle": "Your personal guide to finding the perfect neighborhood in Mexico City. Adjust the filters in the sidebar to match your lifestyle and preferences, then click 'Find My Alcaldía' to see your personalized recommendations.",
            "spinner_text": "Analyzing your preferences...",
            "map_header": "Map of Recommendations",
            "chart_header": "Recommendation Score",
            "chart_info": "Apply filters to see your personalized ranking.",
            "expander_title": "View Raw Geographic Data"
        },
        # Sidebar
        "sidebar": {
            "header": "Find Your Ideal Alcaldía",
            "button_text": "🚀 Find My Alcaldía",
            "lifestyle_subheader": "Lifestyle",
            "demographics_subheader": "Demographics",
            "housing_subheader": "Housing & Environment"
        },
        # Filter Labels
        "filters": {
            "work_situation": "Work Situation",
            "sports_centers": "Importance of Sports Centers",
            "education_level": "Education Level",
            "cultural_venues": "Importance of Cultural Venues",
            "recreational_areas": "Importance of Recreational Areas",
            "restaurants": "Importance of Restaurants",
            "public_transport": "Primary Public Transport",
            "gender": "Gender",
            "marital_status": "Marital Status",
            "religion": "Religious Preference",
            "filter_by_age": "Filter by Age?",
            "your_age": "Your Age",
            "filter_by_household": "Filter by Household Size?",
            "household_size": "People in Household",
            "buy_or_rent": "Buy or Rent?",
            "your_budget": "Your Budget (MXN)",
            "green_spaces": "Importance of Green Spaces",
            "health_centers": "Importance of Health Centers"
        },
        # Options for Select Boxes
        "options": {
            "yes": "Yes",
            "no": "No",
            "doesnt_matter": "Doesn't Matter",
            # Work Options
            "work_0": "Officials, professionals, technicians and administrators",
            "work_1": "Agricultural workers",
            "work_2": "Industry workers",
            "work_3": "Merchants and workers in various services",
            "work_4": "Others",
            # Education
            "basic_education": "Basic Education",
            "higher_education": "Higher Education",
            # Religion
            "judeo_christian": "Judeo-Christian",
            "other_religions": "Other Religions",
            "no_religion": "No Religion",
            # Marriage
            "not_married": "Not Married",
            "married": "Married",
            # Budget
            "buy": "Buy",
            "rent": "Rent",
            # Gender
            "male": "Male",
            "female": "Female",
            # Transport
            "metro": "Metro",
            "metrobus": "Metrobus",
            "ecobici": "Ecobici",
            "rtp": "RTP"
        }
    },
    "es": {
        "plots": {
            "main_header": "Comparación Detallada de Alcaldías",
            "other_alcaldias": "Otras Alcaldías"
        },
        "plot_titles": {
            "workforce": "Distribución de la Fuerza Laboral por Sector",
            "sports_centers": "Centros Deportivos por 10k Habitantes",
            "schools": "Disponibilidad de Escuelas (%)",
            "religion": "Afiliación Religiosa (%)",
            "marital_status": "Distribución por Estado Civil (%)",
            "cultural_venues": "Espacios Culturales por 10k Habitantes",
            "budget": "Precios Promedio de Vivienda (MXN)",
            "gender_distribution": "Distribución por Género (%)",
            "age_distribution": "Distribución por Edad (%)",
            "household_size": "Tamaño Promedio del Hogar",
            "housing_quality": "Viviendas en Buen Estado (%)",
            "recreational_spaces": "Espacios Recreativos por 10k Habitantes",
            "security_for_women": "Percepción de Inseguridad para Mujeres (Puntaje)",
            "general_security": "Seguridad General (Puntaje)",
            "green_spaces": "Espacio Verde por Cápita (m²)",
            "health_centers": "Centros de Salud por 10k Habitantes",
            "restaurants": "Restaurantes por 10k Habitantes",
            "transportation": "Composición del Transporte Público"
        },
        # UI Elements
        "ui": {
            "title": "SETTLY 🏠",
            "subtitle": "Tu guía personal para encontrar la alcaldía perfecta en la Ciudad de México. Ajusta los filtros en la barra lateral según tu estilo de vida y preferencias, y luego haz clic en 'Encuentra Mi Alcaldía' para ver tus recomendaciones.",
            "spinner_text": "Analizando tus preferencias...",
            "map_header": "Mapa de Recomendaciones",
            "chart_header": "Puntuación de Recomendación",
            "chart_info": "Aplica los filtros para ver tu ranking personalizado.",
            "expander_title": "Ver Datos Geográficos Crudos"
        },
        # Sidebar
        "sidebar": {
            "header": "Encuentra Tu Alcaldía Ideal",
            "button_text": "🚀 Encuentra Mi Alcaldía",
            "lifestyle_subheader": "Estilo de Vida",
            "demographics_subheader": "Demografía",
            "housing_subheader": "Vivienda y Entorno"
        },
        # Filter Labels
        "filters": {
            "work_situation": "Situación Laboral",
            "sports_centers": "Importancia de Centros Deportivos",
            "education_level": "Nivel Educativo",
            "cultural_venues": "Importancia de Espacios Culturales",
            "recreational_areas": "Importancia de Áreas Recreativas",
            "restaurants": "Importancia de Restaurantes",
            "public_transport": "Transporte Público Principal",
            "gender": "Género",
            "marital_status": "Estado Civil",
            "religion": "Preferencia Religiosa",
            "filter_by_age": "¿Filtrar por Edad?",
            "your_age": "Tu Edad",
            "filter_by_household": "¿Filtrar por Tamaño del Hogar?",
            "household_size": "Personas en el Hogar",
            "buy_or_rent": "¿Comprar o Rentar?",
            "your_budget": "Tu Presupuesto (MXN)",
            "green_spaces": "Importancia de Espacios Verdes",
            "health_centers": "Importancia de Centros de Salud"
        },
        # Options for Select Boxes
        "options": {
            "yes": "Sí",
            "no": "No",
            "doesnt_matter": "No importa",
            # Work Options
            "work_0": "Funcionarios, profesionistas, técnicos y administrativos",
            "work_1": "Trabajadores agropecuarios",
            "work_2": "Trabajadores en la industria",
            "work_3": "Comerciantes y trabajadores en servicios diversos",
            "work_4": "Otros",
            # Education
            "basic_education": "Educación Básica",
            "higher_education": "Educación Superior",
            # Religion
            "judeo_christian": "Judeocristiana",
            "other_religions": "Otras Religiones",
            "no_religion": "Sin Religión",
            # Marriage
            "not_married": "No Casado/a",
            "married": "Casado/a",
            # Budget
            "buy": "Comprar",
            "rent": "Rentar",
            # Gender
            "male": "Masculino",
            "female": "Femenino",
            # Transport
            "metro": "Metro",
            "metrobus": "Metrobús",
            "ecobici": "Ecobici",
            "rtp": "RTP"
        }
    }
}

def get_localizer(language="en"):
    """
    Returns a function that fetches a translated string for a given key.
    Example: t = get_localizer("es")
             t("ui.title") -> returns the Spanish title
    """
    def t(key):
        # Navigate through the dictionary using dot notation, e.g., "ui.title"
        keys = key.split('.')
        try:
            val = LANGUAGES[language]
            for k in keys:
                val = val[k]
            return val
        except KeyError:
            # Fallback to English if a key is not found in the selected language
            val = LANGUAGES["en"]
            for k in keys:
                val = val.get(k, f"[{k}]") # Return [key] if not found in English either
            return val
    return t
