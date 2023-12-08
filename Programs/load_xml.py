import xml.etree.ElementTree as ET
from mongo_connection import get_database

def load_xml(file_path, collection_name):
    db = get_database("your_database_name")
    collection = db[collection_name]

    tree = ET.parse(file_path)
    root = tree.getroot()

    for item in root:
        data = {}
        for child in item:
            data[child.tag] = child.text
        collection.insert_one(data)
