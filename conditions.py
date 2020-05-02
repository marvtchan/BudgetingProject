import pandas as pd
import numpy as np
from transactions import Transactions
from transactions import ledger

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def _read_categories():
    categories = {}
    
    with open('categories.txt') as f:
        for i, line in enumerate(f.readlines()):
            categories[i] = line.strip()
    return categories

categories = _read_categories()
_read_categories()


# conditions for each category

shopping = ('target', 'levi', 'amazon', 'cvs', 'best buy', 'bestbuy','flower', 'urban', 'kohl', 'zumiez', 'adidas', 'uniqlo', 'walgreens', 
			'books', 'amzn', 'tire', 'ikea', 'boosted', 'vans', 'etsy', 'apple', 'nordstrom', 'store', 'homemade', 'kotis', 'aisle 1', 'likes', 'oaklandish', 'ace hardware')

food = ('coffee', 'mediterranean', 'itea', 'b-dama', 'tofu', 'hancook', 'cheesesteak', 'restaurant','boba', 'cafe', 'farley', 'pho',
		'ubereats', 'sushi', 'umami', 'bassam', 'pot', 'sukiyaki', 'tea', 'kitchen', 'poke', 'dumpling', 't4', 'meats', 'e&o', 'lunch', 'seven eleven', 
        'pizza', 'starbucks', 'reno market', 'xiao long', 'ohgane', 'postmates', 'food', 'oma', 'golden pineapple', 'chopbar', 'noodle', 'meat', 'grubhub', 'fentons', 
        'salute', 'kafe', 'wings', 'bun mi', 'burger', 'bagel', 'crepes', 'shake', 'bar', 'sauce', 'yokee', 'baguette', 'sergio', 'cha', 'matcha', 'bbq', 'jrcp', 'nagoya')

groceries = ('costco', 'whole food', 'grocery', 'koreana', 'sprouts', 'nob hill', 'instacart', 'supermarket', 'market', 'berkeley bowl', 'mart', 'trader joe')

income_sources = ('mammoth', 'trinet', 'unity', 'qwil', 'paypal', 'tax')

rent = ('venmo', 'allegro', 'windsor')
rent_amount = (-1000)

gas = ('chevron', 'union', 'fuel', '7 eleven', 'shell', 'arco', '7-eleven', 'exxon', 'neumann ent', 'valero')

transfer = ('american express', 'capital one', 'robinhood', 'barclay', 'simple', 'online payment', 'autopay payment', 'transfer', 
            'balance', 'payment received', 'chase credit', 'payment thank you')

bills = ('lemonade', 'comcast', 'pacific gas', 'pg&e', 'pay fee', 'at&t', 'windsor', 'allegro', 
         'squarespace', 'at&', 'storage', 'todoist', 'gsuite', 'mailbird', 'adobe', 'actblue')

gym_name = ('gym', 'ironworks')

pet = ('pet', 'dog')

cash = ('venmo', 'withdrwl', 'atm', 'deposit', 'check', 'peralta', 'cash back')

entertainment = ('spotify', 'pika', 'netflix', 'hulu', 'mad oak', 'amc', 'photo', 'zoo', 'exploratorium', 'rocket fizz',  
                 'blizzard entertain', 'bobby lee', 'disney', 'folsom', 'punch line', 'yosemite', 'reg jack london', 'museum', 'event', 'vudu', 'rakuten')

rewards = ('rewards', 'cashback', 'cash reward', 'cash back')

travel = ('uber', 'lyft', 'garage', 'airport', 'impark', 'airbnb', 'bart', 'oakland park', 
          'sutter', 'parking', 'prkng' , 'hopper', 'airline', 'garg', 'gara', 'oakland downtown', 'ips meters')

gifts = ['quijote', 'dept', 'flowers']



Transactions(ledger).categorize(income_sources, categories[0])
Transactions(ledger).categorize_expense_amount(rent, categories[1], rent_amount)
Transactions(ledger).categorize(shopping, categories[3])
Transactions(ledger).categorize(gas, categories[4])
Transactions(ledger).categorize(transfer, categories[10])
Transactions(ledger).categorize(travel, categories[5])
Transactions(ledger).categorize(cash, categories[6])
Transactions(ledger).categorize(pet, categories[7])
Transactions(ledger).categorize(gifts, categories[8])
Transactions(ledger).categorize(gym_name, categories[9])
Transactions(ledger).categorize(transfer, categories[10])
Transactions(ledger).categorize(groceries, categories[11])
Transactions(ledger).categorize(bills, categories[12])
Transactions(ledger).categorize(entertainment, categories[14])
Transactions(ledger).categorize(rewards, categories[15])
Transactions(ledger).categorize(food, categories[2])
Transactions(ledger).categorize_source(categories[2], "Chase")
Transactions(ledger).categorize_source(categories[2], "Uber")

# ledger.ix[849, 'Category'] = 'Bills'

# expense or income?

income_categories= ['Income', 'Credit Card Reward']

expense_categories= ['Rent', 'Food', 'Shopping', 'Gas', 'Travel', 'Pet', 'Gifts', 'Gym', 'Groceries', 'Bills', 'Uncategorized', 'Entertainment']




# ledger.to_csv('ledger.csv', index=False)


# print(categories)