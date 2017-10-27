"""Converting a csv file to a database using pandas."""
import pandas as pd
from sqlalchemy import create_engine

# Create a sqlite database from a csv file.

# Unix/Mac - 4 initial slashes in total
# engine = create_engine('sqlite:////absolute/path/to/foo.db')

# Windows engine creation
engine = create_engine('sqlite:///C:\\Users\\shutchins2\\Desktop\\sqlpandas\\test.sqlite')

csvfile = 'MAFV3.3.csv'
df = pd.read_csv(csvfile)
df.to_sql(name='test', con=engine, if_exists='append', index=False)
