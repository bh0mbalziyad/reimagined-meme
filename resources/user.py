import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
# from app import status_code

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        required=True,
        type=str,
        help="Username field required."
    )
    parser.add_argument(
        'password',
        required=True,
        type=str,
        help="Password field required."
    )
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']) :
            return {"message" : "Username unavailable."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES(NULL, ?,?)"
        cursor.execute(query,(data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message" : "User created successfully."}, 201
    