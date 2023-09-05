from flask import request
from flask_restful import Resource, Api
from Database.mongo import Database

db = Database("registrations")
eventsdb = Database("events")

def check_user_registration(userid, eventid):
    if db.find({"userid": userid, "eventid": eventid}) == None:
        return True
    return False

def check_max_team_size(eventid, teamid):
    event = eventsdb.find({"eventid": eventid})
    
    if db.find({"eventid": eventid, "teamid": teamid}).count() < event["max_team_size"]:
        return True
    
    return False

def create_new_team(eventid):
    teamid = ''.join(random.choice(string.ascii_letters) for i in range(10))
    while db.find({"eventid": eventid, "teamid": teamid}).count() > 0:
        teamid = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return teamid

class Register(Resource):

    def post(self):

        data = request.get_json()
        userid = data['userid']
        eventid = data['eventid']
        teamid = data['preferred_teamid']
        assign_random = data['assign_random']

        if assign_random:
            teamid = create_new_team(eventid)

        if check_user_registration(userid, eventid):
            return {"message": "User already registered"}, 406
        
        if check_max_team_size(eventid, teamid):
            return {"message": "Team is full"}, 406
        
        registration = {
            "userid": userid,
            "eventid": eventid,
            "teamid": teamid
        }

        return {"message": "User registered successfully", "team_id": teamid}, 201