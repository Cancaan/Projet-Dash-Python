import pandas as pd

#charger le dataset de base :
data = pd.read_csv('sdg_index_2000-2022.csv')
#dictionnaire avec anciens et nouveaux noms des variables
new_names = {'goal_1_score': 'No_Poverty',
            'goal_2_score': 'Zero_Hunger',
            'goal_3_score': 'Good_Health&Wellbeing',
            'goal_4_score': 'Quality_Education',
            'goal_5_score': 'Gender_Equality',
            'goal_6_score': 'Clean_Water&Sanitation',
            'goal_7_score': 'Affordable&Clean_Energy',
            'goal_8_score': 'Decent_Work&Economic_Growth',
            'goal_9_score': 'Industry_Innovation&Infrastructure',
            'goal_10_score': 'Reduced_Inequalities',
            'goal_11_score': 'Sustainable_Cities&Communities',
            'goal_12_score': 'Responsible_Consumption&Production',
            'goal_13_score': 'Climate_Action',
            'goal_14_score': 'Life_Below_Water',
            'goal_15_score': 'Life_on_Land',
            'goal_16_score': 'Peace_Justice&Strong_Institutions',
            'goal_17_score': 'Partnerships'
            }
#renommer les colonnes
data = data.rename(columns=new_names)
#création de notre nouveau data frame avec des nouveaux noms de variables
data.to_csv('Sustainable_Development_Data.csv', index=False)

def get_data(file):
    df = pd.read_csv(file)
    return df