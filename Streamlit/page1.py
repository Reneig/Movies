import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
from utils import load_parquet_data

# Output directory definition
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "Data_visualization" / "output"
st.title("🎬 General Movie & Ratings Analysis")

# Cache function to load parquet files
@st.cache_data
def load_parquet_data(file_name):
    file_path = OUTPUT_DIR / file_name
    return pd.read_parquet(file_path)

# Data Loading
genre_df = load_parquet_data("genre_df.parquet")
genre_rating_stats = load_parquet_data("genre_rating_stats.parquet")
# st.write(genre_rating_stats.head(10)) # Optional: Displaying raw data
movies_by_year = load_parquet_data("movies_by_year.parquet")
top_movies = load_parquet_data("top_movies_by_ratings.parquet")
ratings_df = load_parquet_data("ratings.parquet")

# Chart 1: Top 10 Genres by Number of Movies
fig_genre = px.bar(
    genre_df,
    x="count",
    y="genre",
    title="Top 10 Genres by Number of Movies",
    labels={"genre": "Genre", "count": "Number of Movies"},
    color="count",
    color_continuous_scale="viridis",
    orientation='h'
)
fig_genre.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=350
)

# Chart 2: Top 10 Genres by Number of Ratings and Average Rating
top10_genre_stats = genre_rating_stats.sort_values("rating_count", ascending=False).head(10)
fig_genre_rating = px.bar(
    top10_genre_stats,
    x="rating_count",
    y="genre",
    orientation="h",
    color="avg_rating",
    color_continuous_scale="viridis",
    title="Top 10 Genres by Number of Ratings and Average Rating",
    labels={"genre": "Genre", "rating_count": "Number of Ratings", "avg_rating": "Average Rating"}
)
fig_genre_rating.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=350
)

# Chart 4: Top 20 Movies by Number of Ratings
fig_top_movies = px.bar(
    top_movies.sort_values("rating_count", ascending=True),
    x="rating_count",
    y="title",
    color="avg_rating",
    orientation="h",
    title="Top 20 Movies by Number of Ratings",
    labels={"title": "Movie Title", "rating_count": "Number of Ratings", "avg_rating": "Average Rating"},
    color_continuous_scale="viridis"
)
fig_top_movies.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=700
)

# Chart 5: Number of Movies per Year
fig_by_year = px.bar(
    movies_by_year,
    x="year",
    y="movie_count",
    title="Total Number of Movies per Year (Based on Title)",
    labels={"year": "Year", "movie_count": "Number of Movies"},
)
fig_by_year.update_layout(
    xaxis_title="Year",
    yaxis_title="Number of Movies",
    height=500
)

# Streamlit Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.plotly_chart(fig_genre, use_container_width=True)
    st.plotly_chart(fig_genre_rating, use_container_width=True)

with col2:
    st.plotly_chart(fig_top_movies, use_container_width=True)

st.divider()

st.plotly_chart(fig_by_year, use_container_width=True)