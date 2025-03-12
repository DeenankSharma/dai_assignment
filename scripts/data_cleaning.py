# importing dependencies
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.data_cleaning_functions import calculate_null_precent,calc_duplicacies, categorize_customer



# reading data from the csv files and converting it to data frames
customers = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers.csv')
products = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products.csv')
transactions = pd.read_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions.csv')


# making copies of the original data before cleaning it 
customers_original = customers.copy()
products_original = products.copy()
transactions_original = transactions.copy()

# Issues with Customers Table 
#  - Some last names are missing 
#  - some age groups may be considered as outliers such below 10 and above 90 (subject to the proportion of the respective age groups)
#  - in city column, there is inconsistency in the entry of New York City (abbrevated as NY)
#  - some values are missing in state column
#  - in country column, there is inconsistency in the entry of United States (abbrevated as USA)
#  - some values are missing in membership_duration column
#  - faulty data in customer_segment as some customers are marked as regular even though their membership data is missing

# Issues with Products Table
#  - Some of the records are duplicated 

# Issues with the Transactions Table
#  - quantity column has invalid data i.e. 0
#  - price_paid logic is wrong, therefore, the data is inaccurate
#  - coupon applied column has empty values

###############################################
# Cleaning Customers Data #
###############################################

print(f"Information about Customers Table : \n {customers.info()}")
print(f"Shape of Customers Table : \n {customers.shape}")

# calculating null percentages in the following columns - last_name, state, membership_duration
print(calculate_null_precent(customers,'last_name'))
print(calculate_null_precent(customers,'state'))
print(calculate_null_precent(customers,'membership_duration'))

# checking duplicacies
print(f"Number of duplicated records : {calc_duplicacies(customers)}")

# As the null %ages are decent, therefore dropping the recording may lead to loss of data, therefore, opting for filling the missing values
customers = customers.fillna({
    'last_name': 'Unknown',
    'state': 'Unknown',
    'membership_duration': 0 # treating them as new_customers
})

# replacing NY with New York City
customers['city'] = customers['city'].str.replace('NY','New York City')

# replacing USA with United States
customers['country'] = customers['country'].str.replace('USA','United States')

# customers with 0 yrs of membership_duration to be marked as new customers, maintaining others
customers['customer_status'] = customers['membership_duration'].apply(lambda x : categorize_customer(int(x)))
