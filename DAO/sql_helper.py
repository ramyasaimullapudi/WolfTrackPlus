import pymysql
import os


class sql_helper:
    def __init__(self):
        self.connection_obj = None

    def connect_database(self):
        try:
            self.connection_obj = pymysql.connect(
                host="wolftrackdb.cqxwgddfgicy.us-east-1.rds.amazonaws.com",
                port=3306,
                user="WolfaTrack",
                password="n1rjbhPukoiFDtYV7sjJ",
                db="wolftrack",
                autocommit=True,
            )
        except:
            pass
            # Need to import error handling class

    def disconnect_database(self):
        try:
            self.connection_obj.close()
        except:
            pass
            # Need to import error handling class

    def run_query(self, query):
        self.connect_database()
        tempCursor = self.connection_obj.cursor()
        tempCursor.execute(query)
        output = tempCursor.fetchall()
        self.disconnect_database()
        return output
