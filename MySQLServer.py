import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host='localhost',      # Change if your MySQL host is different
            user='root',           # Replace with your MySQL username
            password=''            # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional message on closing
            # print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
