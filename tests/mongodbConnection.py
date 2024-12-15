from pymongo import MongoClient
import certifi
# Replace with your MongoDB Atlas connection string
CONNECTION_STRING = "mongodb+srv://test-user-1:fDewHphCn1fWeYEC@cluster0.gjzij.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
    # List all databases
    databases = client.list_database_names()
    print("Connected to MongoDB Atlas!")
    print("Databases:", databases)
except Exception as e:
    print("Failed to connect to MongoDB Atlas")
    print("Error:", e)
