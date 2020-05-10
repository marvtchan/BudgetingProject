# Budgeting Project

This project is made for everyday users who want an automated tracking of their budget. 

Within the depository there is a Plaid API that pulls transactions from the prior month and adds to a SQLite database.

With that data, pandas is used to clean, categorize, and prepare for analysis.
Categorization is used with an SVM model from previous data. This model is catered specifically to my own past transactions showing a 93% accuracy rate. 

![image](https://user-images.githubusercontent.com/49408616/81507686-e068fe80-92b3-11ea-8684-7f653c2cd8f2.png)

Below is a confusion matrix showing where the inaccuracies stem from. The model mostly shows that it has difficulty with differentiating Food with Bills, Groceries, Entertainment, and Shopping.

![confusion](https://user-images.githubusercontent.com/49408616/81508027-4d7d9380-92b6-11ea-8fe6-ae6137a3d3f2.png)


Analysis is done with charts from matplotlib and seaborn.

In order to use this program, create a database prior to running execute.py.

Analyses includes: 

Categorical, Monthly (past 3 months), and Income to Expense Ratio

![category](https://user-images.githubusercontent.com/49408616/80895588-704aef00-8c9b-11ea-8202-7e63a674c798.png)
![monthly](https://user-images.githubusercontent.com/49408616/80895600-8789dc80-8c9b-11ea-8b84-20d7a69ca904.png)
![in_out](https://user-images.githubusercontent.com/49408616/80895613-9cff0680-8c9b-11ea-8b75-bf8bbbe8b612.png)


Categorization is built off of conditions from my own prior history. 

