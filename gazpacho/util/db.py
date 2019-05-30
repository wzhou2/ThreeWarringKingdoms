import sqlite3
from util.constants import *

class Database:
    """A class to faciliate database read/write.
    """

    def __init__(self, f):
        self.DB_FILE = f
        self.conn = sqlite3.connect(f)
        self.conn.close()

    def openDB(func):
        """A wrapper function which opens the database for read/write

        Args:
            func (obj): A function that performs an operation on the database

        Returns:
            obj: A function object
        """
        def inner(self, *args, **kwargs):
            with sqlite3.connect(self.DB_FILE) as db:
                return func(self, db, *args, **kwargs)
        return inner

    @openDB
    def createTable(self, db, name, *cols):
        """ Create a x column table with the name provided given it
        does not exist yet.

        Args:
            name (str): The name of the table
            db (obj): The sqlite3 object for the database
            *cols : A variable length of columns

        Returns:
            bool: True if successful, False otherwise

        Note:
            - col (tuple)
            - SyntaxError: Column names can not be use with create table
                "CREATE TABLE users (?,?,?,?)", (user, password, first, last)
        """
        # print(cols, len(cols))
        if self.tableInDB(name):
            return False
        c = db.cursor()
        command = "CREATE TABLE " + name
        colName = "(" + ", ".join(cols) + ")"
        print(command + colName)
        c.execute(command + colName)

        return True

    @openDB
    def tableInDB(self, db, name):
        """ Checks if a table exists in the database

        Args:
            db (obj): The sqlite3 object for the database
            name (str): The name of the table

        Returns:
            bool: True(!0) if in db, False(0) otherwise

        """
        c = db.cursor()
        cmd = 'SELECT count(name) FROM sqlite_master WHERE type="table" AND name=?'
        contain = c.execute(cmd, (name,)).fetchone()[0]
        # print(contain)
        return contain != 0

    @openDB
    def insert(self, db, name, values):
        """ Inserts a row with the given values into a table with the
        corresponding name.

        Args:
            name (str): The name of the table
            values (array): Values to be inserted into the table

        Returns:
            bool: True if successful, False otherwise

        Raises:
            sqlite3.OperationalError: The values param does not contain enough element to fill
            the row.
        """
        c = db.cursor()
        command = "INSERT INTO " + name + " values" + "(" + ",".join(["?" for x in values]) + ")"

        # print(command)
        try:
            # print(command)
            c.execute(command, values)
        except (sqlite3.OperationalError):
            print("Sqlite3 insertion error check command")
            return False
        return True


    @openDB
    def get(self, db, name, *cols, **conditions):
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
        c = db.cursor()

        command = "SELECT {} from {}".format(",".join([x for x in cols]), name)
        # print(conditions)
        if conditions:
            conditionals = " ".join(conditions.values())
            # print(conditionals)
            command += " " + conditionals

        # print(command)
        c.execute(command)

        result = c.fetchall()
        # print(result)

        return result

    @openDB
    def update(self, db, user, table, updates):
        """ Updates select columns for a specified user. Update schedule or user info.

        Args:
            user (str): name of user
            table (str): table being updated
            updates (dict): dict of column name and new values

        Return:
            bool: True if update succeeds

        """
        values = ",".join( [ "=".join([x, "'" + updates[x] + "'"]) for x in updates] )
        print(values)
        command = "UPDATE {} SET {} WHERE user='{}'".format(table, values, user)
        print(command)
        c = db.cursor()
        try:
            c.execute(command)
            return True
        except:
            print('insert schedule error')
            return False

    def checkUser(self, user):
        """Checks if the user is in the the database

        Args:
            user (str): The name of the user

        Return:
            bool : True if user exists in database, False otherwise
        """
        in_User = self.get(USER_TABLE, "count(user)", a = "WHERE user = '{}'".format(user))[0][0]
        in_Schedule = self.get(SCHEDULES_TABLE, "count(user)", a = "WHERE user = '{}'".format(user))[0][0]

        return in_User + in_Schedule != 0

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
        contain = self.get("users", "count(user)", a = "WHERE user = '{}'".format(user), b = "AND password = '{}'".format(password))[0][0]

        return contain != 0

    def insertUser(self, info):
        """ Adds a row entry into the table of users and schedules

        Args:
            info : Dictionary of user inputted information

        Returns:
            bool: True if successful, False otherwise

        """
        print(info)
        if self.checkUser(info[USER]):
            return False

        values = [ info[USER], info[FIRST], info[LAST], info[PASSWORD], 0, info[POSITION] ]
        timeTable = [ info[USER], '', '', '', '', '', '', '']
        print("VALUES")
        print(values)

        a = self.insert("users", values)
        b = self.insert("schedules", timeTable)
        c = a and b

        # print(a, b, c)
        return c

    @openDB
    def updateSchedule(self, db, user, updates):
        """ Updates the hours for an user

        Args:
            user (str): The name of the user
            updates (dict): a dictionary of weekdays to update

        Returns:
            bool: True if successful, False otherwise

        Raises:
            - ValueError: if updates (dict) does not contain any
            valid keys
        Notes:
            - only the days of week are valid keys in updates (dict)
        """
        return self.update( user, 'schedules', updates )


    def getSchedule(self, user):
        """ Get the schedule of the user

        Args:
            user (str): The name of the user

        Returns:
            list: the schedule
        """
        # contain = self.get("users", "count(user)", a = "WHERE user = '{}'".format(user), b = "AND password = '{}'".format(password))[0][0]

        sch = self.get( 'schedules', '*', a = "WHERE user = '{}'".format(user))[0]
        return sch


    def checkProject(self, project_name):
        """Checks if the project is in the the database

        Args:
            project (str): The name of the user

        Return:
            bool : True if user exists in database, False otherwise
        """
        contain = self.get("projects", "count(name)", a = "WHERE name = '{}'".format(project_name))[0][0]

        return contain != 0

    def createProject(self, project, creator):
        """ Adds a project into the table projects

        Args:
            project (str): The name of the project
            creator (str): The user who is creating the project

        Returns:
            bool: True if successful, False otherwise
        """
        if self.checkProject(project):
            # already exist
            return False
        values = [project, creator, '']
        return self.insert('projects', values)

    def getProjects(self, user):
        """ Gets all projects a user is part of

        Args:
            user (str): The name of the user

        Returns:
            list: list of projects
        """
        projects = self.get("projects", "*", a = "WHERE name = '{}'".format(user))
        return projects

    def addMembers(self, project, *user):
        """ Adds new users to the project

        Args:
            project (str): the name of the project
            *user : a variable number of new users to add to projects

        Returns:
            bool: True if successful, False otherwise
        """

        p = self.get("projects", "*", a = "WHERE name = '{}'".format(project))[0]
        values = [project, p[1], users]

        return self.insert(project, values)

    def removeMembers(self, project, *user):
        """ Removes the users from the project

        Args:
            project (str): the name of the project
            *user : a variable number of users to remove from the project

        Returns:
            bool: True if successful, False otherwise

        Raises:
            - ValueError: if a user requested to be removed is not in
            the project
        """
        info = self.get("projects", "members", a = "WHERE name = '{}'".format(project))[0]
        userlist = info[2].split(',')
        for u in user:
            try:
                userlist.remove(u)
            except:
                print("user not in list")
        values = [project, info[1], userlist]
        return self.insert('projects', values)


    # RECORD TABLE METHODS
