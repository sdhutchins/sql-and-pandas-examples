"""Converting a csv file to a database using pandas."""
import pandas as pd
from sqlalchemy import create_engine

def csv_to_sqlite(csv_file_path, db_file_path, table_name):
    """
    Convert a CSV file to a SQLite database.

    Parameters:
    csv_file_path (str): The path to the CSV file.
    db_file_path (str): The path to the SQLite database file.
    table_name (str): The name of the table to store the data in.

    Returns:
    None
    """
    # Create SQLite engine
    engine = create_engine(f'sqlite:///{db_file_path}')

    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Write the DataFrame to the SQLite database
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

    print(f"Data from {csv_file_path} has been successfully written to the {table_name} table in {db_file_path}.")

# Example usage
if __name__ == "__main__":
    csv_file = 'MAFV3.3.csv'
    db_file = 'C:\\Users\\shutchins2\\Desktop\\sqlpandas\\test.sqlite'
    table_name = 'test'

    csv_to_sqlite(csv_file, db_file, table_name)
