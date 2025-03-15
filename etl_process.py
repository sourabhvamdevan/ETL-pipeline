import pandas as pd
from sqlalchemy import create_engine

def create_database_connection():
    return create_engine('postgresql://username:password@localhost:5432/database_name')

def load_data_to_dataframe():
    return pd.read_sql("SELECT * FROM messages;", create_database_connection())

def perform_etl(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df_filtered = df[df['timestamp'] > '2024-10-02 15:30:00'].copy()
    df_filtered.loc[:, 'new_column'] = 'Transformed Data'
    return df_filtered

if __name__ == "__main__":
    messages_df = load_data_to_dataframe()
    transformed_df = perform_etl(messages_df)
    print(transformed_df[['timestamp', 'id', 'new_column']])
    print(transformed_df.dtypes)
