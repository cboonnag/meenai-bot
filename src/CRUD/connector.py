import mysql.connector 
from config import * 

def db_connect():
    print("db_connect")
    config = {
            'user': USERNAME,
            'database': DATABASE_NAME,
            'password': PASSWORD,
            'host': HOST,
            'port': PORT
        }

    mydb = mysql.connector.connect(**config)

    return mydb