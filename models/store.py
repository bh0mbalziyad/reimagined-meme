from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel')

    def __init__(self, name):
        self.name = name
    
    def json(self):
        # print("Debug")
        # print(self.items.all())
        return {'name' : self.name, 'items' : [item.json() for item in self.items]}

    @classmethod
    def find_by_name(cls, name):
        # select * from items where name=name limit 1
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()