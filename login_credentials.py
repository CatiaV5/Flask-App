import os

from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import certifi
from dotenv import load_dotenv

load_dotenv()

# Access the connection string
connection_string = os.getenv("MONGO_CONNECTION_STRING")

# MongoDB connection
try:
    client = MongoClient(connection_string, tlsCAFile=certifi.where())
except Exception as e:
    print("Failed to connect to MongoDB Atlas")
    print("Error:", e)

db = client['ToDoApp']
users_collection = db['users']

bcrypt = Bcrypt()

# Securely store credentials
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

# Insert into the database
users_collection.insert_one({"username": username, "password": hashed_password})
print("User added successfully!")
