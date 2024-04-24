from flask import Flask, render_template, request, jsonify, abort
from flask_cors import CORS
import sqlite3
import joblib
import pandas as pd

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for all domains on all routes. Adjust as necessary for production environments.

# Load the k-means model and scaler
model = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

def get_db_connection():
    """Create and return a connection to the database."""
    conn = sqlite3.connect('foodfolio.db')
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access to columns
    return conn

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML file

@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Endpoint to retrieve all recipes."""
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
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
    return jsonify({'message': 'Logged in successfully'})

@app.route('/recommend', methods=['GET'])
def recommend():
    """Endpoint to make recommendations based on the k-means model."""
    desired_cluster = int(request.args.get('cluster', 0))
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()

    recipes_df = pd.DataFrame([dict(recipe) for recipe in recipes])
    features = ['protein_standardized', 'carbs_standardized', 'fat_standardized']  # Update to use the standardized columns
    scaled_features = scaler.transform(recipes_df[features])

    predictions = model.predict(scaled_features)
    recommended_recipes = recipes_df[predictions == desired_cluster].to_dict(orient='records')

    return jsonify(recommended_recipes)

@app.route('/api/recipes', methods=['GET'])
def search_recipes():
    search_query = request.args.get('search', '')
    conn = get_db_connection()
    query = f"SELECT * FROM recipes WHERE recipeName LIKE '%{search_query}%'"
    recipes = conn.execute(query).fetchall()
    conn.close()
    return jsonify([dict(recipe) for recipe in recipes])

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({'error': 'Not found', 'message': error.description}), 404

@app.errorhandler(400)
def bad_request(error):
    """Custom error handler for 400 errors."""
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
