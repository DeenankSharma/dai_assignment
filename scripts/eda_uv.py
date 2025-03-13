import pandas as pd
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# reading data from the csv files and converting it to data frames
customers = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers_cleaned.csv')
products = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products_cleaned.csv')
transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions_cleaned.csv')


# Summary Statistics of Numerical Variables of Customers data

# Display summary statistics for 'age' and 'membership_duration' columns
print("Summary Statistics for Customers:")

print(customers['age'].describe())  # Age distribution
print(customers['age'].skew())

print(customers['membership_duration'].describe())  # Membership duration distribution
print(customers['membership_duration'].skew())

# Summary Statistics of Numerical Variables of Products data

# Display summary statistics for 'price' and 'inventory_level' columns
print("\nSummary Statistics for Products:")

print(products['price'].describe())  # Price distribution
print(products['price'].skew()) 

print(products['inventory_level'].describe())  # Inventory level distribution
print(products['inventory_level'].skew()) 

# Summary Statistics of Numerical Variables of Transactions data

# Display summary statistics for 'price', 'quantity', 'discount', and 'price_paid' columns
print("\nSummary Statistics for Transactions:")

print(transactions['price'].describe())  # Original price distribution
print(transactions['price'].skew()) 

print(transactions['quantity'].describe())  # Quantity distribution
print(transactions['quantity'].skew())

print(transactions['discount'].describe())  # Discount distribution
print(transactions['discount'].skew())

print(transactions['price_paid'].describe())  # Paid price paid distribution
print(transactions['price_paid'].skew())


# Frequency distributions for categorical variables of Customers Table

# Analyze and plot 'gender' distribution
print("### Gender Distribution:")
print(customers['gender'].value_counts())
customers['gender'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.title('Gender Distribution')
plt.show()  

# Analyze and plot 'city' distribution
print("\n### City Distribution:")
print(customers['city'].value_counts())
customers['city'].value_counts()[0:10].plot(kind='bar')
plt.title('City Distribution')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Analyze and plot 'state' distribution
print("\n### State Distribution:")
print(customers['state'].value_counts())
customers['state'].value_counts().plot(kind='bar')
plt.title('State Distribution')
plt.xlabel('State')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout() 
plt.show()

# Analyze and plot 'country' distribution
print("\n### Country Distribution:")
print(customers['country'].value_counts())
customers['country'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.title('Country Distribution')
plt.show() 

# Analyze and plot 'customer_segment' distribution
print("\n### Customer Segment Distribution:")
print(customers['customer_segment'].value_counts())
customers['customer_segment'].value_counts().plot(kind='bar')
plt.title('Customer Segment Distribution')
plt.xlabel('Segment')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout() 
plt.show()

# Frequency distributions for categorical variables of Products Table

# Analyze and plot 'category' distribution
print("### Category Distribution:")
print(products['category'].value_counts())
products['category'].value_counts()[0:10].plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Analyze and plot 'subcategory' distribution
print("\n### Subcategory Distribution:")
print(products['subcategory'].value_counts())
products['subcategory'].value_counts()[0:10].plot(kind='bar')
plt.title('Subcategory Distribution')
plt.xlabel('Subcategory')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Analyze and plot 'product' distribution
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

# Analyze and plot 'category' distribution
print("### Category Distribution:")
print(transactions['category'].value_counts())
transactions['category'].value_counts()[0:10].plot(kind='bar')
plt.title('Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Analyze and plot 'subcategory' distribution
print("### SubCategory Distribution:")
print(transactions['subcategory'].value_counts())
transactions['subcategory'].value_counts()[0:10].plot(kind='bar')
plt.title('Sub Category Distribution')
plt.xlabel('Sub Category')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Analyze and plot 'product_name' distribution
print("### Product Distribution:")
print(transactions['name'].value_counts())
transactions['name'].value_counts()[0:10].plot(kind='bar')
plt.title('Product Distribution')
plt.xlabel('Product Name')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()

# Analyze and plot 'coupon_applied' distribution
print("### Coupons Applied Distribution:")
print(transactions['coupon_applied'].value_counts())
transactions['coupon_applied'].value_counts().plot(kind='pie', autopct='%0.1f%%')
plt.title('Coupon Applied Distribution')
plt.xlabel('Coupon Applied')
plt.ylabel('Count')
plt.xticks(rotation=90)  
plt.tight_layout()  
plt.show()