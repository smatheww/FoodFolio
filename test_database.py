import pytest
import sqlite3

@pytest.fixture
def conn():
    """Fixture to provide a database connection."""
    connection = sqlite3.connect('C:/Users/mathe/Projects/CMPSC445/FinalProject/foodfolio.db')
    connection.row_factory = sqlite3.Row  # Allows using column names as indices
    yield connection
    connection.close()

def test_select_query(conn):
    """Test to fetch some recipes and check the result is not empty."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes LIMIT 5;")
    results = cursor.fetchall()
    assert len(results) > 0, "No recipes found"
    cursor.close()

def test_high_protein_low_carb_recipes(conn):
    """Test fetching high protein, low carb recipes."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE highProtein = 1 AND lowCarb = 1 LIMIT 5;")
    results = cursor.fetchall()
    assert len(results) > 0, "No high protein, low carb recipes found"
    cursor.close()

def test_update_health_index(conn):
    """Test updating a recipe's health index and verify the update."""
    cursor = conn.cursor()
    cursor.execute("UPDATE recipes SET healthIndex = 0.95 WHERE id = 1;")
    conn.commit()
    cursor.execute("SELECT id, healthIndex FROM recipes WHERE id = 1;")
    result = cursor.fetchone()
    assert result['healthIndex'] == 0.95, "Health index was not updated correctly"
    cursor.close()
