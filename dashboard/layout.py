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
            dcc.Graph(id='bar-chart',
                    figure={
                        'data': [{'x': df[df['country'] == "Afghanistan"]
                                  ['year'], 'y': df[df['country'] == "Afghanistan"]
                                  ['sdg_index_score'], 'type': 'bar', 'name': 'Index score'},
                                ],
                        'layout': {
                            'title': f'Index score of Afghanistan',
                            'xaxis': {'title': 'Year'},
                            'yaxis': {'title': 'Score'},}
            })
        ])
    ])


def correlation_poverty_hunger(df):
    selected_columns = ['country', 'year', 'No_Poverty', 'No_Hunger']
    data_subset = df[selected_columns]
    fig = px.scatter(data_subset, x='No_Poverty', y='No_Hunger', 
                     text='country', title='Relation Beetween Poverty and Hunger')
    fig.update_layout(width=1280, height=720, title_x=0.5)
    return fig