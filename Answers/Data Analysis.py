#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter


# #### Merging all files into one

# In[3]:


files = [file for file in os.listdir('./Sales_Data')]
all_data_month = pd.DataFrame()
for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_data_month = pd.concat([all_data_month,df])
all_data_month.to_csv("all_data.csv",index=False)


# In[4]:


df = pd.read_csv("all_data.csv")
df.head(10)


# ## Drop NaN values from DataFrame

# In[5]:


all_data = pd.read_csv("all_data.csv")
all_data = all_data.dropna()
all_data = all_data.reset_index(drop = True)
all_data.head()


# ## Removing rows based on a condition

# #### Removing rows which is not Value

# In[6]:


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
all_data.head()


# ## Add a Month Column

# In[7]:


all_data['Month'] = all_data['Order Date'].str[0:2].astype('int32')
all_data.head()


# ### Converting as integers and floats

# In[9]:


all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype('int32')
all_data['Price Each'] = all_data['Price Each'].astype('float')
all_data.head()


# ### Add a Sales Column and calculating the sales turnover

# In[11]:


all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
all_data.head()


# # 1. What was the best month for sales? How much was earned that month?

# In[16]:


results = all_data.groupby('Month').sum()
results.head(100)


# In[22]:


months = range(1,13)
plt.bar(months,results['Sales'])
plt.xticks(months)
plt.show()


# In[23]:


all_data.head()


# ### Adding a city column and get the value

# In[28]:


all_data['City'] = all_data['Purchase Address'].apply([lambda x: x.split(',')[1]])
all_data.head()


# # 2. What city sold the most product?

# In[29]:


results_2 = all_data.groupby('City').sum()
results_2.head(100)


# In[41]:


cities = [city for city, df in all_data.groupby(['City'])]
plt.bar(cities,results_2['Quantity Ordered'])
plt.xticks(cities,rotation = 'vertical')
plt.show()


# # 3. What time should we display advertisemens to maximize the likelihood of customer’s buying product?

# In[43]:


all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data.head()


# ### Adding Hour and minute column and alculations for that

# In[44]:


all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
all_data.head()


# In[50]:


hour = [hour for hour, df in all_data.groupby('Hour')]
plt.plot(hour,all_data.groupby(['Hour']).count())
plt.xticks(hour)
plt.grid()
plt.show()


# # 4. What products are most often sold together?

# In[68]:


df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID', 'Grouped']].drop_duplicates()
df.head(100)


# ### Counting pairs of products

# In[75]:


count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))
count.most_common(10)


# # 5. What product sold the most? Why do you think it sold the most?

# In[98]:


product_df = all_data.groupby('Product')
quantity_ordered = product_df.sum()['Quantity Ordered']
products = [product for product, df in product_df]

plt.bar(products,quantity_ordered)
plt.xticks(products,rotation = 'vertical')
plt.show()

