import pymongo

server = 'mongodb+srv://vending_machine:wYvBQGPZHF6tMGbqHueyZZeWMjcuq47zSA6p9DifL3WeExvSi5RWE4hYuuwAcgG4ZoSNoXyYb37txCESZw6UfffmFrnuRZXP4Rpqd9LfRMEq8K3toKAwsuUcbakHvz58@clustertni.kt6oq.mongodb.net/Food_Vending_Machine?retryWrites=true&w=majority'


def serchData():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        found = db['products'].count_documents({})
        print('Data in {}'.format(found))


def countData():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        found = db['products'].count_documents({})
        return found


def getAllImage():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        cursor = db['products'].find()
        image = []
        for i in cursor:
            image.append(i['image'])
        return image


def getAll_Id():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        cursor = db['products'].find()
        _id = []
        for i in cursor:
            _id.append(i['_id'])
        return _id


def getFood(_id):
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        where = {'_id': _id}
        cursor = db['products'].find(where)
        food = []
        for i in cursor:
            food.append(i)
        return food
