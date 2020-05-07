# train_model.py

import os
import pandas as pd
import datetime as dt
import dateutil.relativedelta
from datetime import timedelta
from sqlalchemy import create_engine, select, MetaData, Table, Integer, String, inspect, Column, ForeignKey
pd.set_option('display.max_rows', 1200)

# establish connection
engine = create_engine('sqlite:////Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/transactions_ledger.db', echo=False)
connection = engine.raw_connection()
# to check all table names
inspector = inspect(engine)

inspector.get_table_names()

start = "2019-01-01" 
end = "2020-04-30"


# Query data all-time
transactions_aggregate_categorized = pd.read_sql_query(('SELECT * '
													   'FROM transactions_categorized_aggregate '
													   'where transactions_categorized_aggregate.Date between ?  and ?'), connection, params=[start,end])

# establish categories
def _read_categories():
    categories = {}
    
    with open('categories.txt') as f:
        for i, line in enumerate(f.readlines()):
            categories[i] = line.strip()
    return categories

categories = _read_categories()


# create objects for transactions
class Transactions:
    def __init__(self, description, category, amount):
        self.description = description
        self.category = category
        self.amount = amount
        
    def get_category(self):
        for i in categories:
            if self.category == categories[i]:
                return categories[i]
            
# create objects for categories         
class Category:
    Income = "Income"
    Rent = "Rent"
    Food = "Food"
    Shopping = "Shopping"
    Gas = "Gas"
    Travel = "Travel"
    Cash = "Cash"
    Pet = "Pet"
    Gifts = "Gifts"
    Gym = "Gym"
    Transfer = "Transfer"
    Groceries = "Groceries"
    Bills = "Bills"
    Uncategorized = "Uncategorized"
    Entertainment = "Entertainment"
    Credit_Card_Reward = "Credit Card Reward"


# pull data for training
transactions = transactions_aggregate_categorized[['Description', 'Category', 'Amount']]
transaction = [(Transactions(row.Description,row.Category,row.Amount)) for index, row in transactions.iterrows() ] 

# import sklearn
from sklearn.model_selection import train_test_split

# split data between training and test
training, test=train_test_split(transaction, test_size=.33, random_state=42)

# create list of strings for training data and test data
train_x = [x.description for x in training]
train_y = [x.category for x in training]

test_x = [x.description for x in test]
test_y = [x.category for x in test]

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# turn string to vectors for training
vectorizer = CountVectorizer()
train_x_vectors = vectorizer.fit_transform(train_x)

test_x_vectors = vectorizer.transform(test_x)

from sklearn import svm

# train with support vector model
clf_svm = svm.SVC(C=16, kernel='linear', gamma='auto')

clf_svm.fit(train_x_vectors, train_y)

test_x[0]
# test_x_vectors[0]

print(clf_svm.predict(test_x_vectors[0]))


# evalute model and accuracy
print(clf_svm.score(test_x_vectors, test_y))

from sklearn.metrics import f1_score

print(f1_score(test_y, clf_svm.predict(test_x_vectors), average=None, labels=[Category.Rent, Category.Income, Category.Food, Category.Shopping, Category.Gas, Category.Travel, Category.Cash, 
                                                                        Category.Pet, Category.Gifts, Category.Gym, Category.Transfer, Category.Groceries, Category.Bills, Category.Uncategorized, Category.Entertainment, 
                                                                       Category.Credit_Card_Reward]))


#Save Model to Pickle

# import pickle

# with open('categorizer.pkl', 'wb') as f:
#     pickle.dump(clf, f)

