# def clean_header(df):
# 	"""
# 	This functions removes weird characters and spaces from column names, while keeping everything lower case
# 	"""
#     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')




# https://towardsdatascience.com/automate-boring-tasks-with-your-own-functions-a32785437179
import pandas as pd
import config
df = pd.DataFrame(pd.read_excel(config.TRAINING_FILE))
print(df.columns)
print(df.dtypes)







# Defining the function that you will run later
# def calculate_vif_(X):
#     vif = pd.DataFrame()
#     vif['variables'] = X.columns
#     vif['VIF'] = [variance_inflation_factor(X.values, ix) for ix in range(X.shape[1])]
#     return vif 

# print(calculate_vif_(clean_feat))
