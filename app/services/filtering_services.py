import pandas as pd
from collections import Counter

def get_best_work(df,choice):
    if choice==0:
        return None
    else:
        data=df.iloc[1:,choice]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia

def get_best_sport(df,choice):
    if choice==1:
        data=df.iloc[:,1]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==0:
        return None

def get_best_school(df,choice):
    if choice==1:
        data=df.iloc[1:,3]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==2:
        data=df.iloc[1:,4]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==0:
        return None

def get_best_religion(df,choice):
    if choice==1:
        data=df.copy()
        data["JUDEOCRISTIANO_PORCENTAJE"]=data.iloc[:,5:7].sum(axis=1)
        max_row = data.loc[data["JUDEOCRISTIANO_PORCENTAJE"].idxmax()]
        max_alcaldia=max_row[data.columns[0]]
        return max_alcaldia
    elif choice==2:
        data=df.iloc[1:,7]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==3:
        data=df.iloc[1:,8]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==0:
        return None

def get_best_marriage(df,choice):
    if choice==1:
        data=df.copy()
        data["NO_CASADO_PORCENTAJE"]=data.iloc[1:,5:].sum(axis=1)
        max_row = data.loc[data["NO_CASADO_PORCENTAJE"].idxmax()]
        max_alcaldia=max_row[data.columns[0]]
        return max_alcaldia
    elif choice==2:
        data=df.iloc[1:,4]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==0:
        return None

def get_best_culture(df,choice):
    if choice==1:
        data=df.iloc[:,1]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==0:
        return None

def get_best_recreation(df,choice):
    if choice==1:
        data=df.iloc[:,1]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia
    elif choice==0:
        return None

def get_best_budget(df,choice,budget):
    if choice==1:
        closest_row = df.loc[(df.iloc[:,1] - budget).abs().idxmin()]
        min_alcaldia=closest_row[df.columns[0]]
        return min_alcaldia
    elif choice==2:
        closest_row = df.loc[(df.iloc[:,2] - budget).abs().idxmin()]
        min_alcaldia=closest_row[df.columns[0]]
        return min_alcaldia
    elif choice==0:
        return None

def get_best_sex(df,choice,dw,dm):
    if choice==0:
        security=dm.iloc[:,1]
        max_row_security = dm.loc[security.idxmax()]
        max_alcaldia_security=max_row_security[dm.columns[0]]
        return max_alcaldia_security
    elif choice==2:
        data=df.iloc[1:,18]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        security=dw.iloc[:,1]
        max_row_security = dw.loc[security.idxmax()]
        max_alcaldia_security=max_row_security[dw.columns[0]]
        return max_alcaldia,max_alcaldia_security
    elif choice==1:
        data=df.iloc[1:,17]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        security=dm.iloc[:,1]
        max_row_security = dm.loc[security.idxmax()]
        max_alcaldia_security=max_row_security[dm.columns[0]]
        return max_alcaldia,max_alcaldia_security

def get_best_number_people(df, choice, number_people):
    if choice==1:
        closest_row = df.loc[(df.iloc[1:,1] - number_people).abs().idxmin()]
        min_alcaldia=closest_row[df.columns[0]]
        return min_alcaldia
    elif choice==0:
        return None

def get_best_age(df,age_choice,age):
    if age_choice==0:
        return None
    elif age_choice==1:
        if age<18:
            return None
        if 18<=age<30:
            data=df.iloc[1:,:].copy()
            data["18_A_30"]=(data[["P_18A24","P_25A29"]].sum(axis=1))/data["POBTOT"]
            max_row = data.loc[data["18_A_30"].idxmax()]
            max_alcaldia=max_row[data.columns[0]]
            return max_alcaldia
        if 30<=age<60:
            data=df.iloc[1:,:].copy()
            data["30_A_60"]=(data["P_18YMAS"]-data[["P_18A24","P_25A29"]].sum(axis=1)-data["P_60YMAS"])/data["POBTOT"]
            max_row = data.loc[data["30_A_60"].idxmax()]
            max_alcaldia=max_row[data.columns[0]]
            return max_alcaldia
        if 60<=age:
            data=df.iloc[1:,:].copy()
            data["MAS_60"]=data["P_60YMAS"]/data["POBTOT"]
            max_row = data.loc[data["MAS_60"].idxmax()]
            max_alcaldia=max_row[data.columns[0]]
            return max_alcaldia
    
def get_best_green_space(df,choice):
        if choice==1:
            data=df.iloc[1:,5]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        elif choice==0:
            return None
    
def get_best_health(df,choice):
        if choice==1:
            data=df.iloc[1:,2]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        elif choice==0:
            return None
    
def get_best_house(df):
        data=df.iloc[1:,26]
        max_row = df.loc[data.idxmax()]
        max_alcaldia=max_row[df.columns[0]]
        return max_alcaldia

def get_best_restaurant(df,choice):
        if choice==1:
            data=df.iloc[:,1]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        elif choice==0:
            return None

def get_best_transportation(df,choice):
        if choice==1:
            data=df.iloc[1:,5]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        if choice==2:
            data=df.iloc[1:,6]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        if choice==3:
            data=df.iloc[1:,7]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        if choice==4:
            data=df.iloc[1:,8]
            max_row = df.loc[data.idxmax()]
            max_alcaldia=max_row[df.columns[0]]
            return max_alcaldia
        elif choice==0:
            return None

def get_best_filter(data_work,data_sport,data_school,data_religion,data_marriage,data_culture,data_budget,data_people,data_housing,\
                    data_recreation,data_security_women,data_security_everyone,data_green,data_health,data_restaurant,data_transportation,\
                    work_choice,sport_choice,school_choice,religion_choice,marriage_choice,culture_choice,budget_choice,budget,sex_choice,\
                    people_choice,number_people,age_choice,age,recreation_choice, green_choice,health_choice,restaurant_choice,transportation_choice):
    vector=[]
    vector.append(get_best_work(data_work,work_choice))
    vector.append(get_best_sport(data_sport,sport_choice))
    vector.append(get_best_school(data_school,school_choice))
    vector.append(get_best_religion(data_religion,religion_choice))
    vector.append(get_best_marriage(data_marriage,marriage_choice))
    vector.append(get_best_culture(data_culture,culture_choice))
    vector.append(get_best_budget(data_budget,budget_choice,budget))
    res_1, res_2 = get_best_sex(data_people,sex_choice, data_security_women,data_security_everyone)
    vector.append(res_1)
    vector.append(res_2)
    vector.append(get_best_number_people(data_housing,people_choice,number_people))
    vector.append(get_best_age(data_people,age_choice,age))
    vector.append(get_best_recreation(data_recreation,recreation_choice))
    vector.append(get_best_green_space(data_green,green_choice))
    vector.append(get_best_health(data_health,health_choice))
    vector.append(get_best_house(data_housing))
    vector.append(get_best_restaurant(data_restaurant,restaurant_choice))
    vector.append(get_best_transportation(data_transportation,transportation_choice))

    vector=list(filter(None,vector))
    counts=Counter(vector).most_common()

    return counts

def get_alcaldia_info(data_work,data_sport,data_school,data_religion,data_marriage,data_culture,data_budget,data_people,data_housing,\
                      data_recreation,data_security_women,data_security_everyone,data_green,data_health,data_restaurant,data_transportation,alcaldia):
    plot_info={}

    work_result=data_work.iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 1":work_result})

    sport_result=data_sport.to_dict(orient="records")
    plot_info.update({"Bar Chart - 1":sport_result})

    school_result=data_school[["ALCALDIA","NO_ESCUELAS_BASICAS_PORCENTAJE_MUN","NO_ESCUELAS_SUPERIORES_PORCENTAJE_MUN"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 2":school_result})

    religion_result=data_religion[["NOM_MUN","PCATOLICA_PORCENTAJE_MUN","PRO_CRIEVA_PORCENTAJE_MUN","POTRAS_REL_PORCENTAJE_MUN","PSIN_RELIG_PORCENTAJE_MUN"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 3":religion_result})

    marriage_result=data_marriage[["NOM_MUN","P12YM_CASA_PORCENTAJE_MUN","P12YM_SOLT_PORCENTAJE_MUN","P12YM_SEPA_PORCENTAJE_MUN"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 4":marriage_result})

    culture_result=data_culture.to_dict(orient="records")
    plot_info.update({"Bar Chart - 2":culture_result})

    budget_result=data_budget[["Alcaldia","venta","Renta"]].to_dict(orient="records")
    plot_info.update({"Line Chart - Multiple -1":budget_result})

    sex_result=data_people[["NOM_MUN","POBFEM_PORCENTAJE_MUN","POBMAS_PORCENTAJE_MUN"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 5":sex_result})

    data_people["18_A_30_P"]=(data_people[["P_18A24","P_25A29"]].sum(axis=1))/data_people["POBTOT"]
    data_people["30_A_60_P"]=(data_people["P_18YMAS"]-data_people[["P_18A24","P_25A29"]].sum(axis=1)-data_people["P_60YMAS"])/data_people["POBTOT"]
    data_people["MAS_60_P"]=data_people["P_60YMAS"]/data_people["POBTOT"]
    ages_result=data_people[["NOM_MUN","18_A_30_P","30_A_60_P","MAS_60_P"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 6":ages_result})

    number_people_result=data_housing[["NOM_MUN","PROM_OCUP"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - 3":number_people_result})

    quality_result=data_housing[["NOM_MUN","BUEN_EDO"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - 4":quality_result})

    recreation_result=data_recreation.to_dict(orient="records")
    plot_info.update({"Bar Chart - 5":recreation_result})

    security_women_result=data_security_women.to_dict(orient="records")
    plot_info.update({"Bar Chart - 6":security_women_result})

    security_result=data_security_everyone.to_dict(orient="records")
    plot_info.update({"Bar Chart - 7":security_result})

    green_result=data_green[["Alcaldía","Superficie (m²)_PORCENTAJE"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - 8":green_result})

    health_result=data_health[["Demarcación territorial","NUMERO_CENTROS_PORCENTAJE"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - 9":health_result})

    restaurant_result=data_restaurant.to_dict(orient="records")
    plot_info.update({"Bar Chart - 10":restaurant_result})

    transportation_result=data_transportation[["Alcaldias","Lineas de metro_PORCENTAJE_MUN","Lineas de metrobus_PORCENTAJE_MUN","Estaciones Ecobici_PORCENTAJE_MUN","LineasRTP_PORCENTAJE_MUN"]].iloc[1:,:].to_dict(orient="records")
    plot_info.update({"Bar Chart - Multiple - 7":transportation_result})

    plot_info.update({"ALCALDIA":alcaldia})

    return plot_info

    

if __name__ == "__main__":
    data_work= pd.read_csv("../../../data/output/work.csv")
    data_sport=pd.read_csv("../../../data/output/sport_centers.csv")
    data_school=pd.read_csv("../../../data/output/schools.csv")
    data_religion=pd.read_csv("../../../data/output/religion.csv")
    data_marriage=pd.read_csv("../../../data/output/married.csv")
    data_culture=pd.read_csv("../../../data/output/cultural.csv")
    data_budget=pd.read_csv("../../../data/output/budget.csv")
    data_people=pd.read_csv("../../../data/output/ages.csv")
    data_housing=pd.read_csv("../../../data/output/housing_state.csv")
    data_recreation=pd.read_csv("../../../data/output/recreational.csv")
    data_security_women=pd.read_csv("../../../data/output/security_for_women.csv")
    data_security_everyone=pd.read_csv("../../../data/output/security_everyone.csv")
    data_green=pd.read_csv("../../../data/output/green_spaces.csv")
    data_health=pd.read_csv("../../../data/output/health_centers.csv")
    data_restaurant=pd.read_csv("../../../data/output/restaurant.csv")
    data_transportation=pd.read_csv("../../../data/output/transportation.csv")




    filter=get_best_filter(data_work,data_sport,data_school,data_religion,data_marriage,data_culture,data_budget,data_people,data_housing,\
                           data_recreation,data_security_women,data_security_everyone,data_green,data_health,data_restaurant,data_transportation,\
                            0,0,2,1,1,1,1,6000000,1,1,1,1,30,0,1,0,0,0)
    print(filter)

    """alcaldia_info=get_alcaldia_info(data_work,data_sport,data_school,data_religion,data_marriage,data_culture,data_budget,data_people,data_housing,\
                      data_recreation,data_security_women,data_security_everyone,data_green,data_health,data_restaurant,data_transportation,"Coyoacán")
    print(alcaldia_info)"""

   