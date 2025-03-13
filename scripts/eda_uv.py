import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from functions.eda_functions import print_summary_stats,plot_bar_chart,plot_box_plot,plot_histogram,plot_kde_plot,plot_pie_chart


# reading data from the csv files and converting it to data frames
customers = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers_cleaned.csv')
products = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products_cleaned.csv')
transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions_cleaned.csv')


# Summary Statistics of Numerical Variables of Customers data
print("Summary Statistics for Customers:")
print_summary_stats(customers, 'age')
print_summary_stats(customers, 'membership_duration')

# Summary Statistics of Numerical Variables of Products data
print("\nSummary Statistics for Products:")
print_summary_stats(products, 'price')
print_summary_stats(products, 'inventory_level')

# Summary Statistics of Numerical Variables of Transactions data
print("\nSummary Statistics for Transactions:")
print_summary_stats(transactions, 'price')
print_summary_stats(transactions, 'quantity')
print_summary_stats(transactions, 'discount')
print_summary_stats(transactions, 'price_paid')

# Frequency distributions for categorical variables of Customers Table

plot_pie_chart("Gender", customers, 'gender')

print("\n### City Distribution:")
print(customers['city'].value_counts())
customers['city'].value_counts()[0:10].plot(kind='bar')
plt.title('City Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

plot_bar_chart("State", customers, 'state')
plot_pie_chart("Country", customers, 'country')
plot_bar_chart("Customer Segment", customers, 'customer_segment')

# Frequency distributions for categorical variables of Products Table

print("### Category Distribution:")
print(products['category'].value_counts())
products['category'].value_counts()[0:10].plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

print("\n### Subcategory Distribution:")
print(products['subcategory'].value_counts())
products['subcategory'].value_counts()[0:10].plot(kind='bar')
plt.title('Subcategory Distribution')
plt.xlabel('Subcategory')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

print("\n### Product Distribution:")
print(products['product_name'].value_counts())
products['product_name'].value_counts()[0:10].plot(kind='bar')
plt.title('Product Distribution')
plt.xlabel('Product')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Frequency distributions for categorical variables of Transactions Table
print("### Category Distribution:")
print(transactions['category'].value_counts())
transactions['category'].value_counts()[0:10].plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

print("### SubCategory Distribution:")
print(transactions['subcategory'].value_counts())
transactions['subcategory'].value_counts()[0:10].plot(kind='bar')
plt.title('Sub Category Distribution')
plt.xlabel('Sub Category')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

print("### Product Distribution:")
print(transactions['name'].value_counts())
transactions['name'].value_counts()[0:10].plot(kind='bar')
plt.title('Product Distribution')
plt.xlabel('Product Name')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

plot_pie_chart("Coupons Applied", transactions, 'coupon_applied')

# Histograms and box plots to visualize distributions for Customers Table
plot_histogram("Customers Age", customers, 'age', 10)
plot_box_plot("Customers Age", customers, 'age')
plot_kde_plot("Customers Age", customers, 'age')

plot_histogram("Customers Membership Duration", customers, 'membership_duration', 10)
plot_box_plot("Customers Membership Duration", customers, 'membership_duration')
plot_kde_plot("Customers Membership Duration", customers, 'membership_duration')

# Histograms and box plots to visualize distributions for Products Table
plot_histogram("Products Price", products, 'price', 10)
plot_box_plot("Products Price", products, 'price')
plot_kde_plot("Products Price", products, 'price')

plot_histogram("Products Inventory Level", products, 'inventory_level', 10)
plot_box_plot("Products Inventory Level", products, 'inventory_level')
plot_kde_plot("Products Inventory Level", products, 'inventory_level')

# Histograms and box plots to visualize distributions for Transactions Table
plot_histogram("Transactions Price", transactions, 'price', 10)
plot_box_plot("Transactions Price", transactions, 'price')
plot_kde_plot("Transactions Price", transactions, 'price')

plot_histogram("Transactions Quantity", transactions, 'quantity', 5)
plot_box_plot("Transactions Quantity", transactions, 'quantity')
plot_kde_plot("Transactions Quantity", transactions, 'quantity')

plot_histogram("Transactions Discount", transactions, 'discount', 5)
plot_box_plot("Transactions Discount", transactions, 'discount')
plot_kde_plot("Transactions Discount", transactions, 'discount')

plot_histogram("Transactions Price Paid", transactions, 'price_paid', 20)
plot_box_plot("Transactions Price Paid", transactions, 'price_paid')
plot_kde_plot("Transactions Price Paid", transactions, 'price_paid')