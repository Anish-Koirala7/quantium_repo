import pandas as pd

df1 = pd.read_csv('./data/daily_sales_data_0.csv')
df2 = pd.read_csv('./data/daily_sales_data_1.csv')
df3 = pd.read_csv('./data/daily_sales_data_2.csv')

df= pd.concat([df1, df2, df3], ignore_index=True)

pink_df=df[df['product'] == "pink morsel"]
pink_df["price"] = pink_df["price"].astype(str).str.replace('$', '', regex=False).astype(float)
pink_df['Sales'] = pink_df["price"] * pink_df["quantity"]
final_df=pink_df.drop(columns=["price", "quantity", "product"])
print(final_df.info)
final_df.to_csv("Processed_daily_sales.csv" )