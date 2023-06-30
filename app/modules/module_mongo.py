import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')


class MongoLink():
    def __init__(self):
        self.client = MongoClient(MONGO_HOST)

    def get_db(self):
        return self.client['pbandai']

    def get_collection(self, collection_name):
        return self.get_db()[collection_name]

    def get_all(self, collection_name):
        return self.get_collection(collection_name).find()

    def get_one(self, collection_name, query):
        return self.get_collection(collection_name).find_one(query)

    def insert_one(self, collection_name, data):
        return self.get_collection(collection_name).insert_one(data)

    def update_one(self, collection_name, query, data):
        return self.get_collection(collection_name).update_one(query, data)

    def upsert_one(self, collection_name, query, data):
        return self.get_collection(collection_name).update_one(query, data, upsert=True)

    def update_many(self, collection_name, query, data):
        return self.get_collection(collection_name).update_many(query, data)

    def delete_one(self, collection_name, query):
        return self.get_collection(collection_name).delete_one(query)

    def delete_many(self, collection_name, query):
        return self.get_collection(collection_name).delete_many(query)

    def get_monitor_item(self, key_id, item_id):
        # get an item to monitor
        combined_id = str(key_id) + '::' + str(item_id)
        return self.get_collection('item_monitor').find_one({'combined_id': combined_id})

    def get_monitor_items(self):
        return self.get_collection('item_monitor').find({'monitor': True})

    def add_monitor_item(self, key_id, item_id):
        # upsert an item to monitor
        combined_id = str(key_id) + '::' + str(item_id)

        filter = {
            'combined_id': combined_id,
        }

        update = {
            '$set': {
                'key_id': key_id,
                'item_id': item_id,
                'monitor': True,
            }
        }

        return self.upsert_one('item_monitor', filter, update)

    def deactivate_monitor_item(self, key_id, item_id):
        # deactivate an item to monitor
        combined_id = str(key_id) + '::' + str(item_id)

        filter = {
            'combined_id': combined_id,
        }

        update = {
            '$set': {
                'key_id': key_id,
                'item_id': item_id,
                'monitor': False,
            }
        }

        return self.update_one('item_monitor', filter, update)

    def mass_deactivate_monitor_items(self, key_ids):
        # deactivate all items to monitor
        filter = {
            'combined_id': {
                '$in': key_ids
            }
        }

        update = {
            '$set': {
                'monitor': False,
            }
        }

        return self.update_many('item_monitor', filter, update)
