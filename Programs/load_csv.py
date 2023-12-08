import pandas as pd
from mongo_connection import get_database

def load_csv(file_path, collection_name):
    db = get_database("your_database_name")
    collection = db[collection_name]

    data = pd.read_csv(file_path)
    payload = json.loads(data.to_json(orient='records'))

    collection.insert_many(payload)
