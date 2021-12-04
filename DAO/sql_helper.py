import pymysql
import os


class sql_helper:
    """
    This class contains the necessary supporting funtions to perform SQL related operations.
    """

    def __init__(self):
        """
        Default constructor for class sql_helper
        """
        self.connection_obj = None

    def connect_database(self):
        """
        This function connects to the database on AWS, and authenticates the user.
        """
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
        """
        This function closes the database connection once done with it.
        """
        try:
            self.connection_obj.close()
        except:
            pass
            # Need to import error handling class

    def run_query(self, query):
        """
        Runs the specified query through the database and returns the output.

        Args:
            query (string): [Requires a valid SQL query passed as an argument.]

        Returns:
            [Tuple(Tuple..)]: [The output of the query being executed on the database is returned in the form of nested tuples.]
        """
        self.connect_database()
        tempCursor = self.connection_obj.cursor()
        tempCursor.execute(query)
        output = tempCursor.fetchall()
        self.disconnect_database()
        return output
