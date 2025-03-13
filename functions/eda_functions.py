import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def print_summary_stats(df,col_name):
  print(df[col_name].describe())
  print(df[col_name].skew())
  
def plot_pie_chart(phrase,df,col_name):
  print(f"\n### {phrase} Distribution:")
  print(df[col_name].value_counts())
  df[col_name].value_counts().plot(kind='pie',autopct='%0.1f%%')
  plt.title(f"{phrase} Distribution")
  plt.show()

def plot_bar_chart(phrase,df,col_name):
  print(f"\n### {phrase} Distribution:")
  print(df[col_name].value_counts())
  df[col_name].value_counts().plot(kind='bar')
  plt.title(f"{phrase} Distribution")
  plt.xlabel(phrase)
  plt.ylabel('Count')
  plt.xticks(rotation=90)  
  plt.tight_layout() 
  plt.show()
  
def plot_histogram(phrase,df,col_name,bins_):
  print(f"### {phrase} Distribution:")
  df[col_name].plot(kind='hist',bins = bins_)
  plt.title(f'{phrase} Distribution')
  plt.xlabel(phrase)
  plt.ylabel('Frequency')
  plt.tight_layout()  
  plt.show()
  
  
def plot_box_plot(phrase,df,col_name):
  print(f"### {phrase} Distribution:")
  df[col_name].plot(kind='box')
  plt.title(f'{phrase} Distribution')
  plt.xlabel(phrase) 
  plt.tight_layout()  
  plt.show()

def plot_kde_plot(phrase,df,col_name):
  print(f"### {phrase} Distribution:")
  df[col_name].plot(kind='kde')
  plt.title(f'{phrase} Distribution')
  plt.xlabel(phrase) 
  plt.ylabel('Density') 
  plt.tight_layout()  
  plt.show()
  
def calc_corr_matrix(df, col1, col2):
    '''
    Calculates and prints the correlation matrix between two numerical columns of a dataframe.
    
    Parameters:
    df (pandas.DataFrame): The dataframe containing the data
    col1 (str): Name of the first column
    col2 (str): Name of the second column
    '''
    subset_df = df[[col1, col2]]
    corrM = subset_df.corr()
    
    print(corrM)
    
    
def create_scatter_plot(df, col1, col2):
    '''
    Creates and displays a scatter plot of two numerical columns from a dataframe.
    
    Parameters:
    df (pandas.DataFrame): The dataframe containing the data
    col1 (str): Name of the first column (x-axis)
    col2 (str): Name of the second column (y-axis)
    '''
    
    plt.scatter(df[col1], df[col2], alpha=0.7)
    title = f"Scatter plot of {col2} vs {col1}"
   
    plt.set_xlabel(col1)
    plt.set_ylabel(col2)
    plt.set_title(title)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()


def create_violin_plot(df,col1,col2):
  sns.violinplot(x=col1,y=col2,data=df)
  plt.xlabel(col1)
  plt.ylabel(col2)
  plt.title(f"Violin Plot between {col1} and {col2}")
  plt.show()
  
def plot_inventory_by_category(df, top_n=5):
    '''
    Creates a simple stacked bar chart showing inventory levels by category,
    stacked by subcategory, for the categories with lowest inventory.
    
    Parameters:
    df (pandas.DataFrame): DataFrame with 'category', 'subcategory', and 'inventory_level' columns
    top_n (int): Number of categories with lowest inventory to show
    '''
    inventory_data = df.groupby(['category', 'subcategory'])['inventory_level'].mean().reset_index()
    category_totals = inventory_data.groupby('category')['inventory_level'].mean().reset_index()
    
    low_inventory_cats = category_totals.sort_values('inventory_level').head(top_n)['category'].tolist()
    filtered_data = inventory_data[inventory_data['category'].isin(low_inventory_cats)]

    pivot_data = filtered_data.pivot_table(
        index='category', 
        columns='subcategory', 
        values='inventory_level',
        fill_value=0
    )
  
    pivot_data = pivot_data.loc[low_inventory_cats]
    
    pivot_data.plot(kind='bar', stacked=True)
    
    plt.title('Categories with Lowest Inventory Levels')
    plt.xlabel('Category')
    plt.ylabel('Inventory Level')
    plt.xticks(rotation=45)
    plt.legend(title='Subcategory')
    
    plt.tight_layout()
    plt.show()