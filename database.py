import pandas as pd
from sqlalchemy import create_engine, select, MetaData, Table, Integer, String, inspect, Column, ForeignKey
import os

# print(os.path.abspath('.'))

# establish connection
engine = create_engine('sqlite:////Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/JupyterNotebook/transactions.db', echo=False)
connection = engine.raw_connection()
# to check all table names
inspector = inspect(engine)

SQL_Transactions = pd.read_sql_query('SELECT * FROM transactions_2019_aggregate',connection)

SQL_Transactions

# ledger = pd.read_csv('ledger.csv')

# ledger.to_sql('transactions_2019_categorized', connection, index=False, if_exists='replace')

categorized_transactions = pd.read_sql_query('SELECT * FROM transactions_2019_categorized', connection)



categorized_transactions.to_csv('SQL_Ledger.csv', index=False)

connection.close()


# print(inspector.get_table_names())


