from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message' : 'No such store found.'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message' : 'A store with name "{}" already exists.'.format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return{'message':'An internal error occurred.'}, 500
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
        return {'message':'Item deleted successfully.'}, 200
    
class StoreList(Resource):

    def get(self):
        return {'stores' : [store.json() for store in StoreModel.query.all() ]}