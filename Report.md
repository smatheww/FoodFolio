# The Development of FoodFolio: A Nutrition Program using Python

## Overview
The goal for this project was to develop a software application that helps users in managing their diet by providing recipe recommendations based on the user’s personal goals and the nutritional content of the recipes. This application consists of multiple components including data preprocessing, a backend server using Flask, an SQLite database, and a front end interface for user interaction.

## System Architecture
The system is divided into several Python scripts and modules, each handling a specific part of the application:

1. **Data Preprocessing (`main.py`):**
   - **Pandas** is used for data manipulation 
   - **Scikit-learn** is used for data scaling
   - This script handles the initial data cleaning, feature engineering, and preparation. It also loads the dietary data, removes unnecessary columns, renames columns for consistency through the program, calculates nutritional ratios, and data normalization.

2. **Database Management (`database.py`):**
   - **SQLite3** is used for database operations
   - This script creates a database connection and inserts the processed data into a table.

3. **Clustering and Recommendations (`kmeans.py`):**
   - **Scikit-learn** is used for machine learning
   - **Joblib** is used for model serialization
   - This script implements a k-means clustering model that categorizes recipes into groups based on their nutritional content, facilitating targeted recommendations.

4. **API Server (`flaskapp.py`):**
   - **Flask** is used for the web framework
   - **SQLite3** is used for database queries
   - This script is the API backend and handles HTTP requests for retrieving and displaying recipes, user authentication, and providing recipe recommendations based on clustering.

5. **Front-End Development:**
   - Technologies used: **HTML, CSS, JavaScript, React**

6. **Testing (`test_database.py`):**
   - **SQLite3** is used for testing database interactions
   - This script handles the tests for the database queries to ensure the integrity of operations such as updating records and fetching data.

## Feature Engineering
The data includes several calculated features such as total calories, ratios of macronutrients to total calories, and a health index based on these ratios. These features help to support the functionality of the k-means algorithm to effectively group the recipes.

## Clustering Algorithm
K-means clustering is used to group the recipes into similar clusters so that the system can recommend recipes from a cluster that closely matches the user’s dietary preferences, which are inputted into the API.

## Front-End Interface
Details about how the front-end is implemented and functions to provide user interaction and display the recommendations effectively.

## Challenges
[Discussion of any challenges faced during the development and deployment of the application, and how they were resolved.]

## Conclusion
[Summary of the project outcomes, benefits to users, and any future directions for development.]
