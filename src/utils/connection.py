from dotenv import load_dotenv
from pymongo import MongoClient
import os

dotenv_path = "src\config\.env"

def connect_to_database():
    try:
        load_dotenv(dotenv_path)

        username = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        database_name = os.getenv('MONGO_DATABASE')

        connection_url = f"mongodb+srv://{username}:{password}@clustercertus.d8tb7.mongodb.net/?{database_name}retryWrites=true&w=majority"

        client = MongoClient(connection_url)

        database = client[database_name]

        return database
    except Exception as e:
        print("Error al conectar a la base de datos:",str(e))

def retrieve_data(collection):
    try:
        data = collection.find()
        return data
    except Exception as e:
        print("Error al recuperar datos:",str(e))
        return None
    
if __name__ == "__main__":
    db = connect_to_database()
    collection = db["productos"]
    data = retrieve_data(collection)

    for document in data:
        print(document)
        