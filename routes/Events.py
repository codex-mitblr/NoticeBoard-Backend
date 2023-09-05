from flask import request
from flask_restful import Resource, Api
import random, string
from Database.mongo import Database

db = Database("events")



def create_event_id():
    event_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
    while db.find({"eventid": event_id}).count() > 0:
        event_id = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return event_id

def add_event(event):
    db.insert(event)

class Events(Resource):

    def get(self):
        
        events = db.find({})

        return events, 200

    def post(self):
        
        data = request.get_json()
        event_name = data['event_name']
        event_description = data['event_description']
        event_date = data['event_date']
        event_time = data['event_time']
        event_venue = data['event_venue']
        event_type = data['event_type']
        max_team_size = data['max_team_size']
        event_assets = data['event_assets']
        event_club_id = data["club_id"]
        event_id = create_event_id()

        event = {
            "event_name": event_name,
            "event_description": event_description,
            "event_date": event_date,
            "event_time": event_time,
            "event_venue": event_venue,
            "event_type": event_type,
            "max_team_size": max_team_size,
            "eventid": event_id,
            "event_assets": event_assets,
            "event_club_id": event_club_id
        }

        add_event(event)
        return {"message": "Event created successfully", "event_id": event_id}, 201

        