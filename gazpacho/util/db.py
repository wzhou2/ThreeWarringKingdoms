# import sqlalchemy as db #waiting for permission to use
import sqlite3
class Database:
    """A class to faciliate database read/write.
    """

    def __init__(self, file):
        self.DB_FILE = file
        self.conn = sqlite3.connect(file)
        self.conn.close()

    def openDB(func):
        """A wrapper function which opens the database for read/write

        Args:
            func (obj): A function that performs an operation on the database

        Returns:
            obj: A function object
        """
        def inner(self, *args):
            with sqlite3.connect(self.DB_FILE) as db:
                return func(self, db, *args)
        return inner

    @openDB
    def createTable(self, db, name, *cols):
        """ Create a x column table with the name provided given it
        does not exist yet.

        Args:
            name (str): The name of the table
            *cols : A variable length of columns

        Returns:
            bool: True if successful, False otherwise

        Note:
            - col (tuple)
            - SyntaxError: Column names can not be use with create table
                "CREATE TABLE users (?,?,?,?)", (user, password, first, last)
        """
        # print(cols, len(cols))

        c = db.cursor()
        command = "CREATE TABLE users"
        colName = str(cols)
        c.execute(command + colName)
        db.commit()

        return True

    @openDB
    def tableInDB(self, name):
        """ Checks if a table exists in the database

        Args:
            name (str): The name of the table

        Returns:
            bool: True if successful, False otherwise

        """
        pass

    @openDB
    def insert(self, name, values):
        """ Inserts a row with the given values into a table with the
        corresponding name.

        Args:
            name (str): The name of the table
            values (array): Values to be inserted into the table

        Returns:
            bool: True if successful, False otherwise

        Raises:
            ValueError: The values param does not contain enough element to fill
            the row.
        """
        pass

    @openDB
    def get(self, name, *cols):
        """ Gets values for the columns in cols that satisfy the the conditions
        from the a table

        Args:
            name (str): The name of the table
            *cols: The list of column names
            **conditions: A dictionary of conditions. The key is the column name
            and the value is the logic condition

        Returns:
            list : a list of table rows that satisfy the conditiions

        """
        pass

    def verifyUser(self, user, password):
        """ Verifies that the user is
        1. in the database and
        2. the user's inputted password matches the one in the database

        Args:
            user (str): The name of the user
            password (str): The inputted password of the user

        Return:
            bool: True if successful, False otherwise

        """
        pass

    def insertUser(self, **info):
        """ Adds a row entry into the table of users

        Args:
            **info : Dictionary of user inputted information

        Returns:
            bool: True if successful, False otherwise
        """
        pass

if __name__=="__main__":
    data = Database("test.db")
    args = ['cow', 'dog', 'peep', 'last']
    args = ["user TEXT", "first TEXT", "last TEXT", "password TEXT"]
    a = data.createTable("users", *args)
    print(a)
