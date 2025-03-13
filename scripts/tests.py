# import pandas as pd
# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions.csv')

# print(transactions['discount'].skew())

# def dfed(p):
#   print(f"{p}")
  
# dfed("dsdf")

import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions.data_cleaning_functions_customers import calculate_null_percent

# reading data from the csv files and converting it to data frames
customers = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers.csv')
products = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products.csv')
transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions.csv')


# print(customers.shape)

# print(transactions.shape)

# print(products.shape)

# print(customers.describe())
# print(products.describe())
# print(transactions.describe())

# print(f"Number of duplicate records in Transactions Table are : {transactions['order_id'].duplicated().sum()}")
print(calculate_null_percent(customers,'last_name'))
print(calculate_null_percent(customers,'state'))
print(calculate_null_percent(customers,'membership_duration'))