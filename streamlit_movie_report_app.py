import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('C:/Users/Chris/Desktop/Datasets/movie_dataset.csv')

# Preprocessing if necessary (e.g., fill or drop missing values)
# # Fill missing values for 'Revenue (Millions)' and 'Metascore' with their mean values
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace=True)
df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)

# Convert 'Year' to a categorical type for better charting
df['Year'] = df['Year'].astype('category')

# Ensure no negative values in columns like 'Runtime (Minutes)', 'Rating', 'Votes'
# Set hypothetical minimum values of 0, in case there were any such cases
df['Runtime (Minutes)'] = df['Runtime (Minutes)'].clip(lower=0)
df['Rating'] = df['Rating'].clip(lower=0)
df['Votes'] = df['Votes'].clip(lower=0)

# You might also want to ensure that all numerical columns are of a float or int type

# Convert columns to numeric if they are not already
numerical_columns = ['Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']

for col in numerical_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
# The above is particularly important for columns that will be used in calculations or charts

# Streamlit app layout
st.title('Movie Dataset Insights')

# Dropdown for selecting the type of chart
chart_type = st.selectbox('Select the type of chart you want to see:', ['Rating Distribution', 'Revenue by Year', 'Runtime Distribution', 'Votes by Rating', 'Metascore Distribution'])

if chart_type == 'Rating Distribution':
    fig, ax = plt.subplots()
    sns.histplot(df['Rating'], bins=20, kde=True, color='skyblue', ax=ax)
    ax.set_title('Rating Distribution')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Count')
    st.pyplot(fig)

elif chart_type == 'Revenue by Year':
    df_grouped = df.groupby('Year')['Revenue (Millions)'].sum().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(x='Year', y='Revenue (Millions)', data=df_grouped, color='green', ax=ax)
    ax.set_title('Total Revenue by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Revenue (Millions)')
    st.pyplot(fig)

elif chart_type == 'Runtime Distribution':
    fig, ax = plt.subplots()
    sns.histplot(df['Runtime (Minutes)'], bins=20, color='red', ax=ax)
    ax.set_title('Runtime Distribution')
    ax.set_xlabel('Runtime (Minutes)')
    ax.set_ylabel('Count')
    st.pyplot(fig)

elif chart_type == 'Votes by Rating':
    fig, ax = plt.subplots()
    sns.scatterplot(x='Rating', y='Votes', data=df, color='purple', ax=ax)
    ax.set_title('Votes by Rating')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Votes')
    st.pyplot(fig)

elif chart_type == 'Metascore Distribution':
    fig, ax = plt.subplots()
    sns.histplot(df['Metascore'], bins=20, color='orange', ax=ax)
    ax.set_title('Metascore Distribution')
    ax.set_xlabel('Metascore')
    ax.set_ylabel('Count')
    st.pyplot(fig)

