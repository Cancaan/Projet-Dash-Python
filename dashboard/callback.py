from dash.dependencies import Input, Output

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
                {'x': filtered_df['year'], 'y': filtered_df['sdg_index_score'], 'type': 'bar', 'name': 'Index score'},
            ],
            'layout': {
                'title': f'SDG Index score of {selected_country}',
                'xaxis': {'title': 'Year'},
                'yaxis': {'title': 'Score'},
            }
        }
        return figure
