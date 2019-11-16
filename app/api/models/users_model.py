from flask import Flask, abort

USERS = [];

class User(object):
    def __init__(self):
        self.users = USERS
        
    def get_users(self):
        return self.users
    
    def register(self,email, password):
        user = {
            'email':email,
            'password':password
        }
        
        self.users.append(user)
        

    def login(self, email, password):
        user = [task for task in self.users if task['email'] == email and task['password'] == password]

        # if(!user){
        #     abort(400)
        # }

        return user