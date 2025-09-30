import os
import json
from typing import List, Optional

import google.generativeai as genai
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- 1. Define Structured Input and Output using Pydantic ---

class UserPreferences(BaseModel):
    # Added language field to the user preferences
    language: str = Field('en', description="The desired output language ('en' for English, 'es' for Spanish).")
    work_choice: int = Field(description="User's work situation preference.")
    sport_choice: int = Field(description="Preference for sports centers.")
    school_choice: int = Field(description="User's education level needs.")
    religion_choice: int = Field(description="User's religious affiliation or lack thereof.")
    marriage_choice: int = Field(description="User's marital status.")
    culture_choice: int = Field(description="Preference for cultural venues.")
    budget_choice: int = Field(description="Whether the user wants to buy or rent.")
    budget: float = Field(description="User's housing budget.")
    sex_choice: int = Field(description="User's gender.")
    people_choice: int = Field(description="Whether to filter by household size.")
    number_people: int = Field(description="Number of people in the household.")
    age_choice: int = Field(description="Whether to filter by age.")
    age: int = Field(description="User's age.")
    recreation_choice: int = Field(description="Preference for recreational areas.")
    green_choice: int = Field(description="Preference for green spaces.")
    health_choice: int = Field(description="Preference for health centers.")
    restaurant_choice: int = Field(description="Preference for restaurants.")
    transportation_choice: int = Field(description="Preference for public transportation.")
    bio: Optional[str] = Field(None, description="A brief user biography for more personalized analysis.")

class AlcaldiaRecommendation(BaseModel):
    primary_recommendation: str = Field(description="A detailed paragraph explaining why the top-ranked alcaldía is the best fit for the user.")
    secondary_options: List[str] = Field(description="A list of 1-2 secondary alcaldías that could also be a good fit, with brief explanations.")
    summary: str = Field(description="A concise summary of the recommendation.")


class AlcaldiaRecommender:
    """
    A class to handle interactions with the Gemini model for generating
    personalized alcaldía recommendations.
    """
    def __init__(self, api_key: str, analysis_data: dict):
        if not api_key:
            raise ValueError("Gemini API key is required.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="gemini-2.5-flash")
        self.analysis_data = analysis_data

    def _get_choice_text(self, category: str, value: int, language: str = 'en') -> str:
        """
        UPDATED: Helper to convert numeric choices into human-readable text
        in the specified language.
        """
        mappings = {
            "work": {
                "en": {0: "Professionals/Admin", 1: "Agricultural", 2: "Industrial", 3: "Commerce & Services", 4: "Other", 5: "Doesn't matter"},
                "es": {0: "Funcionarios, profesionistas, técnicos y administrativos", 1: "Trabajadores agropecuarios", 2: "Trabajadores en la industria", 3: "Comerciantes y trabajadores en servicios diversos", 4: "Otros", 5: "No importa"}
            },
            "school": {
                "en": {0: "Doesn't matter", 1: "Basic Education", 2: "Higher Education"},
                "es": {0: "No importa", 1: "Educación Básica", 2: "Educación Superior"}
            },
            "budget": {
                "en": {0: "Doesn't matter", 1: "Buy", 2: "Rent"},
                "es": {0: "No importa", 1: "Comprar", 2: "Rentar"}
            },
            "sex": {
                "en": {0: "Doesn't matter", 1: "Male", 2: "Female"},
                "es": {0: "No importa", 1: "Masculino", 2: "Femenino"}
            },
            "yes_no": {
                "en": {0: "No", 1: "Yes"},
                "es": {0: "No", 1: "Sí"}
            }
        }
        # Fallback to English if the language is not supported
        lang_map = mappings.get(category, {}).get(language, mappings.get(category, {}).get('en', {}))
        
        if category in mappings:
             return lang_map.get(value, "Not specified")
        elif "choice" in category:
             return mappings["yes_no"][language].get(value, "Not specified")
        return str(value)

    def generate_recommendation(
        self,
        user_preferences: UserPreferences,
        ranked_alcaldias: list
    ) -> Optional[AlcaldiaRecommendation]:
        """UPDATED: Now generates recommendations in the language specified in user_preferences."""
        if not ranked_alcaldias:
            print("No ranked alcaldias provided.")
            return None

        language = user_preferences.language
        lang_full_name = "Spanish" if language == 'es' else "English"

        top_alcaldia_name = ranked_alcaldias[0][0]
        
        # Fetch the language-specific description for the prompt
        alcaldia_info = self.analysis_data.get(top_alcaldia_name, {})
        top_alcaldia_analysis = alcaldia_info.get("analysis", "No analysis available.")
        top_alcaldia_description = alcaldia_info.get("description", {}).get(language, "")


        prompt = f"""
        **Role**: You are a friendly and insightful real estate assistant for Mexico City named Settly.

        **Language Instruction**:
        The user has requested the output in **{lang_full_name} ({language})**. 
        All text in the final JSON response, including recommendations, explanations, and summaries, MUST be in {lang_full_name}.

        **User Profile (in {lang_full_name})**:
        - Bio: {user_preferences.bio or "No provided."}
        - Work: {self._get_choice_text('work', user_preferences.work_choice, language)}, Age: {user_preferences.age}, Budget: ${user_preferences.budget:,.2f} ({self._get_choice_text('budget', user_preferences.budget_choice, language)})
        - Lifestyle: Wants cultural venues ({self._get_choice_text('yes_no', user_preferences.culture_choice, language)}), green spaces ({self._get_choice_text('yes_no', user_preferences.green_choice, language)})

        **Analysis Results**:
        The top recommended alcaldía is: {top_alcaldia_name}.
        Other good options include: {ranked_alcaldias[1][0] if len(ranked_alcaldias) > 1 else 'N/A'} and {ranked_alcaldias[2][0] if len(ranked_alcaldias) > 2 else 'N/A'}.

        **Information on Top Alcaldía ({top_alcaldia_name})**:
        - Data Analysis: {top_alcaldia_analysis}
        - Cultural Description ({lang_full_name}): {top_alcaldia_description}
        
        **Task**:
        Analyze the user's profile and the provided data. Generate a warm, personalized recommendation in {lang_full_name}.
        
        **Your output MUST be a single, valid JSON object** in {lang_full_name} that conforms to the following structure:
        {{
          "primary_recommendation": "A detailed paragraph in {lang_full_name} explaining why {top_alcaldia_name} is the best fit.",
          "secondary_options": ["A brief explanation in {lang_full_name} for the second-best alcaldía.", "A brief explanation in {lang_full_name} for the third-best alcaldía."],
          "summary": "A concise, one-sentence summary in {lang_full_name}."
        }}
        """

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    response_mime_type="application/json",
                )
            )
            response_json = json.loads(response.text)
            return AlcaldiaRecommendation(**response_json)

        except Exception as e:
            print(f"An error occurred while calling the Gemini API or parsing the response: {e}")
            return None


def load_json_data(filepath: str) -> dict:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{filepath}' is not a valid JSON file.")
        return {}

# --- 2. Simulate Inputs and Run the Test ---

def main():
    analysis_data = load_json_data("../data/general-analysis.json")
    if not analysis_data:
        return

    # --- SIMULATED INPUTS (NOW INCLUDING LANGUAGE) ---
    simulated_filters = {
        "language": "es",  # <--- SET LANGUAGE HERE ('es' for Spanish, 'en' for English)
        "work_choice": 1, "sport_choice": 1, "school_choice": 2,
        "religion_choice": 3, "marriage_choice": 1, "culture_choice": 1,
        "budget_choice": 2, "budget": 25000, "sex_choice": 2,
        "people_choice": 0, "number_people": 1, "age_choice": 1, "age": 32,
        "recreation_choice": 1, "green_choice": 1, "health_choice": 0,
        "restaurant_choice": 1, "transportation_choice": 1,
        "bio": "Soy una joven profesional que trabaja en tecnología. Me encanta ir a museos los fines de semana, correr en parques y probar nuevos restaurantes. Busco una zona vibrante, segura y bien comunicada para vivir."
    }

    simulated_ranked_alcaldias = [
        ('Cuauhtémoc', 8), ('Benito Juárez', 6),
        ('Miguel Hidalgo', 4), ('Coyoacán', 2)
    ]
    
    print(f"--- Starting GenAI Test (Language: {simulated_filters['language']}) ---")
    
    user_prefs = UserPreferences(**simulated_filters)

    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        recommender = AlcaldiaRecommender(api_key=api_key, analysis_data=analysis_data)
        
        recommendation = recommender.generate_recommendation(
            user_preferences=user_prefs,
            ranked_alcaldias=simulated_ranked_alcaldias
        )

        if recommendation:
            print("\n--- Personalized Recommendation ---")
            print(recommendation.primary_recommendation)
            print("\n--- Secondary Options ---")
            for option in recommendation.secondary_options:
                print(f"- {option}")
            print("\n--- Summary ---")
            print(recommendation.summary)
        else:
            print("\nCould not generate a recommendation.")

    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please make sure you have set the GOOGLE_API_KEY environment variable.")


if __name__ == "__main__":
    main()
