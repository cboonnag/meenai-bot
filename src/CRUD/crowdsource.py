import mysql.connector 
import json 
from CRUD.connector import db_connect


def insertData(TimeStamp, UserId, MsgType, Col1, Col2 = "NONE", Col3 = "NONE"):

    query = ( "INSERT INTO cleanroom"  
    "(submit_time, user_id, message_type, col1, col2, col3)" 
    "VALUES (%s,%s,%s,%s,%s,%s)" )
    val = (TimeStamp, UserId, MsgType, Col1, Col2, Col3)
    
    mydb = db_connect()
    mycursor = mydb.cursor()
    mycursor.execute("set time_zone = '+7:00'")
    mycursor.execute(query, val)
    mydb.commit()