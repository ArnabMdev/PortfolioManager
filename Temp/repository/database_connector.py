import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = os.getenv('USER'),
        password =os.getenv('PASSWORD'),
        database =os.getenv('DB_NAME')
    )
    return mydb
