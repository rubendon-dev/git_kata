import pandas as pd

def load_data():
    df = pd.read_csv('/Users/rubendonkers/Documents/HWR/Git_exercise/git_kata/data/titanic.csv')
    df = df[df['sex'] == 'male']
    return df

def clean_data(df):
    """
    Cleans the Titanic DataFrame by dropping rows with missing values
    and converting all categorical columns to lowercase.
    """
    # Drop rows with missing values
    df = df.dropna()
    
    # Convert all categorical (object) columns to lowercase
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.lower()
        
    return df