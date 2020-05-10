import pandas as pd
from sqlalchemy import create_engine, select, MetaData, Table, Integer, String, inspect, Column, ForeignKey
import os
# from conditions import ledger

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print(os.path.abspath('.'))

# establish connection
engine = create_engine('sqlite:////Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/transactions_ledger.db', echo=False)
connection = engine.raw_connection()
# to check all table names
inspector = inspect(engine)

print(inspector.get_table_names())

def update_ledger(ledger):
	ledger.to_sql('transactions_categorized_aggregate', connection, if_exists='replace', index=False)

transactions_aggregate_train = pd.read_sql_query('SELECT * FROM transactions_categorized_aggregate', connection)

transactions_aggregate = pd.read_sql_query(('SELECT * '
													   'FROM transactions_categorized_aggregate '
													   'where transactions_categorized_aggregate.Date between ?  and ?'), connection, params=['2019-01-01','2020-03-31'])

# transactions_aggregate_train.to_sql('transactions_categorized_train', connection, if_exists='replace', index=False)


connection.close()


