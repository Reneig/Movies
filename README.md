# Movies Management project 

## Project Purpose and Features

This project provides a comprehensive analysis and visualization of movie data, including user behavior, movie ratings, and genre trends. It leverages data processing, machine learning (implied by analysis notebooks), and interactive visualization to extract insights from a movie dataset. The project also includes a Streamlit application for interactive exploration of the data.

Key features include:

-   **Data Ingestion & Processing:** Handles raw movie data (e.g., `links.csv`) and processes it into structured formats (e.g., Parquet files).
-   **Exploratory Data Analysis (EDA):** Jupyter notebooks (converted to Python scripts) for in-depth analysis of movie ratings, genres, and user interactions.
-   **Data Visualization:** Interactive visualizations to present key findings and trends.
-   **Movie Poster Retrieval:** A utility script to fetch movie posters.
-   **Streamlit Web Application:** An interactive dashboard for users to explore movie data and insights.
-   **Structured Project Layout:** Organized codebase for clarity, maintainability, and scalability.

## Installation and Setup

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/films-analytics.git
    cd films-analytics
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage dependencies.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage Instructions

### 1. Data Processing and Analysis

The core data processing and analysis logic is contained within the Python scripts converted from Jupyter notebooks.

-   **`src/notebooks_converted/film_data_analysis.py`**: Contains the main data analysis steps.
-   **`src/notebooks_converted/film_dataviz.py`**: Focuses on data visualization.

You can run these scripts directly:

```bash
python src/notebooks_converted/film_data_analysis.py
python src/notebooks_converted/film_dataviz.py
```
*(Note: Ensure you have the necessary raw data in `data/raw/` before running these scripts.)*

### 2. Run the Streamlit Application

To launch the interactive Streamlit dashboard:

```bash
streamlit run src/streamlit_app/movielens_app.py
```

The application will open in your web browser, typically at `http://localhost:8501`.

### 3. Movie Poster Retrieval

To use the movie poster retrieval utility:

```bash
python src/get_movie_poster.py
```
*(Note: This script might require additional configuration or API keys depending on its implementation.)*

## Onboarding Guidance for New Developers

Welcome to the Films Analytics Project! Here's a guide to help you get started:

-   **Project Structure:**
    -   `.venv/`: Python virtual environment.
    -   `data/`:
        -   `raw/`: Stores raw, unprocessed datasets (e.g., `links.csv`).
        -   `processed/`: Contains processed data, analysis results, and generated artifacts (e.g., Parquet files, pickle files).
    -   `docs/`: Contains documentation-related assets, such as architecture diagrams and images.
    -   `src/`: Contains all source code.
        -   `notebooks_converted/`: Python scripts converted from original Jupyter notebooks, containing data analysis and visualization logic.
        -   `streamlit_app/`: Source code for the Streamlit web application.
        -   `get_movie_poster.py`: Utility script for fetching movie posters.
    -   `README.md`: This project overview.
    -   `requirements.txt`: Project dependencies.

-   **Key Files & Directories:**
    -   `data/raw/links.csv`: The primary raw dataset.
    -   `src/notebooks_converted/film_data_analysis.py`: Core data processing.
    -   `src/notebooks_converted/film_dataviz.py`: Core data visualization.
    -   `src/streamlit_app/movielens_app.py`: Main entry point for the Streamlit app.

-   **Development Workflow:**
    1.  Set up your environment as described in "Installation and Setup."
    2.  Familiarize yourself with the data in `data/raw/`.
    3.  Explore the `src/notebooks_converted/` scripts to understand the data processing and analysis pipelines.
    4.  Run the Streamlit app to see the interactive dashboard.
    5.  For contributions, create a new branch, implement your changes, and ensure all existing functionalities remain intact.

## Technical Stack and Architecture Overview

### Tech Stack

-   **Python:** Core programming language.
-   **Pandas, NumPy:** For data manipulation and analysis.
-   **Plotly Express:** For interactive data visualization.
-   **Streamlit:** For building interactive web applications/dashboards.
-   **PyArrow, Parquet:** For efficient data storage and retrieval.
-   **Joblib, Pickle:** For serialization/deserialization of Python objects.
-   **`filmsdk`:** (Specific library, if used for movie data interaction).
-   **Virtual Environments:** For dependency management.

### Architecture

The project follows a modular architecture:

1.  **Data Layer:** Raw data (`links.csv`) is stored in `data/raw`. Processed and derived data are stored in `data/processed` (e.g., Parquet files for efficient access).
2.  **Analysis Layer:** Python scripts (`src/notebooks_converted/`) perform data cleaning, transformation, analysis, and generate insights.
3.  **Application Layer:** The Streamlit application (`src/streamlit_app/`) consumes the processed data and provides an interactive user interface for exploration.
4.  **Utility Layer:** Helper scripts like `src/get_movie_poster.py` provide specific functionalities.

This layered approach promotes separation of concerns, making the project scalable and easier to maintain.

## Highlights of Your Expertise

This project demonstrates my proficiency in:

-   **Data Engineering:** Handling raw data, designing data processing pipelines, and managing data storage formats (Parquet).
-   **Data Science & Analytics:** Performing exploratory data analysis, extracting insights, and applying data visualization techniques.
-   **MLOps Fundamentals:** Structuring projects for maintainability, managing dependencies, and preparing for deployment.
-   **Interactive Application Development:** Building user-friendly web applications with Streamlit for data exploration.
-   **Python Development:** Writing clean, modular, and efficient Python code.
-   **Problem Solving:** Addressing data challenges and integrating various tools and libraries.

## Future Improvements

-   **Automated Data Pipelines:** Implement tools like Apache Airflow or Prefect for orchestrating data processing workflows.
-   **Database Integration:** Store processed data in a more robust database (e.g., PostgreSQL, Snowflake) instead of just files.
-   **Advanced ML Models:** Explore more sophisticated machine learning models for recommendations or predictive analytics.
-   **Containerization:** Dockerize the Streamlit application for easier deployment.
-   **CI/CD:** Set up continuous integration and deployment for automated testing and releases.
-   **Testing:** Implement unit and integration tests for data processing, utility functions, and the Streamlit application.
-   **Performance Optimization:** Optimize data loading and processing for larger datasets.
-   **User Authentication/Authorization:** For a production-grade Streamlit app.