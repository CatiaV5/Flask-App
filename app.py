import os
from flask_bcrypt import Bcrypt
from flask import Flask, jsonify, request, session, redirect, flash, url_for
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from pymongo import MongoClient
from flask import Flask, render_template
from datetime import datetime
from bson import ObjectId
import certifi
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change to a strong secret key
jwt = JWTManager(app)
app.secret_key = os.urandom(24)  # Secret key for session handling
bcrypt = Bcrypt(app)

# Access the connection string
connection_string = os.getenv("MONGO_CONNECTION_STRING")


try:
    client = MongoClient(connection_string, tlsCAFile=certifi.where())
except Exception as e:
    print("Failed to connect to MongoDB Atlas")
    print("Error:", e)

db = client['ToDoApp']
tasks_collection = db['tasks']
users_collection = db['users']

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML file



# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Retrieve user from the database
        user = users_collection.find_one({"username": username})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user'] = username  # Store user in session
            return redirect(url_for('dashboard'))  # Redirect to dashboard
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))

    return render_template('login.html')

# Dashboard route to display tasks
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        tasks = list(tasks_collection.find())  # Fetch tasks from MongoDB
        for task in tasks:
            task['_id'] = str(task['_id'])  # Convert ObjectId to string for JSON compatibility
        return render_template('dashboard.html', tasks=tasks, username=session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/api/tasks', methods=['GET'])
def fetch_tasks():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    tasks = list(tasks_collection.find())
    for task in tasks:
        task['_id'] = str(task['_id'])  # Convert ObjectId to string for JSON compatibility
    return jsonify(tasks)

# API route to add a task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    # Get the task data from the request
    data = request.json
    new_task = {
        "name": data.get("name", ""),
        "date_limitation": data.get("date_limitation", ""),
        "description": data.get("description", ""),
        "favourite_moment_lilli": data.get("favourite_moment_lilli", ""),
        "favourite_moment_jana": data.get("favourite_moment_jana", ""),
        "category": data.get("category", ""),
        "done": data.get("done", False),
    }

    # Insert into MongoDB
    result = tasks_collection.insert_one(new_task)
    new_task["_id"] = str(result.inserted_id)  # Convert ObjectId to string
    return jsonify(new_task), 201  # Return the newly created task


# API route to delete a task

@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    # Attempt to delete the task from MongoDB
    result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Task deleted successfully"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404



# API route to update a task
@app.route('/api/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json  # Receive the updated fields from the frontend
    update_fields = {key: value for key, value in data.items() if key != '_id'}  # Exclude _id

    result = tasks_collection.update_one(
        {"_id": ObjectId(task_id)}, {"$set": update_fields}
    )
    if result.matched_count:
        return jsonify({"message": "Task updated successfully"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404



# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
