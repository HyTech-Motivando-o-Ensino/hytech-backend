import mysql.connector
from mysql.connector import errorcode
import os
from pathlib import Path
from dotenv import load_dotenv


class ConnectDB():
    def __init__(self):
        # Configurando dotenv.
        # self.env_path = '/home/jeremias/Documents/cesar/code/hytech-backend/.env'
        self.env_path = Path('modules/..')/'.env'
        load_dotenv(dotenv_path=self.env_path)
        self.host = os.getenv("DATABASE_HOST")
        self.user = os.getenv("DATABASE_USER")
        self.password = os.getenv("DATABASE_PASSWORD")
        self.database = os.getenv("DATABASE_NAME")
    
    def connect(self):
        try:
            # print(self.host)
            # print(self.user)
            # print(self.password)
            # print(self.database)
            db_connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            print("Database connection made!")
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)
        else:
            db_connection.close()