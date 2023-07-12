import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import CollectionInvalid

""" dotenv_path = "config\.env" """

# Obtener la ruta absoluta al archivo .env utilizando la ubicación actual 
dotenv_path = "src\config\.env"

# Cargar variables de entorno desde el archivo .ebv
load_dotenv(dotenv_path)

# Obtener las variables de entorno para la conexión a MongoDB
username = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
database_name = os.getenv('MONGO_DATABASE')

# URL de conexión al Cluster de MongoDB
connection_url = f"mongodb+srv://{username}:{password}@clustercertus.d8tb7.mongodb.net/?{database_name}retryWrites=true&w=majority"

# Conexión a la base de datos MongoDB
cliente = MongoClient(connection_url)
base_datos = cliente[database_name]
coleccion = base_datos["ventas"]

datos_nuevos = [
    {
        "_id":"1",
        "producto":"Hamburguesa",
        "cantidad":12,
        "precio_unitario":10.90,
        "fecha":"2023-06-25",
        "monto_venta":10

    },
    {
        "_id":"2",
        "producto":"papas fritas",
        "cantidad":1,
        "precio_unitario":4.99,
        "fecha":"2023-06-26",
        "monto_venta":15
    },
    {
        "_id":"3",
        "producto":"papas fritas",
        "cantidad":1,
        "precio_unitario":4.99,
        "fecha":"2023-05-26",
        "monto_venta":15
    },
    {
        "_id":"4",
        "producto":"papas fritas",
        "cantidad":1,
        "precio_unitario":4.99,
        "fecha":"2023-04-21",
        "monto_venta":9
    },
    {
        "_id":"5",
        "producto":"gaseosa",
        "cantidad":3,
        "precio_unitario":4.99,
        "fecha":"2023-02-26",
        "monto_venta":20
    }
]
#Insertar los documentos de la coleccion
coleccion.insert_many(datos_nuevos)