import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(db_file):
    """Create a database connection to the specified SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established. SQLite version:", sqlite3.sqlite_version)
    except Error as e:
        print("Error connecting to database:", e)
    return conn

def create_table_from_csv(conn, csv_file):
    """Create a table in the SQLite database from a CSV file and insert data."""
    try:
        df = pd.read_csv(csv_file)
        df['id'] = range(1, len(df) + 1)  # Create an 'id' column if not already present
        # Define the dtype mapping based on your specific data needs.
        dtype_mapping = {
            'id': 'INTEGER PRIMARY KEY',
            'recipeName': 'TEXT',
            'protein': 'REAL',
            'carbs': 'REAL',
            'fat': 'REAL',
            'totalCalories': 'REAL',
            'proteinRatio': 'REAL',
            'carbRatio': 'REAL',
            'fatRatio': 'REAL',
            'healthIndex': 'REAL',
            'highProtein': 'INTEGER',
            'lowCarb': 'INTEGER',
            'lowFat': 'INTEGER',
            # Add other columns with specific types if necessary
        }
        df.to_sql('recipes', conn, if_exists='replace', index=False, dtype=dtype_mapping)
        print("Table created from CSV successfully and data inserted.")
    except Error as e:
        print("Error creating table from CSV:", e)
    except FileNotFoundError:
        print("CSV file not found:", csv_file)
    except Exception as e:
        print("An error occurred:", e)

def main():
    database = "foodfolio.db"
    csv_file = "processedDiet.csv"

    # Create a database connection
    conn = create_connection(database)

    if conn is not None:
        # Create table and insert data from CSV
        create_table_from_csv(conn, csv_file)
        
        # Close the connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
