from flask import request
from flask_restful import Resource, Api
import random, string
from Database.mongo import Database


db = Database("clubs")

def create_club_id():
    club_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
    while db.find({"club_id": club_id}).count() > 0:
        club_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return club_id



class Club(Resource):

    def get(self):

        clubs = db.find()
        return clubs, 200

    def post(self):

        data = request.get_json()

        club_name = data["club_name"]
        club_description = data["club_description"]
        club_president = data["club_president"]
        club_id = create_club_id()

        club = {
            "club_name": club_name,
            "club_description": club_description,
            "club_id": club_id,
            "club_president": club_president
        }
        db.insert(club)

        return {"message": "Club Successfully added", "club_id": club_id}, 201