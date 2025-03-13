import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions.eda_functions import plot_discount_effects


# reading data from the csv files and converting it to data frames
customers = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers_cleaned.csv')
products = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products_cleaned.csv')
transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions_cleaned.csv')


# pair plot for Customers Table, to infer the effect of gender on various numeric variables
sns.pairplot(customers,vars=['age','membership_duration'],hue ='gender') 
plt.show() 

# pair plot for Transactions Table, to infer the effect of coupons on various numeric variables
sns.pairplot(transactions,vars=['quantity','price_paid','price'],hue ='coupon_applied') 
plt.show() 

# heatmap showing the correlation between the discount the actual price of the product
sns.heatmap(pd.crosstab(transactions['discount'],transactions['quantity'],normalize='columns')*100)
plt.show()

# grouped comparision of discount on quantity and price paid
plot_discount_effects(transactions)