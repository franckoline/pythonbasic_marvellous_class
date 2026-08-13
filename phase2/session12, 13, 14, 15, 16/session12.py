import pandas as pd
import numpy as np

#DATA INGESTION
df = pd.read_csv("session12_bulk_price_matrix.csv", index_col = "Item_ID")

print(df.to_string())

array_of_prices = (df[["Cost_Price_NGN", "Retail_Price_NGN"]]).to_numpy()
np.set_printoptions(threshold = np.inf)

array_of_prices[:, 1] *= 0.9
print(array_of_prices[:, 1])

food = df[df["Category"] == "Food"]
prices_of_food = (food[["Cost_Price_NGN", "Retail_Price_NGN"]]).to_numpy()
print(prices_of_food)

prices_of_food[:, 1] *=0.95

print(df[df["Category"] == "Food"][["Cost_Price_NGN", "Retail_Price_NGN"]])

array_of_prices = df[["Cost_Price_NGN", "Wholesale_Price_NGN", "Retail_Price_NGN"]].to_numpy()

print(array_of_prices)

array_of_prices[:, 0] *= 0.5
array_of_prices[:, 1] *= 0.85
array_of_prices[:, 2] *= 0.95

df["Cost_Price_NGN","Wholesale_Price_NGN", "Retail_Price_NGN" ] = array_of_prices

prices = df[["Cost_Price_NGN", "Retail_Price_NGN"]].to_numpy()


# DATA WRANGLING
Profit = prices[: , 1] - prices[:, 0]
df["Profit"] = Profit
top_five = df["Profit"].nlargest(5)
print(top_five)

# THE CLEANING LAB
df = pd.read_csv("dataset.csv")

df = df.fillna({"Stock_Quantity" : 0,"Retail_Price_NGN" : 0})
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df = df.drop_duplicates().reset_index(drop = True)
df = df.drop([2, 3]).reset_index(drop = True)
print(df)

#FEATURE CREATION
df = pd.read_csv("session12_bulk_price_matrix.csv", index_col = "Item_ID")
time = pd.date_range(start = "2025-04-02", periods = len(df), freq = "2D")

df["Timestamp"] = time
print(df["Timestamp"].dtype)
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
day_of_the_week = df["Timestamp"].dt.day_name()
print(day_of_the_week)
df["Day of week"] = day_of_the_week
group = df.groupby("Day of week")
print(group.count())