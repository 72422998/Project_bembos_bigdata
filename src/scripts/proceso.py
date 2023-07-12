import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
import matplotlib.pyplot as excel


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
coleccion_ventas = base_datos["ventas"]

#Obtener los datos de la coleccion ventas
datos_ventas = list(coleccion_ventas.find())

#crear dataframe de pandas con los datos de mongodb
df_ventas = pd.DataFrame(datos_ventas)

#Realizar la preparacion de datos
#Convertir las fechas en el formato adecuado
df_ventas["fecha"] = pd.to_datetime(df_ventas["fecha"])

#Ralizar el modelado de relacion de datos utilizando pandas
ventas_por_mes = df_ventas.groupby(pd.Grouper(key="fecha",freq="M")).sum()["monto_venta"]

#Realizar analisis y realizacion de las ventas por mes
ventas_por_mes.plot(kind="bar")
excel.xlabel("Mes")
excel.ylabel("Ventas")
excel.title("Ventas por mes")
excel.show()