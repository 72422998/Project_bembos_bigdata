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

# Verificar si la colección existe
nombre_coleccion = 'ventas'
if nombre_coleccion in base_datos.list_collection_names():
    print(f'La colección {nombre_coleccion} ya existe')
else:
    # crear la base de datos si no existe
    if database_name not in cliente.list_database_names():
        cliente[database_name].command("create")
    
    # Crea una nueva colección
    try:
        coleccion = base_datos.create_collection(nombre_coleccion)
        print(f'Se ha creado la colección {nombre_coleccion}')
    except CollectionInvalid as e:
        print(f'Error al crear la colección: {e}')