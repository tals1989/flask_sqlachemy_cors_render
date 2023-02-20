import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name


@app.route('/')
def test():
    return '<h1>Welcome' 


@app.route('/waga')
def test1():
    return '<h1>Welcome' 

@app.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return ({"desc":new_item.description,"sName":new_item.name})

@app.route('/item', methods=['GET'])
@app.route('/item/<int:item_id>', methods=['GET'])
def read_item(item_id=-1):
    if (item_id>-1):
        item = Item.query.get(item_id)
        return jsonify({'name': item.name, 'description': item.description,"id":item.id})
    else:
        ar=[]
        for item in Item.query.all():
            ar.append({'name': item.name, 'description': item.description,"id":item.id})
        return(json.dumps( ar))

@app.route('/item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = Item.query.get(item_id)
    item.name = data['name']
    item.description = data['description']
    db.session.commit()
    return jsonify({'message': 'Item updated'})

@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': item_id})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)