# DATABASE SCHEMA
USER_TABLE = "users"
PROJECTS_TABLE = "projects"
SCHEDULES_TABLE = "schedules"
RECORD_TABLE = "record"
MESSAGE_TABLE = "messages"
TIMELINE_TABLE = "timeline"

TABLES = {
    USER_TABLE: ['username TEXT PRIMARY KEY', 'first TEXT', 'last TEXT', 'password TEXT', 'salary INTEGER', 'position TEXT'],
    PROJECTS_TABLE: [ 'name TEXT PRIMARY KEY', 'creator TEXT', 'members TEXT', "description TEXT"],
    SCHEDULES_TABLE: ['username TEXT PRIMARY KEY', 'monday TEXT', 'tuesday TEXT', 'wednesday TEXT', 'thursday TEXT', 'friday TEXT', 'saturday TEXT', 'sunday TEXT'],
    # RECORD_TABLE: ['target TEXT', 'initated_by TEXT', 'type TEXT', 'description TEXT', 'id INTEGER', 'timeStamp INTEGER', 'message TEXT', 'view_level INTEGER'],
    # RECORD_TABLE: ["username TEXT", "project TEXT", "type TEXT", "timestamp INTEGER", "description TEXT"],
    MESSAGE_TABLE: ['sent_to TEXT', 'sent_by TEXT', 'topic TEXT', 'content TEXT', 'timestamp INTEGER' ],
    TIMELINE_TABLE: ['username TEXT', 'start_time INTEGER','end_time INTEGER', 'title TEXT', 'description TEXT']
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

# RECORD TYPES
# REC_PROJECT = "rec_project"
# REC_SALARY = "rec_salary"
# REC_ISSUE = "rec_issue"
# REC_ADD_MEMBER = "rec_add_member"
# REC_REMOVE_MEMBER = "rec_remove_member"
# REC_SCHEDULE_CHANGE = "rec_schedule_change"


PROJECT_NAME = "name"
# ACCESS LEVEL (0 is the highest access level)
ACCESS = {
    'Admin': 0,
    'Employee': 1
}


if __name__ == "__main__":
    print(TABLES)
