import pandas as pd
import matplotlib.pyplot as plt

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