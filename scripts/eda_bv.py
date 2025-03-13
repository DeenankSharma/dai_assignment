import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# reading data from the csv files and converting it to data frames
customers = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers_cleaned.csv')
products = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products_cleaned.csv')
transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions_cleaned.csv')

from functions.eda_functions import calc_corr_matrix,create_scatter_plot,create_violin_plot, plot_inventory_by_category

# Correlation Matrices of Customers Table

print("Correlation Matrix between Age and Membership Duration of Customers Table")
calc_corr_matrix(customers,'age','membership_duration')

# Correlation Matrices of Products Table

print("Correlation Matrix between Price and Inventory Level of Products Table")
calc_corr_matrix(products,'price','inventory_level')

# Correlation Matrices of Transactions Table

print("Correlation Matrix between Quantity and Discount of Transactions Table")
calc_corr_matrix(transactions,'quantity','discount')

# Scatter Plots of Customers Table

print("Scatter Plot between Age and Membership Duration of Customers Table")
create_scatter_plot(customers,'age','membership_duration')

# Scatter Plots of Products Table

print("Scatter Plot between Price and Inventory Level of Products Table")
create_scatter_plot(products,'price','inventory_level')

# Scatter Plots of Transactions Table

print("Scatter Plot between Quantity and Discount of Transactions Table")
create_scatter_plot(transactions,'quantity','discount')


# Violin Plots of Customers Table

print("Violin Plot between Gender and Membership Duration of Customers Table")
create_violin_plot(customers,'gender','membership_duration')

# Violin Plots of Products Table

print("Violin Plot between Category and Inventory Level of Products Table")
create_violin_plot(products,'category','inventory_level')

# Box Plots of Transactions Table

print("Box Plot between Coupon Applied and Price Columns of Transactions Table")
transactions.boxplot(by='coupon_applied',column='price',grid=False)

print("Box Plot between Coupon Applied and Quantity Columns of Transactions Table")
transactions.boxplot(by='coupon_applied',column='quantity',grid=False)


# Stacked Bar Charts for categorical variables of Customers Table

print("Bar Plot to infer the categories with exhausting levels of inventory")
plot_inventory_by_category(products)
