import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Telco_customer_churn.csv")

print(df.head())
print(df.shape)
print(df.columns)

print(df.isna().sum().sum())
#print(df.dtypes)

