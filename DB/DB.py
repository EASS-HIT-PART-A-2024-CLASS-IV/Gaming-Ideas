import pymongo

# Connect to MongoDB
def connect_to_mongodb(uri):
    client = pymongo.MongoClient(uri)
    return client

# Insert data into MongoDB
def insert_data(db, collection, data):
    db[collection].insert_one(data)

# Delete data from MongoDB
def delete_data(db, collection, query):
    db[collection].delete_many(query)

if __name__ == "__main__":
    mongodb_uri = "mongodb://localhost:27017/"

    client = connect_to_mongodb(mongodb_uri)


    db = client["gaming_store"]
    collection = db["games"]


    game_data = {
        "name": "FIFA 24",
        "platform": "PS4",
        "edition": "Standard",
        "price": 59.99
    }

    # Insert data into MongoDB
    insert_data(db, collection, game_data)

    # Delete data from MongoDB (sample query)
    delete_query = {"name": "FIFA 24"}
    delete_data(db, collection, delete_query)

