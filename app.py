from flask import (Flask, flash, render_template, 
                redirect, request, session, url_for)
from flask_pymongo import PyMongo
import os
if os.path.exists('env.py'):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),  # type: ignore
            debug=True)