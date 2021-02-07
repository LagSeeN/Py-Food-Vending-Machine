import pymongo

server = 'mongodb+srv://vending_machine:wYvBQGPZHF6tMGbqHueyZZeWMjcuq47zSA6p9DifL3WeExvSi5RWE4hYuuwAcgG4ZoSNoXyYb37txCESZw6UfffmFrnuRZXP4Rpqd9LfRMEq8K3toKAwsuUcbakHvz58@clustertni.kt6oq.mongodb.net/Food_Vending_Machine?retryWrites=true&w=majority'


def search_data():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        found = db['products'].count_documents({})
        print('Data in {}'.format(found))


def count_data():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        found = db['products'].count_documents({})
        return found


def get_all_image():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        cursor = db['products'].find({}, {'image': 1})
        image = []
        for i in cursor:
            image.append(i['image'])
        return image


def get_all_ids():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        cursor = db['products'].find()
        _id = []
        for i in cursor:
            _id.append(i['_id'])
        return _id


def get_food(_id):
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        where = {'_id': _id}
        cursor = db['products'].find_one(where, {'_id': 1, 'product_name': 1, 'price': 1, 'stock': 1})
        return cursor
