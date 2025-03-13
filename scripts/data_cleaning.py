# importing dependencies
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from functions.data_cleaning_functions_customers import calculate_null_percent ,calc_duplicates, categorize_customer, correct_age, calculate_statistics, treat_outlying_ages
from functions.data_cleaning_functions_transactions import calculate_statistics_txns, treat_missing_discount, calculate_accurate_price_paid


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
#  - some ages are invalid as they contain negative ages
#  - in city column, there is inconsistency in the entry of New York City (abbrevated as NY)
#  - some values are missing in state column
#  - in country column, there is inconsistency in the entry of United States (abbrevated as USA)
#  - some values are missing in membership_duration column
#  - faulty data in customer_segment as some customers are marked as regular even though their membership data is missing
#  - some age groups may be considered as outliers such below 10 and above 90 (subject to the proportion of the respective age groups)

# Issues with Products Table
#  - Some of the records are duplicated 

# Issues with the Transactions Table
#  - price_paid logic is wrong, therefore, the data is inaccurate (additional discount of 10% is to be applied for coupon applied)
#  - base discount has empty values 
#  - data has duplicate records

###############################################
# Cleaning Customers Data #
###############################################

print(f"Shape of Customers Table : \n {customers.shape}")

# calculating null percentages in the following columns - last_name, state, membership_duration
print(calculate_null_percent(customers,'last_name'))
print(calculate_null_percent(customers,'state'))
print(calculate_null_percent(customers,'membership_duration'))

# checking duplicacies
print(f"Number of duplicated records : {calc_duplicates(customers)}")

# As the null %ages are decent, therefore dropping the recording may lead to loss of data, therefore, opting for filling the missing values
customers = customers.fillna({
    'last_name': 'Unknown',
    'state': 'Unknown',
    'membership_duration': 0 
})

# replacing NY with New York City
customers['city'] = customers['city'].str.replace('NY','New York City')

# replacing USA with United States
customers['country'] = customers['country'].str.replace('US','United States')

# customers with 0 yrs of membership_duration to be marked as new customers, maintaining others
customers['customer_segment'] = customers['membership_duration'].apply(lambda x : categorize_customer(int(x)))

# replacing negative ages with their modulus to make ages valid
customers['age'] = customers['age'].apply(lambda x : correct_age(int(x)))

# finding outlier ages and replacing them with average age 
# ages greater than 1.5 IQR + x(75% quantile) and less than x(25% quantile) - 1.5 IQR will be considered as outliers
customers_age_stats = calculate_statistics(customers,'age')

customers['age'] = customers['age'].apply(lambda x : treat_outlying_ages(x,customers_age_stats))


###############################################
# Cleaning Products Data #
###############################################


# dropping duplicate records
products = products.drop_duplicates()




###############################################
# Cleaning Transactions Data #
###############################################

print(transactions.head())

# dropping duplicate records
transactions = transactions.drop_duplicates()

# treating missing discount values with mean discount value (if skewness is less) or replace with 0 if skewness is large
transactions_stats = calculate_statistics_txns(transactions,'discount')
print(f"The mean discount is {transactions_stats}")

transactions['discount'] = transactions['discount'].apply(lambda x : treat_missing_discount(x,transactions_stats))

# calculating the accurate price and updating the records
transactions['price_paid'] = transactions.apply(lambda record : calculate_accurate_price_paid(record),axis=1)


# saving cleaned data as csv files
customers.to_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/customers_cleaned.csv')
products.to_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/products_cleaned.csv')
transactions.to_csv('C:/Users/TUF/OneDrive - iitr.ac.in/Desktop/dai/DAI_ASSIGNMENT/data/transactions_cleaned.csv')