
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

#writinging data to pd dataframes
df_csv = pd.read_csv('Raw/customer_data.csv' ,index_col=False)

df_json = pd.read_json('Raw/transactions.json')

df_xml = pd.read_xml('Raw/products.xml')

#changing column type
df_json['customer_id'] = df_json['customer_id'].fillna(0).astype(np.int64)
df_json['quantity'] = df_json['quantity'].fillna(0).astype(np.int64)


#checking data quality
#profile = ProfileReport(df_csv, title="Customer Data Report")
#print(profile)

#profile = ProfileReport(df_json, title="Customer Data Report")
#print(profile)

#profile = ProfileReport(df_xml, title="Customer Data Report")
#print(profile)

#dropping rows with null values
df_csv_cleaned = df_csv.dropna( axis=0, how="any",subset=['email','gender'])


df_xml_cleaned = df_xml.dropna( axis=0, how="any",subset='price')

#writing cleaned data to csv
df_csv_cleaned.to_csv('Transformed/customer_data.csv', index=False)

df_json.to_csv('Transformed/transactions.csv', index=False)

df_xml_cleaned.to_csv('Transformed/products.csv', index=False)


