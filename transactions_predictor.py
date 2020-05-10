# transactions_predictor.py

import pandas as pd
import numpy as np
from transactions import Transactions
from transactions import ledger
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn import svm
import pickle
pd.set_option('display.max_rows', 1200)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)



with open('categorizer.pkl', 'rb') as f:
    loaded_clf = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)




class Transactions:
	"""Initiate object for each transaction line"""
	def __init__(self, description, category):
	    self.description = description
	    self.category = category

class Predictor:
	"""Return predicted category for each transaction"""
	def __init__(self, ledger):
		self.ledger = ledger

	def categorize_transactions(self):
		"""Return category of each transaction to new column"""
		transaction = [(Transactions(row.Train,row.Category)) for index, row in self.ledger.iterrows() ] 
		transaction_x = [x.description for x in transaction]
		x = vectorizer.transform(transaction_x)
		self.ledger['Category'] = loaded_clf.predict(x)
		return self.ledger['Category']


Predictor(ledger).categorize_transactions()



