import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from conditions import ledger
from database import transactions_aggregate
from transactions import end
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

income_categories= ['Income', 'Credit Card Reward']
expense_categories= ['Rent', 'Food', 'Shopping', 'Gas', 'Travel', 'Pet', 'Gifts', 'Gym', 'Groceries', 'Bills', 'Uncategorized', 'Entertainment']

class Categories:
  def __init__(self, ledger):
    self.ledger = ledger

  def category_ledger(self):
    expense = self.ledger[self.ledger['Category'].isin(expense_categories)]
    expense['Amount'] = expense['Amount'] * -1
    expense = expense.sort_values(by='Amount', ascending=False)
    expense_group = expense.groupby(['Category'], as_index=False)['Amount'].sum()
    expense_group = expense_group.sort_values(by='Amount', ascending=False)
    return expense_group

  def category_chart(self):        
    plt.figure(figsize=(13,7))
    chart = sns.barplot(y = "Category", data=self.ledger, palette="pastel", x='Amount')
    # ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.xticks(rotation=0, horizontalalignment='right', fontweight='light', fontsize='small')
    figure_title = 'Expenses by Category'
    plt.title(figure_title, fontsize=16, fontname='Arial', fontweight='bold', x=.45, y =1.01) 
    plt.xlabel('Amount',fontsize=12, x=.45)
    plt.ylabel('')
    plt.subplots_adjust(top=.85)
    chart.xaxis.grid(True)
    plt.tight_layout(True)
    plt.savefig('/Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/' + end + '/' 'category.png', dpi = 300, bbox_inches='tight')
    return chart
    


# expense_group = Categories(ledger).category_ledger()
# cat_chart = Categories(expense_group).category_chart()



# print(expense_group)


# plt.show(cat_chart)

class Monthly:
  def __init__(self, ledger):
    self.ledger = ledger

  def monthly_ledger(self):
    monthly = self.ledger[self.ledger['Category'].isin(expense_categories)]
    monthly['Amount'] = monthly['Amount'] * -1
    monthly = monthly.groupby(['Month'], as_index=False)['Amount'].sum()
    return monthly

  def monthly_chart(self):
        # sns.set(style="whitegrid")
    plt.figure(figsize=(10,7))
    ax = sns.barplot(y = "Amount", data=self.ledger, palette="GnBu_d", x='Month')
    # ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.xticks(rotation=45, horizontalalignment='right', fontweight='light', fontsize='small')
    plt.suptitle('Expenses by Month', fontsize=14, fontname='Arial', fontweight ='bold')
    plt.ylabel('Amount',fontsize=12)
    plt.xlabel('Month',fontsize=12)
    # ax.legend(ncol=2, loc="lower right", frameon=True)
    # sns.despine(left=True, bottom=True)
    ax2 = ax.twinx()
    ax2.plot(ax.get_xticks(), self.ledger.Amount)
    ax.get_shared_y_axes().join(ax,ax2)
    plt.grid(color='gray', linestyle='--')
    plt.savefig('/Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/' + end + '/' 'monthly.png', dpi = 300)
    return ax, ax2


# monthly_group = Monthly(ledger).monthly_ledger()
# monthly_chart = Monthly(monthly_group).monthly_chart()
#monthly_chart.savefig('monthly.png')

# print(monthly_group)
# plt.show()


class Transaction:
    def __init__(self, ledger):
      self.ledger = ledger

    def highest_expense(self):
        transactions = self.ledger[self.ledger['Category'] != "Rent"]
        transactions = transactions[transactions['Category'].isin(expense_categories)]
        transactions['Amount'] = transactions['Amount'] * -1
        max_expense = transactions[transactions['Amount'] == transactions['Amount'].max()].reset_index(drop=True)
        max_expense = max_expense.groupby(['Date','Description'], as_index=False)['Amount'].sum()
        print(type(max_expense))
        max_expense = max_expense.to_string(index=False, header=None)
        print(type(max_expense))
        print ("Your highest expense from the month was:") 
        print(max_expense)
        return max_expense

max_expense = Transaction(ledger).highest_expense()



class Income_Expense_Ratio:
    def __init__(self,ledger):
      self.ledger = ledger

    def in_out(self):
        transactions = self.ledger
        transactions['In/Out'] = " "
        transactions.loc[(transactions['Category'].isin(income_categories)), 'In/Out'] = 'Income'
        transactions.loc[(transactions['Category'].isin(expense_categories)), 'In/Out'] = 'Expense'
        transactions['In/Out'].replace(' ', np.nan, inplace=True)
        transactions = transactions[transactions['In/Out'].notna()]
        ratio = transactions.groupby(['In/Out'], as_index=False)['Amount'].sum()
        ratio.loc[ratio['In/Out'] == 'Expense' , 'Amount'] *= -1  
        print(ratio)

        fig1, ax1 = plt.subplots()

        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

        #explsion
        explode = (0.05,0.05)

        ax1.pie('Amount', colors = colors, labels = 'In/Out', data = ratio, autopct='%1.1f%%', startangle=90, pctdistance=0.87, explode=explode)

        centre_circle = plt.Circle((0,0),0.80,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        plt.suptitle('Expense to Income Ratio', fontsize=14, fontname='Arial', fontweight='bold', y=.55 )

        ax1.axis('equal')  
        plt.tight_layout()
        plt.savefig('/Users/marvinchan/Documents/PythonProgramming/DatabaseforStatements/BudgetingProject/' + end + '/' 'in_out.png', dpi = 300)

# pie_ratio = Income_Expense_Ratio(ledger).in_out()















