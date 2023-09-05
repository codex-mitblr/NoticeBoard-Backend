from flask import request
from flask_restful import Resource, Api
import random, string
from Database.mongo import Database
import hashlib

db = Database("users")

def check_user(email):

    if db.find({"email": email}) == None:
        return True
    return False

def confirm_user_id(userid):
    test = db.find({"userid": userid})
    print(test)
    if test == None:
        return True
    return False

def add_user(user):
    db.insert(user)


class RegisterUser(Resource):

    def post(self):

        data = request.get_json()
        email = data["email"].lower()
        password = data['password']
        userid = data["userid"]
        
        password = hashlib.sha256(password.encode()).hexdigest()

        if email.endswith("@learner.manipal.edu") == False:
            return {"message": "Email must be Student Email"}, 406

        if check_user(email):
            return {"message": "User already exists"}, 406    
    

        # while confirm_user_id(userid) == False:
        #     userid = ''.join(random.choice(string.ascii_letters) for i in range(10))

        user = {
            "email": email,
            'password': password, 
            'userid': userid
        }
        add_user(user)

        message = {
            "message": "User created successfully",
            "userid": userid
        }
        return message, 201