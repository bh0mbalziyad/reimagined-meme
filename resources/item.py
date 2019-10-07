from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


# handles endpoint /item/<string:name>
# handles endpoint /items

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        required=True,
        type=float,
        help='This field cannot be left empty.'
    )
    parser.add_argument(
        'store_id',
        required=True,
        type=int,
        help='Store ID is required'
    )


    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message' : 'Item not found.'}, 404
    
    # @classmethod
    # def find_by_name(cls, name):

    # @classmethod
    # def insert(cls, item):
    
    # @classmethod
    # def update(cls, item):

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
        return {'message' : 'Item deleted successfully.'}, 200

    def post(self, name):
        # there already exists an item with the specified name
        if ItemModel.find_by_name(name):
            return {"message" : "An item with name '{}' already exists.".format(name)}, 400

        # get data from request body
        data = Item.parser.parse_args()
        # create new item
        item = ItemModel(name, data["price"], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message','An error occurred inserting the item.'}, 500
        
        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item: #exists
            try:
                item.price = data['price']
                item.store_id = data['store_id']
            except:
                return {'message' : 'An error occurred.'}, 500
        else: #doesn't exists
            try:
                item = ItemModel(name, **data)
            except:
                return {'message' : 'An error occurred inserting the item'}, 500
        item.save_to_db()
        return item.json(), 201
        


class Items(Resource):
    def get(self):
        return({'items' : [item.json() for item in ItemModel.query.all()]})
        # or list(map(lambda x : x.json(), ItemModel.query.all()))
