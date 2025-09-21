import pandas as pd
from filtering_services import get_best_filter, get_alcaldia_info

datasets = {
    "work": pd.read_csv("../data/output/work.csv"),
    "sport_centers": pd.read_csv("../data/output/sport_centers.csv"),
    "schools": pd.read_csv("../data/output/schools.csv"),
    "religion": pd.read_csv("../data/output/religion.csv"),
    "married": pd.read_csv("../data/output/married.csv"),
    "cultural": pd.read_csv("../data/output/cultural.csv"),
    "budget": pd.read_csv("../data/output/budget.csv"),
    "ages": pd.read_csv("../data/output/ages.csv"),
    "housing_state": pd.read_csv("../data/output/housing_state.csv"),
    "recreational": pd.read_csv("../data/output/recreational.csv"),
    "security_for_women": pd.read_csv("../data/output/security_for_women.csv"),
    "security_everyone": pd.read_csv("../data/output/security_everyone.csv"),
    "green_spaces": pd.read_csv("../data/output/green_spaces.csv"),
    "health_centers": pd.read_csv("../data/output/health_centers.csv"),
    "restaurant": pd.read_csv("../data/output/restaurant.csv"),
    "transportation": pd.read_csv("../data/output/transportation.csv"),
}

def get_best_filter_handler(dfs, filter_values):
    return get_best_filter(
        dfs["work"],
        dfs["sport_centers"],
        dfs["schools"],
        dfs["religion"],
        dfs["married"],
        dfs["cultural"],
        dfs["budget"],
        dfs["ages"],
        dfs["housing_state"],
        dfs["recreational"],
        dfs["security_for_women"],
        dfs["security_everyone"],
        dfs["green_spaces"],
        dfs["health_centers"],
        dfs["restaurant"],
        dfs["transportation"],
        filter_values["work_choice"],
        filter_values["sport_choice"],
        filter_values["school_choice"],
        filter_values["religion_choice"],
        filter_values["marriage_choice"],
        filter_values["culture_choice"],
        filter_values["budget_choice"],
        filter_values["budget"],
        filter_values["sex_choice"],
        filter_values["people_choice"],
        filter_values["number_people"],
        filter_values["age_choice"],
        filter_values["age"],
        filter_values["recreation_choice"],
        filter_values["green_choice"],
        filter_values["health_choice"],
        filter_values["restaurant_choice"],
        filter_values["transportation_choice"]
    )

def get_all_alcaldias_data_handler(dfs):
    """
    Calls the get_alcaldia_info service with all datasets to retrieve
    data formatted for plotting.
    """
    if dfs is None:
        return {}
    
    result = get_alcaldia_info(
        dfs["work"], dfs["sport_centers"], dfs["schools"], dfs["religion"],
        dfs["married"], dfs["cultural"], dfs["budget"], dfs["ages"],
        dfs["housing_state"], dfs["recreational"], dfs["security_for_women"],
        dfs["security_everyone"], dfs["green_spaces"], dfs["health_centers"],
        dfs["restaurant"], dfs["transportation"]
    )
    return result