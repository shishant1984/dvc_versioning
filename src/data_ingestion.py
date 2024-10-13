import numpy as np
import pandas as pd
import os

data_file = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

# print (data_file.head())

data_file = data_file.iloc[:,3:] # Remove Address/Avatat and email
data_file = data_file[data_file['Length of Membership']>1] # Keep just data with more than 3 year membership
data_file.drop(columns=['Avg. Session Length'],inplace=True)

data_file.to_csv(os.path.join('data','customer_data.csv')) # Save processed file at data folder with name customer_data.csv.Version 1 of data.