import pandas as pd
import numpy as np

#Read the above excel file in python.
data = {
    'ticker': ['GOOGL', 'WMT', 'MSFT', 'RIL', 'TATA'],
    'eps': [27.82, 4.61, -1, 'not available', 5.6],
    'revenue': [87, 484, 85, 50, -1],
    'price': [845, 65, 64, 1023, 'n.a.'],
    'people': ['larry page', 'n.a.', 'bill gates', 'mukesh ambani', 'ratan tata']
}

df = pd.DataFrame(data)

#Include column names in this file. Use ‘ticker’, ‘eps’, ‘revenue’, ‘price’, ‘people’ as column names.
df.columns = ['ticker', 'eps', 'revenue', 'price', 'people']

#Convert all not available or n.a. values to NAN and also convert negative revenues to NAN because revenues can never be negative.
df.replace(['not available', 'n.a.'], np.nan, inplace=True)
df['eps'] = pd.to_numeric(df['eps'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df.loc[df['revenue'] < 0, 'revenue'] = np.nan

# e. Fill NaN values with appropriate values
df['eps'].fillna(df['eps'].mean(), inplace=True)
df['revenue'].fillna(df['revenue'].median(), inplace=True)
df['price'].fillna(method='ffill', inplace=True)
df['people'].fillna('unknown', inplace=True)

#Fill NAN values using a suitable approach.
def replace_person(df):
    df.loc[df['ticker'] == 'WMT', 'people'] = 'Sam Walton'
    return df

df = replace_person(df)

#Write a function to change n.a value appearing in WMT to Sam Walton
def replace_wmt_person(df):
    if 'WMT' in df['ticker'].values:
        df.loc[df['ticker'] == 'WMT', 'people'] = 'Sam Walton'
    return df

df = replace_wmt_person(df)


#How do I write this file to a new file “new.csv”?
df.to_csv('new.csv', index=False)

print(df)
