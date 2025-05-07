import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
import os

# Set page configuration
st.set_page_config(page_title="Book Analysis Dashboard", layout="wide")

# Connect to MongoDB
@st.cache_resource
def init_connection():
    return MongoClient("mongodb://localhost:27017/")

client = init_connection()
db = client["Library"]
collection = db["books"]

# Fetch data from MongoDB
@st.cache_data
def get_data():
    data = list(collection.find())
    df = pd.DataFrame(data)
    if '_id' in df.columns:
        df = df.drop('_id', axis=1)
    return df

df = get_data()

# Title and description
st.title("Book Analysis Dashboard")
st.markdown("""
This dashboard presents an analysis of books scraped from books.toscrape.com.
Explore the data through interactive tables and visualizations.
""")

# Sidebar for filters
st.sidebar.header("Filters")
genres = sorted(df['Genre'].unique())
selected_genres = st.sidebar.multiselect("Select Genres", genres, default=genres[:5])
price_range = st.sidebar.slider("Price Range (£)", 
                               float(df['Price'].min()), 
                               float(df['Price'].max()), 
                               (float(df['Price'].min()), float(df['Price'].max())))

# Filter data
filtered_df = df[(df['Genre'].isin(selected_genres)) & 
                (df['Price'].between(price_range[0], price_range[1]))]

# Display filtered data
st.header("Book Data")
st.dataframe(filtered_df, height=400, use_container_width=True)

# Visualizations
st.header("Visualizations")

# Genre Distribution
st.subheader("Genre Distribution")
genre_counts = filtered_df['Genre'].value_counts()
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index, ax=ax1)
ax1.set_title("Number of Books per Genre")
ax1.set_xlabel("Number of Books")
ax1.set_ylabel("Genre")
st.pyplot(fig1)

# Average Price by Genre
st.subheader("Average Price by Genre")
avg_price_by_genre = filtered_df.groupby('Genre')['Price'].mean().sort_values()
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_price_by_genre.values, y=avg_price_by_genre.index, ax=ax2)
ax2.set_title("Average Price by Genre")
ax2.set_xlabel("Average Price (£)")
ax2.set_ylabel("Genre")
st.pyplot(fig2)

# Rating Distribution
st.subheader("Rating Distribution")
rating_counts = filtered_df['Rating_Numeric'].value_counts().sort_index()
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x=rating_counts.index, y=rating_counts.values, ax=ax3)
ax3.set_title("Distribution of Book Ratings")
ax3.set_xlabel("Rating (1-5)")
ax3.set_ylabel("Number of Books")
st.pyplot(fig3)

# Price Histogram
st.subheader("Price Distribution")
if os.path.exists("price_histogram.png"):
    st.image("price_histogram.png", caption="Histogram of Book Prices", use_column_width=True)
else:
    st.warning("Price histogram image not found. Please ensure 'price_histogram.png' is in the working directory.")


# Close MongoDB connection
client.close()