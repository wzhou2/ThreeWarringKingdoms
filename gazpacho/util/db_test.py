from db import *

data = Database("test.db")
a = data.tableInDB('d')
# print(a)
vals = ['cow', 'dog', 'peep', 'a']
args = ["user TEXT", "first TEXT", "last TEXT", "password TEXT"]
b = data.createTable("users", *args)
c = data.insert("users", vals)

d = data.get("users", "user", "password")
e = data.checkUser("a")
dict = {
    "user": "c",
    "password": "b",
    "num" : 10
}
f = data.insertUser(dict)
