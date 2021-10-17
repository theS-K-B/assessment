import pandas as pd
import sqlalchemy as sa

# creating database connection obj
engine = sa.create_engine('mysql+pymysql://root:12345@localhost:3306/demo_db')
df = pd.read_sql_table('customers', engine, index_col='Customer_Id')

# creating country based table
df.loc[df['Country'] == 'IND'].to_sql(
    name='india_table',
    con=engine,
    index=True,
    if_exists='replace'
)