from dash import dcc
from dash import html
import plotly.express as px

def sdg_map(df):
    fig = px.choropleth(df, locations="country_code",
                            color="sdg_index_score",
                            hover_name="country",
                            projection='natural earth',
                            animation_frame="year",
                            title='Sustainable Development Goal Score Per Country',
                            color_continuous_scale=px.colors.sequential.Plasma)

    fig.update_layout(width=1280, height=720, title_x=0.5)
    return fig

#fonction servant à créer le facetting qui compare la faim et la pauvreté
def correlation_poverty_hunger(df):
    #colonnes qui vont nous servir pour l'étude
    selected_columns = ['country', 'year', 'No_Poverty', 'Zero_Hunger', 'Continent']
    #création d'un sous ensemble de données en filtrant les observations
    #ajout d'une condition pour ne pas prendre en compte les données erronées
    data_subset = df[~((df['No_Poverty'] == 0) | 
                       (df['No_Poverty'] == 100) | 
                       (df['Zero_Hunger'] == 0) | 
                       (df['Zero_Hunger'] == 100))][selected_columns]
    #ajout d'une colonne temporaire pour la comparaison
    #comparaison pour savoir qui est plus élevé entre Zero_Hunger et No_Poverty
    data_subset['Comparison'] = data_subset.apply(lambda row: 'More Poverty than Hunger' 
                                                  if row['Zero_Hunger'] > row['No_Poverty'] 
                                                  else 'More Hunger than Poverty', 
                                                  axis=1)
    fig = px.scatter(data_subset, 
                     x='No_Poverty', y='Zero_Hunger', 
                     text='country',
                     title='Relation Beetween Poverty and Hunger',
                     facet_col='Continent',
                     color='Comparison', #couleur en fonction du résultat de la comparaison
                     animation_frame='year')
    #réduction de la taille des annotations pour + de visibilité
    fig.update_traces(textfont=dict(size=8))
    fig.update_layout(width=1500, height=720, title_x=0.5)
    return fig
    

#définition en amont d'une liste comprenant les colonnes que l'on voudra avoir dans le menu déroulant du 4ème graphique
included_columns = ['sdg_index_score','No_Poverty', 'Zero_Hunger', 'Good_Health&Wellbeing', 'Quality_Education', 
                    'Gender_Equality', 'Clean_Water&Sanitation', 'Affordable&Clean_Energy', 
                    'Decent_Work&Economic_Growth', 'Industry_Innovation&Infrastructure', 
                    'Reduced_Inequalities', 'Sustainable_Cities&Communities', 
                    'Responsible_Consumption&Production', 'Climate_Action', 
                    'Life_Below_Water', 'Life_on_Land', 'Peace_Justice&Strong_Institutions', 
                    'Partnerships']


def layout(df):
    return  html.Div([
        html.H1("Sustainable Development Dashboard"),
        html.Div([
            dcc.Graph(figure=sdg_map(df)),
            html.Hr()
        ]),

        html.Div([
            dcc.Dropdown(
                id='susdev-dropdown',
                options=[
                    {'label': country, 'value': country} for country in df['country'].unique()
                ],
                value=df['country'].iloc[0]
            ),
            dcc.Graph(id='bar-chart')
        ]),


        html.Div([
            dcc.Graph(figure=correlation_poverty_hunger(df)),
            html.Hr()
        ]),


        html.Div([

            dcc.Dropdown(
                id='goal-dropdown',
                #pour dire que dans mon menu déroulant, il y aura les éléments de la liste included_columns
                options=[{'label': column, 'value': column} 
                         for column in included_columns],
                value=included_columns[0]
            ),

            dcc.Slider(
                id = 'year-slider',
                min = df['year'].min(),
                max = df['year'].max(),
                step = 1,  #incrément d'une année
                value = df['year'].min(),  #année par défaut
                marks = {str(year): str(year) 
                         for year in range(df['year'].min(), df['year'].max() + 1)} 
                         #pour que le slider affiche l'année en entier au lieu de 2k...
            ),

            dcc.Graph(id='facet-graph')

        ])

    ])


