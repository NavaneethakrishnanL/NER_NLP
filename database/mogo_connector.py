from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# 🔹 Update these values based on your setup
MONGO_URI = "mongodb://admin:password@localhost:27017"
DATABASE_NAME = "test_db"
COLLECTION_NAME = "users"


class MongoDBConnector:

    def __init__(self):
        try:
            # Create Mongo client
            self.client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

            # Trigger connection check
            self.client.server_info()

            print("✅ Connected to MongoDB")

            # Access DB and collection
            self.db = self.client[DATABASE_NAME]
            self.collection = self.db[COLLECTION_NAME]

        except ConnectionFailure as e:
            print("❌ Could not connect to MongoDB:", e)
            raise

    def run_query(self, query):
        results = self.collection.find(query)
        return list(results)

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def close(self):
        self.client.close()