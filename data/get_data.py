import pandas as pd

#charger le dataset de base :
data = pd.read_csv('sdg_index_2000-2022.csv')
#dictionnaire avec anciens et nouveaux noms des variables

# Charger le DataFrame contenant les informations sur les continents ('continents2.csv')
continents_data = pd.read_csv('continents2.csv')

#fusion des deux datasets grâce à la liaison entre deux variables communes
data = data.merge(continents_data[['alpha-3', 'region']], 
                  left_on='country_code', 
                  right_on='alpha-3', 
                  how='left')

#supression de la colonne 'alpha-3' car déjà présente dans le dataset de base avec 'country_code'
data = data.drop(columns=['alpha-3'])

#création d'une nouvelle data frame avec la nouvelle colonne sur les continents
data.to_csv('Sustainable_Development_Data.csv', index=False)

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
            'goal_17_score': 'Partnerships',
            'region': 'Continent'
            }
#renommer les colonnes
data = data.rename(columns=new_names)
#suppression des lignes avec des valeurs manquantes
#notamment celles qui n'ont pas eu de continent attribué car pas un pays
data = data.dropna()
#mise à jour de notre data frame avec les nouveaux noms de variables
data.to_csv('Sustainable_Development_Data.csv', index=False)

def get_data(file):
    df = pd.read_csv(file)
    return df