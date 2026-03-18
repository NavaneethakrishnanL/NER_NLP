from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME, COLLECTION_NAME


class MongoDBConnector:

    def __init__(self):

        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def run_query(self, query):

        results = self.collection.find(query)

        return list(results)