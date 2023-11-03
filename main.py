from data.get_data import get_data
from dashboard.app import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

if __name__ == "__main__":
    df = get_data("sdg_index_2000-2022.csv")
    # print(df.to_string())
    app = app(df)

    app.run_server(debug=True)
