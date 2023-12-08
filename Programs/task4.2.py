from pymongo import MongoClient

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Выбор базы данных 'BigData' и коллекции 'tasks'
db = client['BigData']
collection = db['task2']

# Пример данных для вставки
data = [
    {"example_field1": "value1", "example_field2": 10},
    {"example_field1": "value2", "example_field2": 20},
    {"example_field1": "value3", "example_field2": 30}
]

# Вставка данных в коллекцию 'tasks'
collection.insert_many(data)

# Создание индекса по 'example_field1'
collection.create_index("example_field1")
