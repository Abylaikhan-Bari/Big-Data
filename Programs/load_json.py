import json
from mongo_connection import get_database

def load_json(file_path, collection_name):
    db = get_database("your_database_name")
    collection = db[collection_name]

    with open(file_path, 'r') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)
