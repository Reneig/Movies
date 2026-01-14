# Movies Management project 


[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Container-2496ED.svg)](https://www.docker.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg)](https://sqlite.org/)

# 👥 Project Authors
- **GBODOGBE Zinsou René**
- **COMLAN Yayra Cybelle**
- **DOMINGO Giovanni**

---

## 📌 Project Overview

### Project Context
Imagine a fictional company, **CineData Insights**, aiming to revolutionize the movie-going experience through an intelligent platform that leverages movie data. Their ambition? **To create a high-performance data analytics system** for streaming platforms, movie enthusiasts, and production studios. But there is a problem… **their data is in a chaotic state!**

The data is scattered across several CSV files, making any form of analysis tedious. There is no centralized system to efficiently query information about movies, user ratings, or associated tags. This is **where we come in**, as **versatile Data Consultants**. Our mission is to transform raw MovieLens data chaos into a powerful and interactive data ecosystem, ultimately building an intelligent movie analytics platform.

To successfully complete this project, the following phases were carried out:

---

## **Phase 1: Python Developer & API Architect**

**Objective: Build a robust API to centralize and expose MovieLens data.**

🔹 **Database Design**  
- Model the SQL database from CSV files  
- Use **SQLite** for efficient data storage  
- Manage relationships between movies, users, ratings, and tags  

🔹 **API Development with FastAPI**  
- Design an **API** to easily query movies and user ratings  
- Integrate **Pydantic** for input data validation  
- Use **SQLAlchemy** for database query management  

🔹 **API Deployment**  
- Host the API on a public cloud (**Render**)  
- Provide an **on-premise** version using Docker  
- Secure endpoints and optimize performance  

🔹 **Python Package Creation**  
- Develop a **Python package** that allows users to easily interact with the API  
- Publish the package on **PyPI** so it can be reused in other projects  

**Deliverables**  
- A centralized, production-ready database  
- A documented and deployed FastAPI API  
- A user-friendly and well-documented Python SDK  

---

## **Phase 2: Data Analyst – Exploration and Visualization**

**Objective: Explore and analyze the data by querying the API.**

🔹 **Exploratory Data Analysis (EDA)**  
- Use the **Python package** to query the API and retrieve data  
- Identify trends in movie ratings  
- Analyze the most popular genres and user preferences  

🔹 **Building a Data App with Streamlit**  
- Create an **interactive application** to visualize movie trends  
- Integrate **dynamic tables** and **interactive charts**  
- Provide **advanced movie search** based on ratings and genres  

**Deliverables**  
- An interactive exploratory analysis notebook  
- A **Streamlit web application** connected to the API that presents insights interactively to stakeholders  

---


Before executing the different steps, we first did the following:

## Create and clone the GitHub repository locally

# Clone the repository

git clone [https://github.com/Reneig/Movies.git](https://github.com/Reneig/Movies.git)

```bash
cd Movies
```
# Create the virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
```
# Install the dependencies
```bash
pip install -r requirements.txt
```
# Dataset

---

# MovieLens Dataset – Data Description

The MovieLens dataset is a public dataset provided by GroupLens, containing information about movies, user ratings, and tags assigned to movies. It is widely used for research and experimentation in the field of recommendation systems.

## Files and Data Structure

### 1. movies.csv
Contains the list of movies with their unique identifier, title, and genres.

**Columns:**
- `movieId`: Unique movie identifier (primary key).
- `title`: Movie title, including the release year in parentheses.
- `genres`: List of genres associated with the movie, separated by "|".

**Example:**
```
movieId,title,genres
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
2,Jumanji (1995),Adventure|Children|Fantasy
```

---

### 2. ratings.csv
Contains movie ratings provided by users.

**Columns:**
- `userId`: Unique user identifier (primary key with `movieId`).
- `movieId`: Identifier of the rated movie (foreign key referencing `movies.movieId`).
- `rating`: Rating given by the user (from 0.5 to 5.0, in 0.5 increments).
- `timestamp`: Rating timestamp.

**Example:**
```
userId,movieId,rating,timestamp
1,1,4.0,964982703
2,1,4.5,847434962
```

---

### 3. tags.csv
Contains tags assigned to movies by users.

**Columns:**
- `userId`: Unique user identifier.
- `movieId`: Identifier of the related movie (foreign key referencing `movies.movieId`).
- `tag`: Textual tag associated with the movie.
- `timestamp`: Timestamp of the tag creation.

**Example:**
```
userId,movieId,tag,timestamp
15,339,atmospheric,1138537770
```

---

### 4. links.csv
Contains external movie identifiers from other databases (IMDB and TMDb).

**Columns:**
- `movieId`: Movie identifier (primary key, references `movies.movieId`).
- `imdbId`: IMDB identifier of the movie.
- `tmdbId`: TMDb (The Movie Database) identifier of the movie.

**Example:**
```
movieId,imdbId,tmdbId
1,0114709,862
2,0113497,8844
```

---

---

## Structure  SQLite3 database

To store this data in a SQLite3 database, we define the following structure::

### Table `movies`
```sql
CREATE TABLE movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genres TEXT
);
```

### Table `ratings`
```sql
CREATE TABLE ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL CHECK(rating >= 0.5 AND rating <= 5.0),
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

### Table `tags`
```sql
CREATE TABLE tags (
    userId INTEGER,
    movieId INTEGER,
    tag TEXT,
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId, tag),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

### Table `links`
```sql
CREATE TABLE links (
    movieId INTEGER PRIMARY KEY,
    imdbId TEXT,
    tmdbId INTEGER,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

## Table Relationships
- `ratings.movieId`, `tags.movieId`, and `links.movieId` are foreign keys since `movies.movieId`.
- The tables `ratings` and `tags` use `userId` and `movieId` like composite primary key.

This structure ensures data integrity while facilitating movie analysis and recommendation

#  SQLite3 database and table creation

```bash
(.venv) vant@MOOVE15:~/Desktop/AMSE2/software/Movies/Movies$ sqlite3 movies.db
```

```sql
CREATE TABLE movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genres TEXT
);
```

```sql
CREATE TABLE ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL CHECK(rating >= 0.5 AND rating <= 5.0),
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

```sql
CREATE TABLE tags (
    userId INTEGER,
    movieId INTEGER,
    tag TEXT,
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId, tag),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

```sql
CREATE TABLE links (
    movieId INTEGER PRIMARY KEY,
    imdbId TEXT,
    tmdbId INTEGER,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

# Loading Data into SQLite3 Tables

## Enabling foreign keys

```sql
PRAGMA foreign_keys = ON;
```

The **`PRAGMA foreign_keys = ON;`** command in SQLite is used to **enable foreign keys**.  This ensures that all foreign key constraints will be enforced.

### **Explanation:**

- SQLite **does not check** foreign key constraints by default.
- This command **enables** referential integrity, which means that:
  - A foreign key value must match an existing primary key.
  - If a referenced row is deleted or modified, this may result in an error or trigger a defined action (e.g., `ON DELETE CASCADE`).


## Prepare the import statement to recognize the CSV format with the following command:

```sql
.mode csv
```

## Loading data from CSV files into tables

### Loading


```sql
.import --skip 1 data/movies.csv movies
```

```sql
.import --skip 1 data/ratings.csv ratings
```

```sql
.import --skip 1 data/tags.csv tags
```

```sql
.import --skip 1 data/links.csv links
```

## 🌐 API created and deployed on the Cloud (Render)

The API is hosted on **Render** and benefits from continuous integration. Each update to the main branch of the GitHub repo triggers a new build of the Docker container.

* **Live API link:** [https://movies-management-0ypw.onrender.com](https://movies-management-0ypw.onrender.com)
* **Interactive documentation (Swagger UI):** [https://movies-management-0ypw.onrender.com/docs](https://movies-management-0ypw.onrender.com/docs)

---

## 🐳 Containerization (Docker)

The entire API has been encapsulated in a Docker image. This ensures that the application runs the same way on your local machine as it does on the **Render** server, by isolating all dependencies.



### 🏗️ Launching the API with Docker
If you have Docker installed, you can start the ecosystem without manually configuring the Python environment. Go to the /app folder of our project and run the following bash commands:

```bash
# Build the image
docker build -t moviemanagement-api .

# Launch the container
docker run -p 8000:8000 moviemanagement-api
```


## 📦 Python package: `moviemanagement`

To facilitate data exploitation, we have developed and published a Python package (SDK) that acts as an interface between the API and the end user.

[![PyPI version](https://img.shields.io/pypi/v/moviemanagement.svg)](https://pypi.org/project/moviemanagement/)
[![PyPI downloads](https://img.shields

Translated with DeepL.com (free version)


### 🚀 Installation
Le package est disponible sur le dépôt officiel **PyPI** et peut être installé via `pip` :

```bash
pip install moviemanagement

```
---

## 📊 Data App: Streamlit Interface

The final step in our ecosystem is an interactive web application developed with **Streamlit**. It consumes data via our `moviemanagement` package to provide a seamless user experience.

* **Live application link:** [https://movies-9wt5bi7ktwyh5ezegunxcq.streamlit.app](https://movies-9wt5bi7ktwyh5ezegunxcq.streamlit.app)

### 🚀 Local launch
To compile and launch the Streamlit interface on your machine, follow these steps:

1. **Navigate to the project folder:**

```bash
   cd Streamlit
```
For the Movie Explorer page of the application to work, you must wake up the API on Render each time. Here is the link to access the API on Render: ([https://movies-management-0ypw.onrender.com](https://movies-management-0ypw.onrender.com))

2. **Run the Streamlit application file**

```python
 streamlit run movielens_app.py
```
You can access the application at: ([https://movies-5g88tflnmyxvdhyfqzchou.streamlit.app/](https://movies-5g88tflnmyxvdhyfqzchou.streamlit.app/))