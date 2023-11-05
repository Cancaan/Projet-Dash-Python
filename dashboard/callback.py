from dash.dependencies import Input, Output
import plotly.express as px


def register_callbacks(app,df):
    
    @app.callback(
        Output('bar-chart', 'figure'),
        Input('susdev-dropdown', 'value')
    )
    #fonction qui met à jour l'histogramme du svg en fonction du pays sélectionné
    def update_bar_chart(selected_country):
       
        filtered_df = df[df['country'] == selected_country]
        
        figure = {
            'data': [
                {'x': filtered_df['year'], 
                 'y': filtered_df['sdg_index_score'], 
                 'type': 'bar', #pour obtenir un histogramme
                 'name': 'Index score'},
            ],
            'layout': {
                'title': f'SDG Index score of {selected_country}',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Score'},
            }
        }
        return figure
    
   
    @app.callback(
        Output('facet-graph', 'figure'),
        Input('goal-dropdown', 'value'),
        Input('year-slider', 'value')
    )
    #fonction qui met à jour le facetting en fonction du critère et de l'année sélectionnés
    def update_facet(selected_goal, selected_year) :

        filtered_df = df[(df['year'] == selected_year)]

        figure = px.scatter(
            data_frame=filtered_df,
            x='sdg_index_score',
            y=selected_goal,
            hover_name='country', #pour qu'il y ait le nom du pays d'écrit sur l'étiquette au passage de la souris
            facet_col='Continent', #facetting en fonction du continent
            title=f'Facetting for {selected_goal} in {selected_year}'
            #labels={selected_goal: selected_goal}
        )
        return figure

