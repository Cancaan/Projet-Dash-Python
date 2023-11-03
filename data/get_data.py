import pandas as pd

def get_data(file):
    df = pd.read_csv(file)
    return df