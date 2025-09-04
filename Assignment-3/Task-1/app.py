
from flask import Flask, jsonify
import json
import os
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
DATA_FILE = os.path.join(BASE_DIR, "data.json")
# Route definition
@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Read data from JSON file
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data)   # Return data as JSON response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
