import pymongo


def serchData():
    server = 'mongodb+srv://vending_machine:wYvBQGPZHF6tMGbqHueyZZeWMjcuq47zSA6p9DifL3WeExvSi5RWE4hYuuwAcgG4ZoSNoXyYb37txCESZw6UfffmFrnuRZXP4Rpqd9LfRMEq8K3toKAwsuUcbakHvz58@clustertni.kt6oq.mongodb.net/Food_Vending_Machine?retryWrites=true&w=majority'
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        found = db['products'].count_documents({})
        print('Data in {}'.format(found))
