import os

from pymongo import MongoClient
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

db = client['ToDoApp']  # Database name
tasks_collection = db['tasks']  # Collection name

# List of existing To-Dos
todos = [
    {
        "name": "Apple Vision Pro Demo",
        "date_limitation": "None",
        "description": "Test Apple Vision Pro in Munich Apple Store -> Jana needs to organise",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Studio of Wonders",
        "date_limitation": "None",
        "description": "Sendlinger Str. 10, 80331 München",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Happy End Hotel",
        "date_limitation": "None",
        "description": "Paul-Heyse-Straße 18, 80336 München",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Poetry Slam",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Ice Skating",
        "date_limitation": "01.02.2025",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Munich Tour by Lilli Denker",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Thiel Area Munich",
        "date_limitation": "None",
        "description": "Hippster Area of Munich which is apparently worth a visit",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Museum Lichtspiele",
        "date_limitation": "None",
        "description": "Cinema next to Lilli's place where we can watch a movie",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "House of Banksy",
        "date_limitation": "16.02.2025",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Escape Room",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Jump Town or similar",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Ballet Nuremberg",
        "date_limitation": "None",
        "description": "Aiming for end of January -> ask Lucas for tickets",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },

    {
        "name": "Luffy Pancakes",
        "date_limitation": "None",
        "description": "Food",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Food"
    },
    {
        "name": "Musical",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Dinner at Lilli's",
        "date_limitation": "None",
        "description": "Made Lilli's signature dish, oven veggies, and watched 'Carol' ",
        "done": True,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "The moment you took my hand",
        "category": "Food"
    },
    {
        "name": "Dinner at Jana's",
        "date_limitation": "01.02.2025",
        "description": "Not possible before February",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Food"
    },
    {
        "name": "Solimans Dream",
        "date_limitation": "05.02.2025",
        "description": "Christmas Light Show in Munich. Brunnenhof der Residenz München",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Pretty Pizzy",
        "date_limitation": "None",
        "description": "Food",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Food"
    },
    {
        "name": "Rock the Ballet",
        "date_limitation": "01.04.2025",
        "description": "Starts in April in Munich",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Meta Quest with Lilli",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Holey Night",
        "date_limitation": "11.01.2025",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Party"
    },
    {
        "name": "Defcon 2025",
        "date_limitation": "01.08.2025",
        "description": "Biggest Hacker Event in the world in Las Vegas",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Singing",
        "date_limitation": "None",
        "description": "https://www.gasteig.de/themen/mitsingen-im-gasteig/. Only on Sundays",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Bavaria Film Museum",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
    {
        "name": "Vertigo Bar",
        "date_limitation": "None",
        "description": "Food",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Drinks"
    },
    {
        "name": "Planetarium im Deutschen Museum",
        "date_limitation": "None",
        "description": "N/A",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Event"
    },
{
        "name": "Peet and the Flat White",
        "date_limitation": "None",
        "description": "Brunch",
        "done": False,
        "favourite_moment_lilli": "TBD",
        "favourite_moment_jana": "TBD",
        "category": "Food"
    },
]

# Insert To-Dos into the collection
result = tasks_collection.insert_many(todos)
print(f"Inserted {len(result.inserted_ids)} tasks into the database!")
