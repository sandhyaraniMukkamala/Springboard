#!/usr/bin/env python
# coding: utf-8

# In[91]:


# Import storing and analysis related libraries
import numpy as np
import pandas as pd

# import visualization related libraries
import matplotlib.pyplot as plt
import seaborn as sns
from chart_studio import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import folium


# In[92]:


# import dataset
df = pd.read_csv('../../../EDA/COVID-19.csv', parse_dates=['Date'])

df1 = df.copy()
df.head()


# In[93]:


# dataframe info
df.info()


# In[94]:


# checking for missing value
df.isna().sum()


# ## Cleaning Data

# In[95]:


# replacing Mainland china with just China
df['Country/Region'] = df['Country/Region'].replace('Mainland China', 'China')

# filling missing values with NA
df[['Province/State']] = df[['Province/State']].fillna('NA')


# ## Derived Tables

# In[96]:


# Seperating the data with respect to the location
# cases in the Diamond Princess cruise ship
ship = df[df['Province/State']=='Diamond Princess cruise ship']

# cases in other locations
df = df[df['Province/State']!='Diamond Princess cruise ship']

# cases in only China
china = df[df['Country/Region']=='China']

# cases in other locations than China and ship
others = df[df['Country/Region']!='China']

# latest cases reported
latest_cases = df[df['Date'] == max(df['Date'])].reset_index()

# group the data according to locations
full_data_grouped = df.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
chinese_data_grouped = china.groupby('Province/State')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
others_grouped = others.groupby('Country/Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()


# ## Exploratory Data Analysis

# In[97]:


# latest cases reported as 26th Feb
latest = df.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].sum()
latest = latest.reset_index()
latest = latest.sort_values('Date', ascending=False)
latest.head(1).style.background_gradient(cmap='Pastel1')


# In[98]:


# Complete data grouped by latest date
temp = latest_cases.groupby(['Country/Region', 'Province/State', 'Date'])['Confirmed', 'Deaths', 'Recovered'].max()
temp.style.background_gradient(cmap='Pastel1_r')


# ## Country Wise Latest Data

# In[99]:


temp = full_data_grouped[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
temp = temp.sort_values(by='Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Pastel1_r')


# ## Chinese Province Wise Latest Data

# In[100]:


temp = chinese_data_grouped[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
temp = temp.sort_values(by='Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Pastel1_r')


# In[101]:


# Vizualizing the rise of cases from Feb 1st to Feb 26th
fig = go.Figure()
fig.add_trace(go.Bar(
                x=df["Province/State"],
                y=df["Confirmed"],
                marker_color='darkorange',
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2, 
                opacity=0.7)
             )

fig.update_layout(
    title_text='Confirmed Cases in different provinces (Till February 26, 2020)',
    height=700, width=800, xaxis_title='Province/State', yaxis_title='Confirmed')

fig.show()

fig.add_trace(go.Bar(
                x=df["Province/State"],
                y=df["Deaths"],
                marker_color='darkorange',
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2, 
                opacity=0.7)
             )

fig.update_layout(
    title_text='Death Cases in different provinces (Till February 26, 2020)',
    height=700, width=800, xaxis_title='Province/State', yaxis_title='Deaths')

fig.show()


# In[102]:


# Vizualizing the rise of cases from Feb 1st to Feb 26th
fig = go.Figure()
fig.add_trace(go.Bar(
                x=df["Country/Region"],
                y=df["Confirmed"],
                marker_color='darkorange',
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2, 
                opacity=0.7)
             )

fig.update_layout(
    title_text='Confirmed Cases in different countries (Till February 26, 2020)',
    height=700, width=800, xaxis_title='Country/Region', yaxis_title='Confirmed')

fig.show()

fig.add_trace(go.Bar(
                x=df["Country/Region"],
                y=df["Deaths"],
                marker_color='darkorange',
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2, 
                opacity=0.7)
             )

fig.update_layout(
    title_text='Death Cases in different contries (Till February 26, 2020)',
    height=700, width=800, xaxis_title='Country/Region', yaxis_title='Deaths')

fig.show()


# ## Countries with deaths reported

# In[103]:


temp = full_data_grouped[['Country/Region', 'Deaths']]
temp = temp.sort_values(by='Deaths', ascending=False)
temp = temp.reset_index(drop=True)
temp = temp[temp['Deaths']>0]
temp.style.background_gradient(cmap='Pastel1_r')


# ## Countries and Provinces with no recovered cases

# In[104]:


# Countries with no cases recovered
temp = others_grouped[others_grouped['Recovered']==0]
temp = temp[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
temp = temp.sort_values('Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Pastel1_r')


# In[105]:


# Provinces with no cases recovered
temp = chinese_data_grouped[chinese_data_grouped['Recovered']==0]
temp = temp[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
temp = temp.sort_values('Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Pastel1_r')


# ## Countries and Provinces with no affected case anymore

# In[106]:


temp = others_grouped[others_grouped['Confirmed']==
                          others_grouped['Deaths']+
                          others_grouped['Recovered']]
temp = temp[['Country/Region', 'Confirmed', 'Deaths', 'Recovered']]
temp = temp.sort_values('Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Greens')


# In[107]:


temp = chinese_data_grouped[chinese_data_grouped['Confirmed']==
                          chinese_data_grouped['Deaths']+
                          chinese_data_grouped['Recovered']]
temp = temp[['Province/State', 'Confirmed', 'Deaths', 'Recovered']]
temp = temp.sort_values('Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Greens')


# ## Countries and Provinces with all the cases recovered

# In[108]:


temp = others_grouped[others_grouped['Confirmed']==
                          others_grouped['Recovered']]
temp = temp[['Country/Region', 'Confirmed', 'Recovered']]
temp = temp.sort_values('Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Greens')


# In[109]:


temp = chinese_data_grouped[chinese_data_grouped['Confirmed']==
                          chinese_data_grouped['Recovered']]
temp = temp[['Province/State', 'Confirmed', 'Recovered']]
temp = temp.sort_values('Confirmed', ascending=False)
temp = temp.reset_index(drop=True)
temp.style.background_gradient(cmap='Greens')


# ## Diamond Princess Cruise ship Status

# In[110]:


# Cases in the Diamond Princess Cruise Ship
temp = ship.sort_values(by='Date', ascending=False).head(1)
temp = temp[['Province/State', 'Confirmed', 'Deaths', 'Recovered']].reset_index(drop=True)
temp.style.background_gradient(cmap='rainbow')


# ## Hubei - China - World

# In[111]:


def location(row):
    if row['Country/Region']=='China':
        if row['Province/State']=='Hubei':
            return 'Hubei'
        else:
            return 'Other Chinese Provinces'
    else:
        return 'Rest of the World'

temp = df.copy()
temp['Region'] = temp.apply(location, axis=1)
temp = temp.groupby('Region')['Confirmed', 'Deaths', 'Recovered'].sum().reset_index()
temp = temp.melt(id_vars='Region', value_vars=['Confirmed', 'Deaths', 'Recovered'], 
                 var_name='Case', value_name='Count').sort_values('Count')
temp.head()
fig = px.bar(temp, y='Region', x='Count', color='Case', barmode='group', orientation='h',
             text='Count', title='Hubei - China - World', 
             color_discrete_sequence= ['#EF553B', '#00CC96', '#636EFA'])
fig.update_traces(textposition='outside')
fig.show()


# ## Number of new cases everyday

# In[112]:


# In China
temp = china.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].sum().diff()
temp = temp.reset_index()
temp = temp.melt(id_vars="Date", 
                 value_vars=['Confirmed', 'Deaths', 'Recovered'])

fig = px.bar(temp, x="Date", y="value", color='variable', 
             title='Number of new cases in China everyday')
fig.update_layout(barmode='group')
fig.show()

#-----------------------------------------------------------------------------

# Others
temp = others.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].sum().diff()
temp = temp.reset_index()
temp = temp.melt(id_vars="Date", 
                 value_vars=['Confirmed', 'Deaths', 'Recovered'])

fig = px.bar(temp, x="Date", y="value", color='variable', 
             title='Number of new cases outside China everyday')
fig.update_layout(barmode='group')
fig.show()


# ## Number of Cases

# In[113]:


grouped_df = df.groupby(['Date', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered'].max()
grouped_df = grouped_df.reset_index()

temp = grouped_df[grouped_df['Country/Region']=='China'].reset_index()
temp = temp.melt(id_vars='Date', value_vars=['Confirmed', 'Deaths', 'Recovered'],
                var_name='Case', value_name='Count')
fig = px.bar(temp, x="Date", y="Count", color='Case', facet_col="Case",
            title='Cases in China')
fig.show()

temp = grouped_df[grouped_df['Country/Region']!='China'].groupby('Date').sum().reset_index()
temp = temp.melt(id_vars='Date', value_vars=['Confirmed', 'Deaths', 'Recovered'],
                var_name='Case', value_name='Count')
fig = px.bar(temp, x="Date", y="Count", color='Case', facet_col="Case",
             title='Cases Outside China')
fig.show()


# ## Number of Places to which COVID-19 Spread

# In[114]:


virus_spread_Chinese = china[china['Confirmed']!=0].groupby('Date')['Province/State'].unique().apply(len)
virus_spread_Chinese = pd.DataFrame(virus_spread_Chinese).reset_index()

fig = px.line(virus_spread_Chinese, x='Date', y='Province/State', 
              title='Number of Provinces/States/Regions of China to which COVID-19 spread over the time')
fig.show()

# ------------------------------------------------------------------------------------------

spread_others = df[df['Confirmed']!=0].groupby('Date')['Country/Region'].unique().apply(len)
spread_others = pd.DataFrame(spread_others).reset_index()

fig = px.line(spread_others, x='Date', y='Country/Region', 
              title='Number of Countries/Regions to which COVID-19 spread over the time')
fig.show()


# ## Recovery and Mortality Rate Over The Time

# In[115]:


temp = df.groupby('Date').sum().reset_index()
temp.head()

# adding two more columns
temp['No. of Deaths to 100 Confirmed Cases'] = round(temp['Deaths']/
                                                     temp['Confirmed'], 3)*100
temp['No. of Recovered to 100 Confirmed Cases'] = round(temp['Recovered']/
                                                        temp['Confirmed'], 3)*100
temp['No. of Recovered to 1 Death Case'] = round(temp['Recovered']/
                                                 temp['Deaths'], 3)

temp = temp.melt(id_vars='Date', 
                 value_vars=['No. of Deaths to 100 Confirmed Cases', 
                             'No. of Recovered to 100 Confirmed Cases', 
                             'No. of Recovered to 1 Death Case'], 
                 var_name='Ratio', 
                 value_name='Value')

fig = px.line(temp, x="Date", y="Value", color='Ratio', 
              title='Recovery and Mortality Rate Over The Time')
fig.show()


# ## Comparision between different Epidemics

# In[116]:


epidemics = pd.DataFrame({
'epidemic' : ['COVID-19', 'SARS', 'EBOLA', 'MERS', 'H1N1'],
'start_year' : [2019, 2003, 2014, 2012, 2009],
'end_year' : [2020, 2004, 2016, 2017, 2010],
'confirmed' : [1383591, 8096, 28646, 2494, 6724149],
'deaths' : [37688, 774, 11323, 858, 19654]
})

epidemics['mortality'] = round((epidemics['deaths']/epidemics['confirmed'])*100, 2)

epidemics.head()


# In[117]:


temp = epidemics.melt(id_vars='epidemic', value_vars=['confirmed', 'deaths', 'mortality'],
                      var_name='Case', value_name='Value')
fig = px.bar(temp, x="epidemic", y="Value", color='epidemic', text='Value', facet_col="Case",
             color_discrete_sequence = px.colors.qualitative.Bold)
fig.update_traces(textposition='outside')

fig.update_yaxes(showticklabels=False)
fig.layout.yaxis2.update(matches=None)
fig.layout.yaxis3.update(matches=None)
fig.show()


# In[ ]:




