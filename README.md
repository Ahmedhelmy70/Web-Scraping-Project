# Books Data Analysis & Visualization

This project processes a book dataset scraped from [books.toscrape.com](https://books.toscrape.com), performs data cleaning, generates visualizations, and stores the processed data in a MongoDB database. It’s a great example of end-to-end data analysis, combining data preprocessing, visualization, and database integration using Python.

## Features
- **Data Cleaning**: Extracts numeric prices from text (e.g., `Â£45.17` to `45.17`) using regular expressions (`re`) and converts text ratings (e.g., "Three") to numeric values.
- **Visualizations**: Generates four insightful plots using Seaborn and Matplotlib:
  - Bar plot: Number of books per genre.
  - Box plot: Price distribution across top 10 genres.
  - Scatter plot: Price vs. rating, colored by genre.
  - Histogram: Distribution of book prices.
- **Database Storage**: Stores the processed dataset in a MongoDB collection for persistent storage and querying.
- **Technologies**: Built with Python, Pandas, Seaborn, Matplotlib, and PyMongo.

## Dataset
The dataset (`books.csv`) contains book information from books.toscrape.com, with columns:
- `Title`: Book title.
- `Price`: Price in pounds (e.g., `Â£45.17`).
- `Availability`: Stock status (e.g., "In stock").
- `Rating`: Text rating (e.g., "One" to "Five").
- `Product Page`: URL to the book’s page.
- `Genre`: Book genre (e.g., "Fiction", "Mystery").

## Visualizations
The project generates four separate visualizations, saved as PNG files:
1. **Genre Distribution**: Bar plot showing the number of books per genre.
2. **Price by Genre**: Box plot of price distributions for the top 10 genres.
3. **Price vs. Rating**: Scatter plot exploring the relationship between price and rating, colored by genre.
4. **Price Distribution**: Histogram of book prices with a kernel density estimate.

## Requirements
- Python 3.8+
- MongoDB (local or remote, e.g., MongoDB Atlas)
- Libraries: `pandas`, `matplotlib`, `seaborn`, `pymongo`
