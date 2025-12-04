import pandas as pd

df1=pd.read_csv("customers.csv")
print(df1)

df2=pd.read_csv('orders.csv')
print(df2)

# 2. Merge customers + orders using customer_id

df_combined=pd.merge(df1,df2,on="customer_id",how='inner')
print(df_combined)

# ✔ 3. Find total amount spent per customer
res=df_combined.groupby(['name','customer_id'])['amount'].sum().sort_values(ascending=False)
print(res)

# ✔ 4. Find average order value per city

res2=df_combined.groupby(['city'])['amount'].aggregate(
    'mean'
).sort_values(ascending=False)
print(res2)


# Add a new column discounted_amount
# def discout()
# filter=df2['amount']>5000
# df2['discounted_amount']=df2['amount'].apply()

# ✔ 6. Get only “Grocery” category orders

cat_grocery=df2['category']=='Grocery'
print(df2[cat_grocery])

# Find the top 2 customers by spend
res=df_combined.groupby(['name'])['amount'].sum().sort_values(ascending=False).head(2)
print(res)

# Save merged clean data into customer_orders_clean.csv

df_combined.to_csv("customer_orders_clean.csv",index=True)

# highdest_order
highest_order =df_combined.groupby(['name','customer_id'])['amount'].max().sort_values(ascending=False)
print(highest_order)

def expensive(amount):
    if amount >5000:
        return "Expensive"
    else:
        return "Normal"
    
df_combined['expensive']=df_combined['amount'].apply(expensive)
print("added column")
print(df_combined)

total_revenue=df_combined.groupby('category').agg({
    'amount':'sum'
})
print(total_revenue)

pivot_table = pd.pivot_table(
    df_combined,
    values="amount",
    index="city",
    columns="category",
    aggfunc="sum",
    fill_value=0       # replaces NaN with 0
)

print(pivot_table)



df_combined.to_csv("customer_orders_clean.csv",index=False)
    
