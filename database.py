import pandas as pd
from sqlalchemy import create_engine, select, MetaData, Table, Integer, String, inspect, Column, ForeignKey
import os
# from conditions import ledger

# print(os.path.abspath('.'))

# establish connection
engine = create_engine('sqlite:////Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/transactions_ledger.db', echo=False)
connection = engine.raw_connection()
# to check all table names
inspector = inspect(engine)

print(inspector.get_table_names())

def update_ledger():
	ledger.to_sql('transactions_categorized_aggregate', connection, if_exists='append', index=False)

# if __name__ == '__main__':
# 	update_ledger()

transactions_aggregate = pd.read_sql_query('SELECT * FROM transactions_categorized_aggregate', connection)

# transactions_aggregate.to_sql('transactions_categorized_aggregate', connection, if_exists='replace', index=False)
connection.close()

# print(inspector.get_table_names())

# print(transactions_aggregate)
