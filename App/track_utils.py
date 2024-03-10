# Load Database Pkg
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Create a MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='data'
)

c = conn.cursor()

# Fxn for page tracking
def create_page_visited_table():
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS pageTrackTable (
                pagename VARCHAR(255),
                timeOfvisit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    except Error as e:
        print(f"Error: {e}")

def add_page_visited_details(pagename, timeOfvisit):
    try:
        c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES(%s, %s)', (pagename, timeOfvisit))
        conn.commit()
    except Error as e:
        print(f"Error: {e}")

def view_all_page_visited_details():
    try:
        c.execute('SELECT * FROM pageTrackTable')
        data = c.fetchall()
        return data
    except Error as e:
        print(f"Error: {e}")

# Fxn for emotion classification tracking
def create_emotionclf_table():
    try:
        c.execute('''
            CREATE TABLE IF NOT EXISTS emotionclfTable (
                rawtext TEXT,
                prediction TEXT,
                probability FLOAT,
                timeOfvisit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    except Error as e:
        print(f"Error: {e}")

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    try:
        c.execute('''
            INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit)
            VALUES(%s, %s, %s, %s)
        ''', (rawtext, prediction, probability, timeOfvisit))
        conn.commit()
    except Error as e:
        print(f"Error: {e}")

def view_all_prediction_details():
    try:
        c.execute('SELECT * FROM emotionclfTable')
        data = c.fetchall()
        return data
    except Error as e:
        print(f"Error: {e}")
