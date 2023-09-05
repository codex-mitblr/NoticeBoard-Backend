from flask import request
from flask_restful import Resource, Api
import random, string
from Database.mongo import Database
import hashlib

db = Database("users")


def find_user(email, password):

    user = db.find_one({"email": email, "password": password})
    
    return user




class Login(Resource):

    def post(self):

        data = request.get_json()
        password = data['password']
        email = data["email"].lower()
        password = hashlib.sha256(password.encode()).hexdigest()

        user = find_user(email, password)

        if user == None:
            return {"message": "Invalid credentials"}, 406
        
        return {"message": "Login successful", "userid": user["userid"]}, 200
