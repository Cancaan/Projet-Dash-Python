from data.get_data import get_data
from dashboard.app import app
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

if __name__ == "__main__":
    df = get_data("Sustainable_Development_Data.csv")
    # print(df.to_string())
    app = app(df)

    app.run_server(debug=True)

    #test
    #test2
    #test gitlab

