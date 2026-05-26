import pandas as pd

def load_data():
    # Keep your path as is
    df = pd.read_csv('/Users/rubendonkers/Documents/HWR/Git_exercise/git_kata/data/titanic.csv')
    df = df[df['sex'] == 'male']
    return df

def clean_data(df):
    """
    Cleans the Titanic DataFrame by dropping rows only where 
    critical columns are missing, and converting categorical 
    columns to lowercase.
    """
    # 1. Only drop rows if critical columns are empty. 
    # This keeps rows where age might be missing but pclass exists.
    df = df.dropna(subset=['pclass', 'sex'])
    
    # 2. Make a copy to avoid SettingWithCopy warnings
    df = df.copy()
    
    # 3. Convert all object/string columns to lowercase
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.lower()
        
    return df