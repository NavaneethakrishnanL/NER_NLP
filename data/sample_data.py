from pymongo import MongoClient

# 🔹 Update based on your setup
MONGO_URI = "mongodb://admin:password@localhost:27017"
DATABASE_NAME = "test_db"
COLLECTION_NAME = "users"


def seed_users():
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    # Sample data
    users = [
        {
            "id": 1,
            "email_id": "vishwa@example.com",
            "firstName": "Vishwa",
            "lastName": "Priya"
        },
        {
            "id": 2,
            "email_id": "geetha@example.com",
            "firstName": "Geetha",
            "lastName": "Raman"
        },
        {
            "id": 3,
            "email_id": "sofeiya@example.com",
            "firstName": "Sofeiya",
            "lastName": "Khan"
        },
        {
            "id": 4,
            "email_id": "vivek@example.com",
            "firstName": "Vivek",
            "lastName": "Sharma"
        }
    ]

    # Insert data
    result = collection.insert_many(users)

    print(f"✅ Inserted {len(result.inserted_ids)} users")

    client.close()


if __name__ == "__main__":
    seed_users()