# A shell for Flask API using Flask Restful & JWT Authentication & Blueprint 
# It demonstrate how to split the app in sections that may use different routing approaches

from flask import Flask, request, Blueprint
#from flask_bcrypt import Bcrypt

from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
#from resources.routes import initialize_routes

from .dashboards import blpr

import os

app = Flask(__name__)
api = Api(app)

#KEY = os.getenv('API_KEY')
app.config['JWT_SECRET_KEY'] = 'supersecretkey'

jwt = JWTManager(app)

parser = reqparse.RequestParser()

def create_app():
	app = Flask(__name__)
	api = Api(app)
	app.config['JWT_SECRET_KEY'] = 'supersecretkey'

	jwt = JWTManager(app)

	with app.app_context():
		class HelloWorld(Resource):
			def get(self):
				return {'hello': 'world'}

		class Login(Resource):
			def post(self):
				data = request.json
				user_id = data["user_id"]
				pwd = data['pwd']
				print(user_id)
				access_token = create_access_token(identity = data['user_id'])
				return {'user_id': user_id,
						'access_token':access_token
						}
		class Protected(Resource):
			@jwt_required
			def get(self):
				return 'the number is 42, always'

		api.add_resource(HelloWorld, '/')
		api.add_resource(Login, '/login')
		api.add_resource(Protected, '/secret')	

		app.register_blueprint(blpr.test)

		return app 
