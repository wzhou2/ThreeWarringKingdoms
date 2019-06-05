# DATABASE SCHEMA
USER_TABLE = "users"
PROJECTS_TABLE = "projects"
SCHEDULES_TABLE = "schedules"
RECORD_TABLE = "record"

TABLES = {
    USER_TABLE: ['username TEXT PRIMARY KEY', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'position TEXT'],
    PROJECTS_TABLE: [ 'name TEXT PRIMARY KEY', 'creator TEXT', 'members TEXT'],
    SCHEDULES_TABLE: ['username TEXT PRIMARY KEY', 'monday TEXT', 'tuesday TEXT', 'wednesday TEXT', 'thursday TEXT', 'friday TEXT', 'saturday TEXT', 'sunday TEXT'],
    RECORD_TABLE: ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER']
}

# CONSTANTS
USER = "username"
FIRST = "first"
LAST = "last"
PASSWORD = "password"
SALARY = "salary"
POSITION = "position"

ALL = "*"
MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"
SATURDAY = "saturday"
SUNDAY = "sunday"

PROJECT_NAME = "name"
# ACCESS LEVEL (0 is the highest access level)
ACCESS = {
    'Admin': 0,
    'Employee': 1
}


if __name__ == "__main__":
    print(TABLES)
