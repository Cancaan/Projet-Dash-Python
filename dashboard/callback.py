from dash.dependencies import Input, Output
#from dashboard.layout import included_columns


def register_callbacks(app,df):
    
    @app.callback(
        Output('bar-chart', 'figure'),
        Input('susdev-dropdown', 'value')
    )
    def update_bar_chart(selected_country):
        """
        Fonction qui permet de mettre à jour l'histogramme de l'index SVG/an grâce au menu déroulant.
        """
        filtered_df = df[df['country'] == selected_country]
        
        figure = {
            'data': [
                {'x': filtered_df['year'], 
                 'y': filtered_df['sdg_index_score'], 
                 'type': 'bar', 
                 'name': 'Index score'},
            ],
            'layout': {
                'title': f'SDG Index score of {selected_country}',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Score'},
            }
        }
        return figure
    
   
"""
    @app.callback(
        Output('scatter-plot', 'figure'),
        Input('goal-dropdown', 'value')
    )

    def update_scatter_plot(selected_goal) :

        filtered_df = df[df[included_columns] == selected_goal]

        figure = {
            'data': [
                {'x': df['year'], 
                 'y': filtered_df['sdg_index_score'], 
                 'mode': 'markers', #mode de tracage par défaut pour créer un nuage de points
                 'name' : 'Goal per Continent'},
            ],
            'layout': {
                'title': f'{selected_goal} per Continent',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Score'},
            }
        }
        return figure

"""