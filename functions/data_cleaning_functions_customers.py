import pandas as pd
import numpy as np

def calculate_null_percent(df, field):
    """
    Calculate the percentage of null values in a DataFrame column.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to analyze
    field : str
        The column name to check for null values
        
    Returns:
    --------
    float
        The percentage of null values in the specified column
        
    Raises:
    -------
    KeyError
        If the specified field does not exist in the DataFrame
    """
    if field not in df.columns:
        raise KeyError(f"Field '{field}' not found in DataFrame")
    
    return (df[field].isnull().sum() / len(df[field])) * 100


def calc_duplicates(df, subset=None):
    """
    Calculate the number of duplicate rows in a DataFrame.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to analyze
    subset : list or None, default None
        List of column names to consider for identifying duplicates.
        If None, all columns are used.
        
    Returns:
    --------
    int
        The number of duplicate rows in the DataFrame
    """
    return df.duplicated(subset=subset).sum()


def categorize_customer(duration):
    """
    Categorize customers based on their duration.
    
    Parameters:
    -----------
    duration : int or float
        Customer duration in years
        
    Returns:
    --------
    str
        Customer category: 'new' (≤1 year), 'regular' (2-5 years), or 'premium' (>5 years)
    """
    try:
        duration = float(duration)
    except (ValueError, TypeError):
        return 'unknown'
        
    if duration <= 1:
        return 'new'
    elif 2 <= duration <= 5:
        return 'regular'
    elif duration > 5:
        return 'premium'
    else:
        return 'unknown'  


def correct_age(age):
    """
    Correct age values by converting negative ages to positive.
    
    Parameters:
    -----------
    age : int or float or str
        The age value to correct
        
    Returns:
    --------
    int
        Corrected positive integer age value
        
    Notes:
    ------
    - Negative ages are converted to positive
    - Non-numeric values return 0
    - Returns integer values only
    """
    try:
        return int(abs(age))
    except (ValueError, TypeError):
        return 0


def calculate_statistics(df, col_name):
    """
    Calculate basic statistical measures for a DataFrame column.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame containing the data
    col_name : str
        The name of the column to analyze
        
    Returns:
    --------
    tuple
        A tuple containing (mean, Q1, Q3, IQR) where:
        - mean: The average value of the column
        - Q1: The 25th percentile value
        - Q3: The 75th percentile value
        - IQR: The interquartile range (Q3-Q1)
        
    Raises:
    -------
    KeyError
        If the specified column does not exist in the DataFrame
    TypeError
        If the column contains non-numeric data
    """
    if col_name not in df.columns:
        raise KeyError(f"Column '{col_name}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[col_name]):
        raise TypeError(f"Column '{col_name}' must contain numeric data")

    if df[col_name].empty:
        return (np.nan, np.nan, np.nan, np.nan)
    
    clean_data = df[col_name].dropna()
    
    mean_age = clean_data.mean()
    q1 = clean_data.quantile(0.25)
    q3 = clean_data.quantile(0.75)
    iqr = q3 - q1
    
    return mean_age, q1, q3, iqr

def treat_outlying_ages(x, customers_age_stats):
    """
    Replace outlier ages with the mean age.

    Parameters:
    -----------
    x : float
        The age to be processed
    customers_age_stats : tuple
        A tuple containing (mean, Q1, Q3, IQR) where:
        - mean: The average age
        - Q1: The 25th percentile age
        - Q3: The 75th percentile age
        - IQR: The interquartile range (Q3-Q1)

    Returns:
    --------
    float
        The cleaned age (either the original age or the mean age if it's an outlier)

    Notes:
    ------
    Ages are considered outliers if they are greater than Q3 + 1.5*IQR or less than Q1 - 1.5*IQR.
    """

    mean, q1, q3, iqr = customers_age_stats
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return mean if x < lower_bound or x > upper_bound else x

