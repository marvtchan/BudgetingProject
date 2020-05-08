# Budgeting Project

This project is made for everyday users who want an automated tracking of their budget. 

Within the depository there is a Plaid API that pulls transactions from the prior month and adds to a SQLite database.

<<<<<<< HEAD
With that data, pandas is used to clean, categorize, and prepare for analysis. An SVM model is used for categorizing transactions. The model uses previous transaction data with a 90% accuracy rate.
=======
With that data, pandas is used to clean, categorize, and prepare for analysis.
Categorization is used with an SVM model from previous data. This model is catered specifically to my own past transactions showing a 90$ accuracy rate. 


Analysis is done with charts from matplotlib and seaborn.

In order to use this program, create a database prior to running execute.py.

Analyses includes: 

Categorical, Monthly (past 3 months), and Income to Expense Ratio

![category](https://user-images.githubusercontent.com/49408616/80895588-704aef00-8c9b-11ea-8202-7e63a674c798.png)
![monthly](https://user-images.githubusercontent.com/49408616/80895600-8789dc80-8c9b-11ea-8b84-20d7a69ca904.png)
![in_out](https://user-images.githubusercontent.com/49408616/80895613-9cff0680-8c9b-11ea-8b75-bf8bbbe8b612.png)


Categorization is built off of conditions from my own prior history. 

