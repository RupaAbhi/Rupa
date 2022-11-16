
import pandas as pd
df = pd.read_csv('online-retail.csv')
df.head()#print the first n rows in the data frame [default n=5]

print(df)
df['LinePrice'] = df['Quantity'] * df['Unitprice']
df.head()

print(df)

df_customers = df.groupby('CustomerID').agg(orders=('InvoiceData', 'nunique'), skus=('Stockcode', 'nunique'), quantity=('Quantity', 'sum'), revenue=('Lineprice', 'sum'),).reset_index()

df_customers.head()

print(df_customers)

