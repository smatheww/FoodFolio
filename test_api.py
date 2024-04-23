import requests
import pytest
import sqlite3



# The base URL for your API
BASE_URL = "http://localhost:5000"

@pytest.fixture
def conn():
    """Provide a database connection to use for testing."""
    connection = sqlite3.connect('C:/Users/mathe/Projects/CMPSC445/FinalProject/foodfolio.db')
    yield connection  # provide the fixture value
    connection.close()  # cleanup after the test runs

def test_get_all_recipes():
    """Test fetching all recipes."""
    response = requests.get(f"{BASE_URL}/recipes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Assuming the response should be a list

def test_get_recipe():
    """Test fetching a specific recipe by ID."""
    response = requests.get(f"{BASE_URL}/recipe/1")  # Assumes there's at least one recipe with ID 1
    assert response.status_code == 200
    assert 'recipeName' in response.json()  # Assumes JSON response contains 'name'

def test_search_recipes():
    """Test the search functionality."""
    response = requests.get(f"{BASE_URL}/api/recipes", params={'search': 'chicken'})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_recommend():
    """Test the recommendation endpoint."""
    response = requests.get(f"{BASE_URL}/recommend", params={'cluster': 0})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_login():
    """Test user login."""
    credentials = {'username': 'testuser', 'password': 'testpass'}
    response = requests.post(f"{BASE_URL}/login", json=credentials)
    assert response.status_code == 200
    assert response.json().get('message') == 'Logged in successfully'
