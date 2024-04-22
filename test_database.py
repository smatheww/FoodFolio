import sqlite3

def create_connection(db_file):
    """Create a database connection to the specified SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established to SQLite database")
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
    return conn

def test_query(conn, query):
    """Execute a SQL query and print the results."""
    cur = conn.cursor()
    try:
        cur.execute(query)
        if query.lower().startswith('select'):
            results = cur.fetchall()
            print(f"Results for query: {query}")
            for result in results:
                print(result)
        else:
            conn.commit()  # Commit to save changes for update or delete operations
            print(f"Operation successful for query: {query}")
    except sqlite3.Error as e:
        print(f"An error occurred executing query: {query}, error: {e}")
    finally:
        cur.close()

'''def check_schema(conn):
    cur = conn.cursor()
    cur.execute("PRAGMA table_info(recipes);")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()

def print_table_schema(conn, table_name):
    """Prints the schema of the specified table."""
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table_name});")
    columns = cur.fetchall()
    print(f"Schema for {table_name}:")
    for col in columns:
        print(col)
    cur.close()'''


def run_tests():
    database = "foodfolio.db"
    conn = create_connection(database)
    
    if conn is not None:
       # print_table_schema(conn, 'recipes')  # Check and print the table schema
        # Test fetching all recipes with limit
        test_query(conn, "SELECT * FROM recipes LIMIT 5;")

        # Test fetching high protein, low carb recipes
        test_query(conn, "SELECT * FROM recipes WHERE highProtein = 1 AND lowCarb = 1 LIMIT 5;")

        # Test updating a recipe's health index
        test_query(conn, "UPDATE recipes SET healthIndex = 0.95 WHERE id = 1;")

        # Test fetching to verify update
        test_query(conn, "SELECT id, healthIndex FROM recipes WHERE id = 1;")

        # Clean up or more tests can be added here
        
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    run_tests()
