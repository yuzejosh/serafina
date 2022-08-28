from flask import Flask
from flask_pymongo import pymongo
#from app import app

CONNECTION_STRING = "mongodb+srv://josherh:0u3jc4dnHuAO4ibu@cluster0.upcyuog.mongodb.net/test"

client = pymongo.MongoClient(CONNECTION_STRING)

# This will either find this database if it already exists, or create one
db = client.get_database('sources')

# This will create a collection named 'collection' within the above database
user_collection = pymongo.collection.Collection(db, 'user_collection')