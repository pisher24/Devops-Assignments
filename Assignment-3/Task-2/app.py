from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
import dotenv

# MongoDB Atlas connection
#MONGO_URI = "your_mongodb_atlas_connection_string_here"
#client = MongoClient(MONGO_URI)
#db = client["testdb"]       # database name
#collection = db["students"] # collection name
'''instead of embedding connection string in the code we will adhere to good coding practices and
use environment variables to store sensitive data
For using environment variabke we need a specific library called dotenv specified in the requirements.txt

'''

dotenv.load_dotenv()
MONGO_URI =  os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
database = client.testdb
collection = database['flask-tutorial']


app = Flask(__name__)

@app.route("/submit", methods=["GET", "POST"])
def index():
    error_message = None
    if request.method == "POST":
        name = request.form.get("name")
        grade = request.form.get("grade")
        
        if not name or not grade:
            error_message = "Both name and grade are required."
            return render_template("form.html", error=error_message)

        if not name.isalnum() or not grade.isalnum():
            error_message = " Something went wrong! please ensure that both name and grade must contain only letters and numbers (alphanumeric). and should also not be blank"
            return render_template("form.html", error=error_message)

        try:
            collection.insert_one({"name": name, "grade": grade})
            return redirect(url_for("success"))
        except Exception as e:
            error_message = f"Error inserting data: {str(e)}"
            return render_template("form.html", error=error_message)

    return render_template("form.html", error=error_message)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
