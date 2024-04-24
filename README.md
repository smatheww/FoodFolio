# FoodFolio: Discover Healthy Recipes

FoodFolio is a web application dedicated to helping users discover and create healthy recipes that cater to various dietary needs, including keto, paleo, and gluten-free options.

## Installation

To set up the FoodFolio application on your local machine, follow these instructions:

### Prerequisites

- Python 3.6 or higher - [Download Python](https://www.python.org/downloads/)
- pip (Python package manager) - typically installed with Python
- Git - [Download Git](https://git-scm.com/downloads)

### Step 1: Clone the Repository

In your bash terminal, enter the following commands to clone the FoodFolio repository from GitHub:

git clone https://github.com/smatheww/FoodFolio.git
cd FoodFolio

### Step 2: Install Dependencies

Install the required packages by running:

pip install -r requirements.txt

If the above command fails, try installing the packages individually.For example: 

pip install flask

### Step 3:  Data preprocessing Script

To preprocess the data, which prepares it for clustering, run:

python datapr.py

### Step 4:  Run the K-Means Clustering Script

To classify recipes based on their nutritional content, execute:

python kmeans.py

### Step 5:  Initialize the Database

Set up your database by running:

python database.py

This script initializes the database with the necessary tables and seeds it with initial data.

### Step 6:  Start the Flask Application

Finally, start the Flask web server with:

python flaskapp.py

The application should now be running on http://localhost:5000.

## Usage

Open a web browser and navigate to http://localhost:5000 to start exploring healthy recipes. Use the 'Recipes' tab to search for recipes based on your dietary preferences.