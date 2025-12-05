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
def discout(amount):
    if amount>5000:
        return amount*0.9
    else:
        return amount*0.95
# filter=df2['amount']>5000
df_combined['discounted_amount']=df_combined['amount'].apply(discout)

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
    aggfunc=["sum",'mean'],
    fill_value=0       # replaces NaN with 0
)

print(pivot_table)



df_combined.to_csv("customer_orders_clean.csv",index=False)
    
pivot__4=pd.pivot_table(
    df_combined,
    columns='category',
    index='city',
    values='amount',
    fill_value=0,
    aggfunc=['sum','mean','count']
)
print(pivot__4)

def order_value(amount):
    if amount>5000:
        return "High"
    elif amount>=2000 and amount<5000:
        return "Medium"
    else:
        return 'Low'
    
df_combined['order_value_category']=df_combined['amount'].apply(order_value)

print(df_combined)

# domain=df_combined['email'].str.split('@')[1]
filter=df_combined['order_value_category']=='High'
city_wize=df_combined[filter].groupby('city').agg({
    'order_value_category':'count'
})
print(city_wize)


df_combined.drop_duplicates(inplace=True)
df_combined.sort_values(by='discounted_amount',ascending=False,inplace=True)
print(df_combined)

df_combined.to_csv('day4_cleaned_output.csv',index=False)