import pandas as pd
import numpy as np

def calculate_statistics_txns(df, col_name):
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
      0 - if skewness is greater than 0.5 
      mean discount - if skewness is less than or equal to 0.5
        
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
        return (np.nan, np.nan)
    
    clean_data = df[col_name].dropna()
    
    skewness = clean_data.skew()
    
    if skewness <= 0.5:
      return clean_data.mean()

    else:
      return 0


def treat_missing_discount(x, transactions_stats):
    """
    Replace missing discount values with the provided transaction statistics.

    Parameters:
    -----------
    x : float
        The discount value to be processed
    transactions_stats : int or float
        The value to replace missing discounts with

    Returns:
    --------
    int or float
        The cleaned discount value (either the original value or the replacement value if it was missing)

    Notes:
    ------
    This function assumes that `transactions_stats` is a single value (e.g., mean, mode) rather than a tuple of statistics.
    """
    if np.isnan(x):
        return int(transactions_stats)
    else:
        return x