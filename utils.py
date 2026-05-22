import pandas as pd

def load_data():
    # Replace the path below with the actual location of your titanic.csv file
    df = pd.read_csv('/Users/rubendonkers/Documents/HWR/Git_exercise/git_kata/data/titanic.csv')
    return df