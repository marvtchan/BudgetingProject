#get_transaction.py
import pandas as pd
import os

pd.set_option('display.max_columns', None)

from plaid import Client as PlaidClient

CHASE = os.getenv('CHASE_ACCESS_TOKEN')
BOFA = os.getenv('BOFA_ACCESS_TOKEN')
AMEX = os.getenv('AMEX_ACCESS_TOKEN')
UBER = os.getenv('UBER_ACCESS_TOKEN')





def get_transactions(token, csv_output, start, end, new_dir):
	plaid_client = PlaidClient(client_id=os.getenv('PLAID_CLIENT_ID'), secret=os.getenv('DEVELOPMENT'),
	                           public_key=os.getenv('PLAID_PUBLIC_KEY'), environment=os.getenv('PLAID_ENV', 'development'))
	response = plaid_client.Transactions.get(token, start_date=start, end_date=end)
	transactions = response['transactions']
	# the transactions in the response are paginated, so make multiple calls while increasing the offset to
	# retrieve all transactions
	while len(transactions) < response['total_transactions']:
	    response = plaid_client.Transactions.get(token, start_date=start, end_date=end,
	                                       offset=len(transactions))
	    transactions.extend(response['transactions'])

	df = pd.DataFrame(transactions)
	df = df[['date', 'name', 'amount']]
	df = df.rename(columns={'date': 'Date', 'name': 'Description', 'amount':'Amount'})
	df.to_csv(new_dir + csv_output + '.csv')


