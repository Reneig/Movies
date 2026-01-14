import streamlit as st
import pandas as pd
import plotly.express as px
import os
from pathlib import Path
from utils import load_parquet_data

# Define the output directory
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "Data_visualization" / "output"

st.title("🏷️ Tags Insights")

# Loading datasets
tag_df = load_parquet_data("user_tag_stats.parquet")
tags_good_rating_df = load_parquet_data("tags_good_ratings.parquet")
tags_compare_df = load_parquet_data("tags_compare.parquet")
tags_by_genre_df = load_parquet_data("tags_by_genre.parquet")

# Chart 1: Top tags used by users
fig_user_tags = px.bar(
    tag_df, x="count", y="tag", orientation="h",
    title="Top Tags Used by Users",
    labels={"count": "Usage Count", "tag": "Tag"},
    color="count", color_continuous_scale="viridis"
)
fig_user_tags.update_layout(yaxis={'categoryorder': 'total ascending'}, height=500)

# Chart 2: Tags in highly rated movies
fig_good_tags = px.bar(
    tags_good_rating_df,
    x="count",
    y="tag",
    orientation="h",
    title="Most Frequent Tags in Highly Rated Movies (Rating ≥ 4)",
    labels={"count": "Number of Occurrences", "tag": "Tag"},
    color="count",
    color_continuous_scale="viridis"
)
fig_good_tags.update_layout(yaxis={'categoryorder': 'total ascending'}, height=500)


# Chart 3: Comparison of tags for highly rated vs. poorly rated movies
tags_compare_melted = tags_compare_df.melt(
    id_vars="tag",
    value_vars=["count_good", "count_bad"],
    var_name="Type",
    value_name="count"
)
fig_compare_tags = px.bar(
    tags_compare_melted,
    x="count",
    y="tag",
    color="Type",
    barmode="group",
    title="Tag Comparison: Highly Rated vs. Poorly Rated Movies",
    labels={"count": "Number of Occurrences", "tag": "Tag"},
    height=500
)
fig_compare_tags.update_layout(yaxis={'categoryorder': 'total ascending'})

# Displaying in 3 columns
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig_user_tags, use_container_width=True)
with col2:
    st.plotly_chart(fig_good_tags, use_container_width=True)
with col3:
    st.plotly_chart(fig_compare_tags, use_container_width=True)

st.divider()

# Preparing data for the final chart
top_tags_by_genre = tags_by_genre_df.groupby("genre").apply(
    lambda g: g.nlargest(3, 'count')
).reset_index(drop=True)
top_tags_by_genre["tag_label"] = top_tags_by_genre["tag"] + " (" + top_tags_by_genre["genre"] + ")"

# Genre multi-selector
all_genres = sorted(top_tags_by_genre["genre"].unique())
selected_genres = st.multiselect(
    "🎯 Select genres to display:",
    options=all_genres,
    default=all_genres
)

# Reactive dataframe based on selected genres
filtered_tags = top_tags_by_genre[top_tags_by_genre["genre"].isin(selected_genres)]

# Final chart: Top 3 tags per genre
fig_tags_by_genre = px.bar(
    filtered_tags.sort_values("count"),
    x="count",
    y="tag_label",
    color="genre",
    orientation="h",
    title="Top 3 Most Used Tags by Genre",
    labels={"count": "Number of Occurrences", "tag_label": "Tag (Genre)"},
    height=800
)
fig_tags_by_genre.update_layout(yaxis=dict(categoryorder='total ascending'))

# Full-width chart display
st.plotly_chart(fig_tags_by_genre, use_container_width=True)