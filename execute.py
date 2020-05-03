# execute.py
import os
import pandas as pd
import datetime
import dateutil.relativedelta
from datetime import timedelta
from get_transaction import get_transactions
from sqlalchemy import create_engine, select, MetaData, Table, Integer, String, inspect, Column, ForeignKey

# establish connection
engine = create_engine('sqlite:////Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/transactions_ledger.db', echo=False)
connection = engine.raw_connection()
# to check all table names
inspector = inspect(engine)

CHASE = os.getenv('CHASE_ACCESS_TOKEN')
BOFA = os.getenv('BOFA_ACCESS_TOKEN')
AMEX = os.getenv('AMEX_ACCESS_TOKEN')
UBER = os.getenv('UBER_ACCESS_TOKEN')



# Get start and end date of previous month

today = datetime.date.today()
first = today.replace(day=1)
end_date = first - datetime.timedelta(days=1)
start = end_date.replace(day=1)
start = start.isoformat()
end = end_date.isoformat()
print(start)
print(end)
three_months = end_date - dateutil.relativedelta.relativedelta(months=3) 
quarter_start = three_months.replace(day=1) + dateutil.relativedelta.relativedelta(months=1)
quarter_start = quarter_start.isoformat()
print(quarter_start)

# Make new directory for related month
def make_dir(dir):
	try:
	    # Create target Directory
	    os.mkdir(dir)
	    print("Directory " , dir ,  " Created ") 
	except FileExistsError:
	    print("Directory " , dir ,  " already exists")


new_dir ='/Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/' + end + '/'

if __name__ == '__main__':
	make_dir(new_dir)
	try:
		get_transactions(CHASE, 'Chase', start, end, new_dir)
	except  KeyError:
		print("No transactions from Chase")

	try:
		get_transactions(BOFA, 'Bank_of_America', start, end, new_dir)
	except KeyError:
		print("No transactions from Bank_of_America")

	try:	
		get_transactions(AMEX, 'American_Express', start, end, new_dir)
	except KeyError:
		print("No transactions from American_Expres")

	try:
		get_transactions(UBER, 'Uber', start, end, new_dir)
	except KeyError:
		print("No transactions from Uber")

	from transactions import Import_CSV, Transactions

	csv_list = Import_CSV(new_dir).read_csv_list()

	transactions = Import_CSV(new_dir).read_csv(csv_list)

	ledger = Transactions(transactions).clean_transactions()

	from conditions import *

# print(ledger)

	def update_ledger():
		ledger.to_sql('transactions_categorized_aggregate', connection, if_exists='append', index=False)

	# update_ledger()


	transactions_aggregate_quarter = pd.read_sql_query(('SELECT * '
													   'FROM transactions_categorized_aggregate '
													   'where transactions_categorized_aggregate.Date between ?  and ?'), connection, params=[quarter_start,end])

	connection.close()

	# print(inspector.get_table_names())

	# print(transactions_aggregate_quarter)

	from data_analysis import Categories, Monthly, Transaction, Income_Expense_Ratio

	expense_group = Categories(ledger).category_ledger()
	
	cat_chart = Categories(expense_group).category_chart()
	monthly_group = Monthly(transactions_aggregate_quarter).monthly_ledger()
	monthly_chart = Monthly(monthly_group).monthly_chart()
	max_expense = Transaction(ledger).highest_expense()
	pie_ratio = Income_Expense_Ratio(ledger).in_out()

	import email_automation_html



