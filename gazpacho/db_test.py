from util.db import *
from util.timestamp import *

# data = Database("../data/block.db")
# d = data.get("users", "*", "WHERE user='asd'")
# print(d)

data = Database("util/test.db")
# a = data.tableInDB('d')
# print(a)

''' functions tested:
createTable
tableInDB
insert 
'''
vals = ['eeeuserna', 'frist', 'lsat', 'pw']
args = ["user TEXT", "first TEXT", "last TEXT", "password TEXT", "salary INTEGER", "position TEXT"]
# b = data.createTable("test_user", *args)
# print(b)
# t = data.tableInDB("users")
# print(t)
# c = data.insert("test_user", vals)
# print(c)

'''
get
checkUser
insertUser
verifyuser
getUser
updateUser
'''
# d = data.get("users", "user", "password")
# print(d)
# e = data.checkUser("userna")
# f = data.checkUser("bleh")
# print(e, f)
di = {
    "username": "a0",
    "first": "dsa",
    "last": "earaelname1",
    "password": "pw1",
    "salary": 100,
    "position": "employee"
}
f = data.insertUser(di)
di = {
    "username": "a1",
    "first": "dsa",
    "last": "earaelname1",
    "password": "pw1",
    "salary": 100,
    "position": "employee"
}
f = data.insertUser(di)
# print(f)
# ver = data.verifyUser( 'test0', 'pw0' )
# print(ver)
# guser = data.getUser('test1')
# print(guser)
# upda = {
#         'first': 'u first',
#         'last': 'u last',
#         'password': 'pwpwpw',
#         'salary': 2334343,
#         'position': 'updated pos'
#         }
# up = data.updateUser('test0', upda)
# print(up)
# guser = data.getUser('test0')
# print(guser)

'''
updateSchedule
getSchedule
'''
# sch = {
#         'monday': 'a0',
#         'tuesday': 'a1',
#         'wednesday': 'a2',
#         'thursday': 'a3',
#         'friday': 'a4',
#         'saturday': 'a5',
#         'sunday': 'a6',
#         }
# s = data.updateSchedule( 'test1', sch )
# gets = data.getSchedule('test0')
# print(gets)
# a = data.getUser('test0')
# print(a)

'''
checkProject
createProject
getProjects
'''
info = {
    'target': 'target text',
    'type': 'type txt',
    'description': 'descr text',
    'message': 'msg text',
    'view_level': 900
        }
# a = data.checkProject('project0')
# print(a)
# proj = data.createProject('project0', 'test0', info)
# print(proj)
# print(data.checkProject('project0'))
# add = data.addMembers('project0', 'u1', 'u2')
# add = data.addMembers('project0', 'bob', 'steve')
# print(add)
# remove = data.removeMembers('project0', 'u1', 'steve', 'aefaewf')
# print(remove)

'''
getAllEmployees
'''
# e = data.getAllEmployees()
# for i in e:
#     print(i)
#     print(e[i])

'''
getRecordByType
'''
# conds = {
#         'type': 'type txt',
#         'target': 'target text',
#         'initated_by': 'test0'
#         }
# r = data.getRecord(conds)
# print(r)
