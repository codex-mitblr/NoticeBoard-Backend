from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:

    def __init__(self, collection_name):
        
        db_name = "noticeboard"

        self.client = MongoClient(os.getenv("MONGO_URL"))
        self.client.admin.command('ping')
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        

    def insert(self, data):
        self.collection.insert_one(data)

    def find(self, query = {}):
        return self.collection.find(query)
    
    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, data):
        self.collection.update_one(query, data)

    def delete(self, query):
        self.collection.delete_one(query)

    def delete_all(self):
        self.collection.delete_many({})

    def count(self):
        return self.collection.count_documents({})

    def close(self):
        self.client.close()

    