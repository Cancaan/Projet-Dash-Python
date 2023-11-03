import dash

from dashboard.layout import layout
from dashboard.callback import register_callbacks


def app(df):
    app = dash.Dash(__name__)

    app.layout = layout(df)
    
    register_callbacks(app,df)

    return app