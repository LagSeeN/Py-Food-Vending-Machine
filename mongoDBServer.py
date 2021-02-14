import pymongo
from datetime import datetime
import pandas as pd
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\')
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


def get_all_status():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        cursor = db['products'].find({}, {'stock': 1})
        status = []
        for i in cursor:
            status.append(i['stock'])
        return status


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


def get_food_time(_id):
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        where = {'_id': _id}
        cursor = db['products'].find_one(where, {'_id': 1, 'time': 1})
        return cursor


def food_finish(_id, current_food):
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        where = {'_id': _id}
        db['products'].update({'_id': _id}, {'$set': {'stock': current_food - 1}})
        db['transaction'].insert_one(
            {'date': datetime.now(), 'food_item': _id, 'food_name': db['products'].find_one(where)['product_name'],
             'price': db['products'].find_one(where)['price']})


def export_log():
    with pymongo.MongoClient(server) as conn:
        db = conn.get_database('Food_Vending_Machine')
        cursor = db['transaction'].find({})
        df = pd.DataFrame(list(cursor))
    current_date = df['date'].dt.month
    df['Month'] = current_date
    df_export = df[df['Month'] == 2].groupby(['food_name'])[['food_name', 'price']].agg(
        {'food_name': ['count'], 'price': ['sum']}).sort_values(by=[('food_name', 'count'), ('price', 'sum')],
                                                                ascending=[0, 1])
    filename = 'Food Vending Machine ' + str(datetime.now().year) + '-' + str(datetime.now().month)
    print(desktop + filename + '.xlsx')
    write_excel = pd.ExcelWriter(desktop + filename + '.xlsx')
    sheet_name = filename
    df_export.to_excel(write_excel, sheet_name, encoding='utf8')
    write_excel.save()
