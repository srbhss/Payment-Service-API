# import libraries
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from .security.security import authenticate, identity
from .resources.users import UserRegister
from .resources.transaction import ProcessPayment, transactionList
from db.database import db
import config

# flask, api and JWT inicialized with some config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_connection_uri
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = config.secret_key
app.testing = True
db.init_app(app)
@app.before_first_request  # created db tables before the first request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)
@jwt.error_handler
def error_handler(e):
    return {'message': "The request is Invalid"}, 400

api = Api(app)
# routes
api.add_resource(ProcessPayment, '/transaction')
api.add_resource(UserRegister, '/signup')

app.test