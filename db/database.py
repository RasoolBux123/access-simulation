
# db/database.py
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def get_db_connection():
    """
    Creates and returns a MySQL database connection.
    Returns None if connection fails.
    """
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None



#import mysql.connector

#def get_db_connection():
#    conn = mysql.connector.connect(
#        host="localhost",
#        user="root",
#        password="123456",  
#        database="access_simulation"
#    )
#    return conn
