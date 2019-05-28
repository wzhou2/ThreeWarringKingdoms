from db import *

# data = Database("../data/block.db")
# d = data.get("users", "*", "WHERE user='asd'")
# print(d)

data = Database("test.db")
a = data.tableInDB('d')
# print(a)

# CREATE TABLE and INSERT USER
# vals = ['userna', 'ja', 'ck', 'pw']
# args = ["user TEXT", "first TEXT", "last TEXT", "password TEXT"]
# b = data.createTable("test_user", *args)
# c = data.insert("test_user", vals)

# GET USER
d = data.get("users", "user", "password")
print(d)
e = data.checkUser("c")
print(e)
di = {
    "user": "c",
    "first": "frist",
    "last": "lsat",
    "password": "b",
}
f = data.insertUser(di)

# def test(*a):
#     print(a)
#     d = ' '.join([str(i) for i in a])
#     print(d)

# test( 1,2,3,4 )
