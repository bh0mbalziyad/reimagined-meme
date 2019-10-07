from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# import from local files
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "jose"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

status_code={
    "ok" : 200,
    "not-found" : 404,
    "created" : 201,
    "accepted" : 202,
    "bad-request" : 400
}

# Register endpoints with API
api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

# run app with specific port number
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)