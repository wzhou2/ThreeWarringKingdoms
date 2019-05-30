from util.db import *

# data = Database("../data/block.db")
# d = data.get("users", "*", "WHERE user='asd'")
# print(d)

data = Database("test.db")
a = data.tableInDB('d')
# print(a)

''' functions tested:
createTable
tableInDB
insert 
'''
# vals = ['userna', 'frist', 'lsat', 'pw', 100, 'noob']
# args = ["user TEXT", "first TEXT", "last TEXT", "password TEXT", "salary INTEGER", "position TEXT"]
# b = data.createTable("test_user", *args)
# print(b)
# t = data.tableInDB("users")
# print(t)
# c = data.insert("users", vals)
# print(c)

'''
get
checkUser
insertUser
verifyuser
getUser
'''
# d = data.get("users", "user", "password")
# print(d)
# e = data.checkUser("userna")
# f = data.checkUser("bleh")
# print(e, f)
# di = {
#     "first": "f1",
#     "last": "l1",
#     "password": "cba",
#     "salary": 1000000,
#     "position": "boss"
# }
# f = data.insertUser(di)
# print(f)
# ver = data.verifyUser( 'test1', 'cba' )
# print(ver)
# guser = data.getUser('test1')

'''
updateSchedule
getSchedule
'''

sch = {
        'monday': 'a0',
        'tuesday': 'a1',
        'wednesday': 'a2',
        'thursday': 'a3',
        'friday': 'a4',
        'saturday': 'a5',
        'sunday': 'a6',
        }
# s = data.updateSchedule( 'test0', sch )
# gets = data.getSchedule('test1')
# print(gets)



# def test(*a):
#     print(a)
#     d = ' '.join([str(i) for i in a])
#     print(d)

# test( 1,2,3,4 )
