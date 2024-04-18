import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb+srv://justin:justin123@cluster0.lhij5pu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db = client['thesisDb'] # database name this will be created if not present
collection = db['thesisCollection'] # collection name


document = {"name" : "Justin", "age" : 22}
insertedDoc = collection.insert_one(document)

print("Inserted Document Success")
print("Document inserted with id: ", insertedDoc.inserted_id)

client.close()