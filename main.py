from flask import Flask
from flask_restful import Resource, Api
from routes import *

app = Flask(__name__)
api = Api(app)


api.add_resource(RegisterUser, '/register-user')
api.add_resource(Register, '/register')
api.add_resource(Events, '/events')
api.add_resource(Login, '/login')
api.add_resource(Club, '/club')


if __name__ == '__main__':
    app.run(debug=False, port=5000)