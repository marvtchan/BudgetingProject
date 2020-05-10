import pandas as pd
import csv 
import os
from os import listdir
from os.path import isfile, join
import datetime
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Get start and end date of previous month
today = datetime.date.today()
first = today.replace(day=1)
end = first - datetime.timedelta(days=1)
start = end.replace(day=1)
start = start.isoformat()
end = end.isoformat()
print(start)
print(end)


# class for importing CSVs, pass folder_path for every month
class Import_CSV:
  def __init__(self, path):
    self.path = path

# function for turning name of CSVs into a list
  def read_csv_list(self):
    csv_list = [f for f in listdir(self.path) if isfile(join(self.path, f))]
    csv_list = [x for x in csv_list if not x.startswith('.')]
    return csv_list
    print(csv_list)

# reading all csvs and turning into dataframe then setting columns for each csv and creating ledger
  def read_csv(self, csv_list):
    aggregate_df = []
    for file in csv_list:
      with open(self.path + file, 'r', errors='ignore') as fin:
        reader = csv.reader(fin)
        idx = next(idx for idx, row in enumerate(reader) if len(row) > 3)  
        df = pd.read_csv(self.path + file, skiprows=idx, error_bad_lines=False)

        if df.columns.str.contains('Transaction').any():
          df = df.rename(columns={'Transaction Date' : 'Date'})

        df = df[['Date','Description', 'Amount']]
        df['Source'] = os.path.basename(file)
        df['Source'] = df['Source'].str.split('.').str[0]

        aggregate_df.append(df)

    aggregate_df = pd.concat(aggregate_df)
    aggregate_df = aggregate_df.reset_index(drop=True)

    return aggregate_df

# class is for cleaning of transactions and categorizing of transactions
class Transactions:
  def __init__(self, ledger):  
    self.ledger = ledger

# cleaning data in preparation of categorizing
  def clean_transactions(self):
    self.ledger['Amount'] = self.ledger['Amount'].fillna(0).astype(int)
    self.ledger['Description'] = self.ledger['Description'].str.lower()
    self.ledger['Description'] = self.ledger['Description'].str.replace('*',' ')
    self.ledger['Description'] = self.ledger['Description'].replace('[^a-zA-Z ]', '', regex=True)
    self.ledger.loc[self.ledger['Description'].str.contains('windsor'), 'Description'] = 'windsor'
    self.ledger.loc[self.ledger['Description'].str.contains('paypal'), 'Description'] = 'paypal'
    self.ledger['Category'] = self.ledger['Category'] = 'Uncategorized'
    self.ledger['Month'] = pd.to_datetime(self.ledger['Date']).dt.to_period('M')
    self.ledger['Month'] = self.ledger['Month'].astype(str)
    self.ledger['Type'] = ''
    self.ledger['Type'] = ["Checkings" if type == "Bank_of_America" else "Credit Card" for type in self.ledger['Source']]
    if self.ledger['Type'].str.contains('Credit Card').any():
          self.ledger['Amount'] = self.ledger['Amount'] * -1
    self.ledger['Train'] = self.ledger['Description'] + ' ' + self.ledger['Amount'].astype(str)
    return self.ledger

# categorizing expenses that only have condition parameter
  def categorize(self, condition, category):
    self.ledger.loc[(self.ledger['Category'] == 'Uncategorized')
    & (self.ledger['Description'].str.contains('|'.join(condition))), "Category"] = category
    return self.ledger['Category']

# categorizing expenses with amount and condition parameters
  def categorize_expense_amount(self, condition, category, amount):
    if 'Rent' not in self.ledger['Category']: 
      self.ledger.loc[(self.ledger['Description'].str.contains('|'.join(condition)) & (self.ledger['Amount'] < amount ) & 
        (self.ledger['Category'] == 'Uncategorized')), "Category"] = category
      return self.ledger['Category']
    
# categorizing expense based on a specific source 
  def categorize_source(self, category, source):
    	self.ledger.loc[(self.ledger['Category'] == 'Uncategorized') & (self.ledger['Source'] == source), "Category"] = category
    	return self.ledger['Category']


#passing path of file from the month

file_path = "/Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/" + end + "/"

csv_list = Import_CSV(file_path).read_csv_list()

# print(csv_list)

# initiating transations and final ledger

transactions = Import_CSV(file_path).read_csv(csv_list)


ledger = Transactions(transactions).clean_transactions()

# print(ledger)










#print(SQL_Transactions