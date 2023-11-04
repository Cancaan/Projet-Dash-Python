from dash.dependencies import Input, Output
#from dashboard.layout import included_columns
import plotly.express as px


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
    
   

    @app.callback(
        Output('facet-graph', 'figure'),
        Input('goal-dropdown', 'value'),
        Input('year-slider', 'value')
    )

    def update_facet(selected_goal, selected_year) :

        filtered_df = df[(df['year'] == selected_year)]

        figure = px.scatter(
            data_frame=filtered_df,
            x='sdg_index_score',
            y=selected_goal,
            hover_data='country',
            facet_col='Continent',
            animation_frame='year',
            title=f'Facetting for {selected_goal} in {selected_year}',
            labels={selected_goal: selected_goal}





        )
        return figure

