import sqlite3
from flask_restful import Resource, reqparse
from db import query
from ..models.user import UserModel


class UserRegister(Resource):

    # this parser will going to require username and password for any user that will be created
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This argument cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This argument cannot be blank."
                        )

    # post method used to create a new user
    @staticmethod
    def post():
        data = UserRegister.parser.parse_args()
        user = UserModel(data['username'], data['password'])
        
        if UserModel.find_by_username(data['username']) is None:
            user.save_to_db()
        else:
            return {"message": "User " + data['username'] + " already exists, please choose another username!"}, 400
        return {"message": "User " + data['username'] + " created!"}, 201
