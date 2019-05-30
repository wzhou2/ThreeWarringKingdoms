# DATABASE SCHEMA
USER_TABLE = "users"
PROJECTS_TABLE = "projects"
SCHEDULES_TABLE = "schedules"
RECORD_TABLE = "record"

TABLES = {
    USER_TABLE: ['user TEXT PRIMARY KEY', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'position TEXT'],
    PROJECTS_TABLE: [ 'name TEXT PRIMARY KEY', 'creator TEXT', 'members TEXT'],
    SCHEDULES_TABLE: ['user TEXT PRIMARY KEY', 'monday TEXT', 'tuesday TEXT', 'wednesday TEXT', 'thursday TEXT', 'friday TEXT', 'saturday TEXT', 'sunday TEXT'],
    RECORD_TABLE: ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER']
}

# CONSTANTS
USER = "username"
FIRST = "first"
LAST = "last"
PASSWORD = "password"
SALARY = "salary"
POSITION = "position"

if __name__ == "__main__":
    print(TABLES)
