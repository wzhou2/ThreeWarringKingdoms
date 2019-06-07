from util.db import *
from util.timestamp import *

# data = Database("../data/block.db")
# d = data.get("users", "*", "WHERE user='asd'")
# print(d)

data = Database("util/test.db")
# data = Database("data/block.db")
# a = data.tableInDB('d')
# print(a)

''' functions tested:
createTable
tableInDB
insert 
'''
# vals = ['eeeuserna', 'frist', 'lsat', 'pw']
# args = ["user TEXT", "first TEXT", "last TEXT", "password TEXT", "salary INTEGER", "position TEXT"]
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
# d = data.get("users", "username", "password")
# print(d)
# e = data.checkUser("userna")
# f = data.checkUser("bleh")
# # print(e, f)
# di = {
#     "username": "a0",
#     "first": "dsa",
#     "last": "earaelname1",
#     "password": "pw1",
#     "salary": 100,
#     "position": "employee"
# }
# f = data.insertUser(di)
# di = {
#     "username": "a1",
#     "first": "dsa",
#     "last": "earaelname1",
#     "password": "pw1",
#     "salary": 100,
#     "position": "employee"
# }
# f = data.insertUser(di)
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
# info = {
#     'target': 'target text',
#     'type': 'type txt',
#     'description': 'descr text',
#     'message': 'msg text',
#     'view_level': 900
#         }
# a = data.checkProject('project0')
# print(a)
# proj = data.createProject('project0', 'a0', 'ooffffffffffff')
# print(proj)
# print(data.checkProject('project0'))
# add = data.addMembers('project0', 'u1', 'u2')
# add = data.addMembers('project0', 'bob', 'steve')
# print(add)
# remove = data.removeMembers('project0', 'u1', 'steve', 'aefaewf')
# print(remove)
# proj = data.createProject('project2', 'a1', 'p2 faweseaeeeee')
# add = data.addMembers('project2', 'u1', 'u2', 'a0')

g = data.getProjects('bob')

'''
getAllEmployees
'''
# e = data.getAllEmployees()
# print(e)
# for i in e:
#     print(i)
#     print(e[i])

'''
Timeline functions
'''
timeline_info = {
        'username': 'a1',
        'title': 'adsfjawelk',
        'description': 'desccccccccccccc'
        }
# a = data.createEvent(timeline_info)
# print(a)
# b = data.deleteEvent(2)
# print(b)
# c = data.getAllEvents()
# print(c)
