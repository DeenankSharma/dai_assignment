
def calculate_null_precent(df,field):
  return df[field].isnull().sum()/len(df[field])*100

def calc_duplicacies(df):
  return df.duplicated().sum()

def categorize_customer(duration):
    if duration <= 1:
        return 'new'
    elif 2 <= duration <= 5:
        return 'regular'
    elif duration > 5:
        return 'premium'
    
