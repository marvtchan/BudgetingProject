README.md

Budgeting Project

This project is made for everyday users who want an automated tracking of their budget. 

Within the depository there is a Plaid API that pulls transactions from the prior month and adds to a SQLite database.

With that data, pandas is used to clean, categorize, and prepare for analysis.

Analysis is done with charts from matplotlib and seaborn.

In order to use this program, create a database prior to running execute.py.

Analyses includes: 

Categorical, Monthly (past QTD), and Income to Expense Ratio

![category](https://user-images.githubusercontent.com/49408616/80895588-704aef00-8c9b-11ea-8202-7e63a674c798.png)

Categorization is built off of conditions from my own prior history. 

