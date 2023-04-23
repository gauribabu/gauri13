#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[5]:


covid_df= pd.read_csv('C:/Users/lenovo/OneDrive/Desktop/PROJECTS/data visualisation/covid_india.csv')


# In[6]:


covid_df.head(10)


# In[7]:


covid_df.info()


# In[8]:


covid_df.describe()


# In[9]:


vaccine_df=pd.read_csv('C:/Users/lenovo/OneDrive/Desktop/PROJECTS/data visualisation/COVID-19 India Statewise Vaccine Data.csv')


# In[10]:


vaccine_df.head(10)


# In[11]:


vaccine_df.info()


# In[12]:


covid_df.head(10)


# In[13]:


statewise=pd.pivot_table(covid_df,values=["Total Confirmed cases", "Deaths","Cured/Discharged/Migrated"],
                                    index="Name of State / UT", aggfunc=max)


# In[14]:


statewise["Recovery rate"]=statewise["Cured/Discharged/Migrated"]*100/statewise["Total Confirmed cases"]


# In[15]:


statewise["Mortality rate"]=statewise["Deaths"]*100/statewise["Total Confirmed cases"]


# In[16]:


statewise= statewise.sort_values(by="Total Confirmed cases", ascending=False)


# In[17]:


statewise.style.background_gradient(cmap="cubehelix")


# In[18]:


#top 10 states with active cases

top_10_active_cases=covid_df.groupby(by='Name of State / UT').max()[['Active Cases']].sort_values(by="Active Cases",ascending=False).reset_index()


# In[19]:


fig = plt.figure(figsize=(16,9))


# In[20]:


plt.title("Top 10 states with most active cases in India",size=20)


# In[21]:


ax= sns.barplot(data= top_10_active_cases.iloc[:10],y="Active Cases",x="Name of State / UT", linewidth=2,edgecolor='red')


# In[22]:


#top 10 states with most active cases

top_10_active_cases=covid_df.groupby(by='Name of State / UT').max()[['Active Cases']].sort_values(by="Active Cases",ascending=False).reset_index()
fig = plt.figure(figsize=(16,9))
plt.title("Top 10 states with most active cases in India",size=20)
ax= sns.barplot(data= top_10_active_cases.iloc[:10],y="Active Cases",x="Name of State / UT", linewidth=2,edgecolor='red')
plt.xlabel("States")
plt.ylabel("Total Active cases")
plt.show()


# In[23]:


#top states with most deaths

top_10_deaths=covid_df.groupby(by='Name of State / UT').max()[['Deaths']].sort_values(by="Deaths",ascending=False).reset_index()
fig=plt.figure(figsize=(18,5))
plt.title("Top 10 states with most deaths",size=20)
ax= sns.barplot(data=top_10_deaths.iloc[:10],y="Deaths",x='Name of State / UT',linewidth=2,edgecolor='black')
plt.xlabel("States")
plt.ylabel("Total death cases")
plt.show()


# In[24]:


vaccine_df


# In[71]:


top_5_states_vacc_doses=vaccine_df.groupby(by='State/UTs').max()[['Total Vaccination Doses']].sort_values(by="Total Vaccination Doses",ascending=False).reset_index()


# In[72]:


np_states=top_5_states_vacc_doses[['State/UTs']].to_numpy().flatten()


# In[73]:


np_states


# In[74]:


np_vacc_doses=top_5_states_vacc_doses[['Total Vaccination Doses']].to_numpy().flatten()


# In[75]:


np_vacc_doses


# In[76]:


top_5_states_vacc_doses


# In[82]:


#most vaccinated states 

fig=plt.figure(figsize=(8,8))
myexplode=[0.1,0,0,0,0]
plt.title("States/UTs with maximum vaccination doses",size=16)
plt.pie(np_vacc_doses[:5],labels=np_states[:5],explode=myexplode,autopct='%1.1f%%', textprops={'fontsize': 12})
plt.show()


# In[99]:


#states with min vaccinations
fig=plt.figure(figsize=(8,8))
myexplode=[0,0,0,0,0.1]
plt.title("States/UTs with minimum vaccination doses",size=16)
plt.pie(np_vacc_doses[-5:],labels=np_states[-5:],explode=myexplode,autopct='%1.1f%%', textprops={'fontsize': 12})
plt.show()


# In[ ]:




