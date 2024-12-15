import os

from pymongo import MongoClient, UpdateOne
import certifi
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

# Connect to MongoDB

db = client['ToDoApp']  # Database name
tasks_collection = db['tasks']  # Collection name

# Add new fields with default values
update_operations = [
    UpdateOne(
        {},
        {
            "$set": {
                "favourite_moment_lilli": "",
                "favourite_moment_jana": "",
                "category": None  # Category can be one of the enums
            }
        },
        upsert=False
    )
]

# Update all documents in the collection
result = tasks_collection.bulk_write(update_operations)
print(f"Modified {result.modified_count} documents!")
