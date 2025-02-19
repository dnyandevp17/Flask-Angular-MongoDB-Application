from flask import Flask
from flask_pymongo import PyMongo 
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/PersonalInfo"
app.config["CORS_HEADERS"] = "Content-Type"

mongodb_local = PyMongo(app)

from project1 import routes

