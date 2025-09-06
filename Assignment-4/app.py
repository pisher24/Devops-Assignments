from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB Atlas (replace <uri> with your connection string)
client = MongoClient(""mongodb+srv://pisher24_db_user:hV9aUERxMK9AlCnB@tute-dude-project-devop.niiczny.mongodb.net/?retryWrites=true&w=majority&appName=tute-dude-project-Devops"")
db = client["todo_db"]
collection = db["items"]
    
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({"error": "Both itemName and itemDescription are required"}), 400

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"message": "To-Do item submitted successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
