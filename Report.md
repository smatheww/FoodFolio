# The Development of FoodFolio: A Nutrition Program using Python

## Overview
The goal for this project was to develop a software application that assists users in managing their diet by providing recipe recommendations based on the user’s personal goals and the nutritional content of the recipes. This application consists of multiple components including data preprocessing, a backend server using Flask, an SQLite database, and a front end interface for user interaction.

## System Architecture
The system is divided into several Python scripts and modules, each handling a specific part of the application:

### CSV Files used (`All_Diets.csv` and `processedDiet.csv`)
The file `All_Diets.csv` contains recipes from different diets and cuisines(7062 unique values), all with the aim of providing healthy and nutritious meal options.

Diet_type: The type of diet the recipe is for. (String)
Recipe_name: The name of the recipe. (String)
Cuisine_type: The cuisine the recipe is from. (String)
Protein(g): The amount of protein in grams. (Float)
Carbs(g): The amount of carbs in grams. (Float)
Fat(g): The amount of fat in grams. (Float)
Extraction_day: The day the recipe was extracted. (String)

The `processedDiet.csv` file is the preprocessed file.

### Data Preprocessing (`datapr.py`)
   - **Pandas** is used for data manipulation 
   - **Scikit-learn** is used for data scaling
   - This script handles the initial data cleaning, feature engineering, and preparation. It also loads the dietary data, removes unnecessary columns, renames columns for consistency through the program, calculates nutritional ratios, and data normalization.

### Database Management (`database.py`)
   - **SQLite3** is used for database operations
   - This script creates a database connection and inserts the processed data into a table.

### Clustering and Recommendations (`kmeans.py`)
   - **Scikit-learn** is used for the k-means clustering model
   - **Joblib** is used for model serialization
   - This script implements a k-means clustering model that categorizes recipes into groups based on their nutritional content, facilitating targeted recommendations.

### API Server (`flaskapp.py`)
   - **Flask** is used for the web framework
   - **SQLite3** is used for handling database queries
   - This script is the API backend and handles HTTP requests for retrieving and displaying recipes, user authentication, and providing recipe recommendations based on clustering.

### Front-End Development
   - Technologies used: **HTML, CSS, JavaScript**
   - This script features responsive design, user interaction through dynamic content loading, and recipe search functionality.
     
#### HTML Structure (`index.html`)
   - HTML5 is used to organize the web content into logical sections.
   - The HTML framework supports the main navigational elements, like the header with links to Home, Recipes, and About pages, and various content sections that include forms for searching recipes and displaying results.
   - The use of semantic HTML tags enhances the accessibility and search engine optimization (SEO) of the application.
      
#### CSS Styling (`styles.css`)
   - CSS is used to style the layout designed in HTML.
   - This provides a visually appealing and responsive user interface.
   - The styling is managed through an external stylesheet that ensures consistency across different sections of the application.
   - Features like flexbox and media queries are utilized to make the design responsive, adapting to variuos device screens from mobile to desktop.
     
#### JavaScript Interactivity (`script.js`)
   - JavaCcript is used to add interactivity to the FoodFolio application.
   - It handles user events such as clicks and form submissions, and can load content without needing to reload the page.
   - By using JavaScript, users can search for recipes based on keywords, with results fetched asynchonously using the Fetch API from the backend.
   - Error handling is also implemented to alert users about issues like network errors or no search results, enhancing the user experience by providng immediate feedback on their actions. 

### Testing

#### Database Testing (`test_database.py`)
   - **SQLite3** is used for testing database interactions
   - This script handles the tests for the database queries to ensure the integrity of operations such as updating records and fetching data.
     
#### API Testing (`test_api.py`)
   - Used frameworks and libraries suitable for HTTP testing (ex. Python's 'unittest' module and 'requests' library)
   - This script handles the tests for API endpoints, in particular, the accuracy of the responses provided by the Flask application.

## Machine Learning in FoodFolio: K-Means Clustering
In FoodFolio, machine learning is utilized to enhance the personalization of recipe recommendations, suggesting recipes that align with users' dietary preferences and nutritional goals. This is acheieved by grouping similar recipes into clusters based on their nutrional content.

### K-Means Implementation

#### Data Preparation
This step involved preparing the dataset, which included nutritional content such as calories, protein, carbohydrates, and fats for many recipes. This data was cleaned and normalized to ensure effective learning and accurate clustering.

#### Feature Engineering
The data includes several calculated features such as total calories, ratios of macronutrients to total calories, and a health index based on these ratios. These features help to support the functionality of the K-Means algorithm to better understand the dietary profile of each recipe, resulting in more effective clusters.

#### Model Training
The K-Means clustering algorithm is applied to the processed data. The algorithm partitions the recipes into k distinct clusters where each recipe belongs to the cluster with the nearest mean nutrional value. This clustering is based on how similar their nutrional content is, which is calcualted using Euclidean distance between feature vectors.

#### Model Utilization
FoodFolio uses the clustered recipes to make recommendations. So when a user inputs their dietary preferences, the system idenfiies which cluster best matches the user's preferences and suggests recipes from that cluster.

## Discussion/Conclusion
FoodFolio successfully provides a user-friendly platform to give users recipe recommendations that take into consideration their personal goals and the nutritional value of the recipes, thus allowing them to better manage their diets.
Limitation: Database did not contain recipe instructions.
Some future enhancements might include user authentication, AI-driven personalized nutrition plans and expanded recipe databases to cover more types of cuisine.

## References
- https://www.kaggle.com/datasets/thedevastator/healthy-diet-recipes-a-comprehensive-dataset/data?select=All_Diets.csv