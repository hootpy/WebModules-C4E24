import mlab
from models.user import User
mlab.connect()

while True:
    username = input("Username: ")
    password = input("Password: ")
    if username =="exit" and password == "exit":
        break
    new_user = User(username=username,password=password)
    print("creating user")
    new_user.save()
    print("done")