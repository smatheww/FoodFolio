from flask import Flask, request, jsonify, abort
import sqlite3
import joblib
import pandas as pd

app = Flask(__name__)

# Load the k-means model and scaler
model = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

def get_db_connection():
    """Create and return a connection to the database."""
    conn = sqlite3.connect('foodfolio.db')
    conn.row_factory = sqlite3.Row  # Allows dictionary-like access to columns
    return conn

@app.route('/')
def index():
    return "Welcome to the FoodFolio API!"

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Endpoint to retrieve all recipes."""
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
    # Convert rows into a list of dicts before returning as JSON
    return jsonify([dict(recipe) for recipe in recipes])

@app.route('/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """Endpoint to retrieve a specific recipe by its ID."""
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    conn.close()
    if recipe is None:
        abort(404, description="Resource not found")
    return jsonify(dict(recipe))

@app.route('/login', methods=['POST'])
def login():
    """Simulated login endpoint."""
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        abort(400, description="Username and password are required")
    # Here you would add authentication against user details in the database.
    return jsonify({'message': 'Logged in successfully'})

@app.route('/recommend', methods=['GET'])
def recommend():
    """Endpoint to make recommendations based on the k-means model."""
    desired_cluster = int(request.args.get('cluster', 0))
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()

    # Prepare data for prediction, ensuring it matches the training set's feature order and scaling
    recipes_df = pd.DataFrame([dict(recipe) for recipe in recipes])
    features = ['protein', 'carbs', 'fat', 'totalCalories']
    scaled_features = scaler.transform(recipes_df[features])  # Apply scaling as done during training

    predictions = model.predict(scaled_features)  # Make predictions with the scaled features
    recommended_recipes = recipes_df[predictions == desired_cluster].to_dict(orient='records')

    return jsonify(recommended_recipes)

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({'error': 'Not found', 'message': error.description}), 404

@app.errorhandler(400)
def bad_request(error):
    """Custom error handler for 400 errors."""
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

if __name__ == '__main__':
    app.run(debug=True)
