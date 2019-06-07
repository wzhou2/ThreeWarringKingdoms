import sqlite3
from util.constants import *
from util.timestamp import *


'''
RECORD: DEPRECIATED
    Types:
        - project commit logs
            - project creation
        - salary change
        - issues
        - add/remove member
        - changing schedule
'''


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
            print("table exists already")
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
        values = ",".join( [ "=".join([x, "'" + str(updates[x]) + "'"]) for x in updates] )
        command = "UPDATE {} SET {} WHERE {}='{}'".format(table, values, USER, user)
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
        in_User = self.get(USER_TABLE, "count({})".format(USER), a = "WHERE {} = '{}'".format(USER, user))[0][0]
        in_Schedule = self.get(SCHEDULES_TABLE, "count({})".format(USER), a = "WHERE {} = '{}'".format(USER, user))[0][0]

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
        contain = self.get(USER_TABLE, "count({})".format(USER), a = "WHERE {} = '{}'".format(USER, user), b = "AND password = '{}'".format(password))[0][0]

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
            print('user exists already')
            return False

        values = [ info[USER], info[FIRST], info[LAST], info[PASSWORD], 0, info[POSITION] ]
        timeTable = [ info[USER], '', '', '', '', '', '', '']

        a = self.insert(USER_TABLE, values)
        b = self.insert(SCHEDULES_TABLE, timeTable)
        c = a and b

        # print(a, b, c)
        return c

    def updateUser(self, user, info):
        """ Updates info for specified user, cannot update username
        Args:
            user (str): username
            info : Dictionary of user inputted information
        Returns:
            bool: True if successful, False otherwise
        """
        return self.update(user, 'users', info)


    def getAllEmployees(self):
        """ get all users with 'employee' position sorted by lastname

        Returns:
            dict: dictionary of user info
                {
                    personal: [USER, FIRST, LAST, SALARY or None]
                    schedule: [MONDAY, TUESDAY, ... , SUNDAY]
                }
        """
        employees = self.get(USER_TABLE, "{}, {}, {}, {}".format(USER, FIRST, LAST, SALARY),
                a = "WHERE position='Employee'")

        schedules = []
        if len(employees) != 0:
            # print(employees)
            conditions = ["username = '{}'".format(i[0]) for i in employees]
            conditions = "WHERE " + " OR ".join(conditions)
            # print(conditions)
            schedules = self.get(SCHEDULES_TABLE, "*", a = conditions)

        diction = {
                "personal": employees,
                "schedule": schedules
                }
        return diction

    def getPosition(self, user):
        """ Returns the position of the user

        Args:
            user (str): name of the user

        Returns:
            str : position of the user
        """

        return self.get(USER_TABLE, POSITION, a = "WHERE {} = '{}'".format(USER, user))[0][0]

    def getUser(self, user):
        """ Gets profile info of user

        Args:
            user (str): the name of the user

        Returns:
            dict: dictionary of user info
                {
                    personal: [USER, FIRST, LAST, SALARY or None]
                    schedule: [MONDAY, TUESDAY, ... , SUNDAY]
                }
        """
        order = [USER, FIRST, LAST, SALARY]
        info = self.get(USER_TABLE, *order, a = "WHERE {} = '{}'".format(USER, user))[0]
        schedule = self.getSchedule(user)
        profile = {
            "personal" : dict(zip(order, info)),
            "schedule" : schedule
        }
        # print(type(info), info)
        # print(type(schedule), schedule)
        # print(profile)
        return profile

    def updateSchedule(self, user, updates):
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
            dict: the schedule
                ex. "monday": "9:30 - 16:00"
            None: if the user does not have an assign schedule as of right now
        """
        order = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]
        schedule = self.get(SCHEDULES_TABLE, *order, a = "WHERE {} = '{}'".format(USER, user))[0]
        # print(schedule)
        if "".join(schedule) == "":
            return None
        return dict(zip(order, schedule))

    def checkProject(self, project_name):
        """Checks if the project is in the the database

        Args:
            project (str): The name of the user

        Return:
            bool : True if user exists in database, False otherwise
        """
        contain = self.get("projects", "count(name)", a = "WHERE name = '{}'".format(project_name))[0][0]

        return contain != 0

    def createProject(self, project_name, creator, description):
        """ Adds a project into the table projects

        Args:
            project_name (str): The name of the project
            description (str): description of the project
            creator (str): The user who is creating the project

        Returns:
            bool: True if successful, False otherwise
        """
        if self.checkProject(project_name):
            print("project already exists")
            return False

        values = [project_name, creator, '', description]
        if self.insert(PROJECTS_TABLE, values) != True:
            print('insert project fail')
            return False

        # project_id = self.get("projects", "rowid", a = "WHERE name='{}'".format(project_name))[0][0]
        # if self.createRecord(creator, record_info, project_id) != True:
        #     print('insert record fail')
        #     return False

        # return self.insert('projects', values)
        return True

    # def createRecord(self, creator, info, project_id):
    #     """ inserts row in record table corresponding to a project
    #     Args:
    #         creator (str): name of creator
    #         info (dict): dict of info to be inserted
    #     Returns:
    #         bool: True if successful
    #     """
    #     # [target, initated_by, type, description, id, timeStamp, message, view_level]
    #     time = createTimestamp()
    #     values = [info['target'], creator, info['type'], info['description'], project_id, time, info['message'], info['view_level']]
    #     return self.insert('record', values)

    # def getRecord(self, conditions):
    #     """ gets records by defined conditions
    #     Args:
    #         conditions (dict): Dict of key:value pairs
    #         ex: { 'type': 'message' } gets all messages
    #     Returns:
    #         list of records
    #     """
    #     # print(conditions)
    #     conds = " AND ".join([ "{}='{}'".format( i, conditions[i] ) for i in conditions])
    #     # conds = ' AND '.join( [ i + "'{}'".format( conditions[i] ) for i in conditions] )
    #     # print(conds)
    #     recs = self.get("record", "*", a = "WHERE {}".format(conds))

    #     return recs
    # def createRecord(self, creator, info, project_id):
    #     """ inserts row in record table corresponding to a project
    #     Args:
    #         creator (str): name of creator
    #         info (dict): dict of info to be inserted
    #     Returns:
    #         bool: True if successful
    #     """
    #     # [target, initated_by, type, description, id, timeStamp, message, view_level]
    #     time = createTimestamp()
    #     print(info)
    #     values = [info['target'], creator, info['type'], info['description'], project_id, time, info['message'], info['view_level']]
    #     return self.insert('record', values)

    # def getRecord(self, conditions):
    #     """ gets records by defined conditions
    #     Args:
    #         conditions (dict): Dict of key:value pairs
    #         ex: { 'type': 'message' } gets all messages
    #     Returns:
    #         list of records
    #     """
    #     # print(conditions)
    #     conds = " AND ".join([ "{}='{}'".format( i, conditions[i] ) for i in conditions])
    #     # conds = ' AND '.join( [ i + "'{}'".format( conditions[i] ) for i in conditions] )
    #     # print(conds)
    #     recs = self.get("record", "*", a = "WHERE {}".format(conds))

    #     return recs


    def getAllProjects(self):
        """ Get list of project names

        Returns:
            list: list of project names
        """
        return self.get(PROJECTS_TABLE, PROJECT_NAME)

    def getProjects(self, user):
        """ Gets all projects a user is part of

        Args:
            user (str): The name of the user

        Returns:
            list: list of projects
        """
        user_projects = []
        project_list = self.get(PROJECTS_TABLE, "*")
        for project in project_list:
            userlist = project[2].split(',')
            if project[1] == user or user in userlist:
                u_p = {}
                u_p['name'] = project[0]
                u_p['creator'] = project[1]
                u_p['members'] = project[2]
                u_p['description'] = project[3]
                user_projects.append(u_p)

        return user_projects

    @openDB
    def addMembers(self, db, project, *users):
        """ Adds new users to the project
        Args:
            project (str): the name of the project
            *user : a variable number of new users to add to projects
        Returns:
            bool: True if successful, False otherwise
        """
        if self.checkProject(project) == False:
            return False
        old_users = self.get("projects", "*", a = "WHERE name = '{}'".format(project))[0][2]
        new_users = ','.join(users)
        if old_users !='':
            u = old_users + ',' + new_users
        else:
            u = new_users
        userlist = ','.join(list(set(u.split(','))))
        # print(userlist)
        cmd = "UPDATE {} SET members='{}' WHERE name='{}'".format('projects', userlist, project)
        c = db.cursor()
        try:
            c.execute(cmd)
            return True
        except:
            print("add members failed")
            return False

    @openDB
    def removeMembers(self, db, project, *users):
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
        userlist = self.get("projects", "*", a = "WHERE name = '{}'".format(project))[0][2]
        userlist = userlist.split(',')
        for u in users:
            try:
                userlist.remove(u)
            except:
                print('user not found')
        userlist = ','.join(userlist)
        cmd = "UPDATE {} SET members='{}' WHERE name='{}'".format('projects', userlist, project)
        c = db.cursor()
        try:
            c.execute(cmd)
            return True
        except:
            print("remove members failed")
            return False

#Timeline
#    - Add event
#    - Delete event
#    - get all events

    def createEvent(self, info):
        """Create event in timeline
        Args: 
            info (dict): keys: { username, title, description }
        Return:
            bool: true if successful
        """
        time = createTimestamp()
        info_array = [info[USER], time, info['title'], info['description']]
        return self.insert(TIMELINE_TABLE, info_array)

    @openDB
    def deleteEvent(self, db, rowid):
        """Deletes event in timeline
        Args: 
            rowid: row id of event in timeline table in db
        Return:
            bool: true if successful
        """
        cmd = "DELETE FROM {} WHERE rowid={}".format(TIMELINE_TABLE, rowid)
        c = db.cursor()
        try:
            c.execute(cmd)
            return True
        except:
            print('delete event failed')
            return False

    def getAllEvents(self):
        """Gets all events for rendering timeline
        Return:
            array of event dictionaries (sorted by time)
                dict:
                {
                username (str): usr of creator,
                timestamp (float): time of creation,
                title (str): title of event,
                description (str): body text,
                rowid (int): used for deleting event
                }
        """
        events = self.get(TIMELINE_TABLE, "*, rowid")
        events.sort(key = lambda tup: tup[1])

        keys = ['username', 'timestamp', 'title', 'description', 'rowid']
        for e in range(len(events)):
            di = { keys[i]:events[e][i] for i in range(5) }
            events[e] = di

        return events

    def getInbox( self, user ):
        """ Get a user's inbox
        Args:
            user: username
        Return: Dict: {sent_by, topic, context, timestamp}
        """
        inbox = self.get(MESSAGE_TABLE, "*, rowid", a = "WHERE sent_to='{}'".format(user))
        return inbox

    def send( self, user, sent_to, topic, content ):
        ''' Send msg to multiple users
        Args:
            user (str): username of sender
            sent_to (str): receiver
            topic (str): title of msg
            content (str): text of msg
        return:
            True if success
        '''
        time = createTimestamp()
        values = [sent_to, user, topic, content, time]
        print(values)
        try:
            self.insert(MESSAGE_TABLE, values)
            print("succeed send")
            return True
        except:
            print("fail send")
            return False

    def reply(self, rowid, topic, content):
        ''' send message in reply
        Args:
           rowid (int): rowid of msg given by getInbox 
        return:
            true if successful
        '''
        parent_msg = self.get(MESSAGE_TABLE, "*", a = "WHERE rowid={}".format(rowid))[0]
        print(parent_msg)
        time = createTimestamp()
        values = [ parent_msg[1], parent_msg[0], topic, content, time ]
        try:
            self.insert(MESSAGE_TABLE, values)
            print("succeed reply")
            return True
        except:
            print("fail reply")
            return False


    @openDB
    def delete(self, db, rowid ):
        ''' delete a message in inbox
        Args:
           rowid (int): rowid of msg given by getInbox 
        return:
            true if successful
        '''
        cmd = "DELETE FROM {} WHERE rowid={}".format(MESSAGE_TABLE, rowid)
        c = db.cursor()
        try:
            c.execute(cmd)
            return True
        except:
            print('delete failed')
            return False

