
from pymongo import MongoClient
import requests
import subprocess
def insertData():
    subprocess.Popen(['C:\\Users\\Justin Santos\\Desktop\\Git_Container\\PythonAppKillerNextjs\\Desktop\\venv\\Scripts\\python.exe', 'backend.py'])
    client = MongoClient('mongodb+srv://justin:justin123@cluster0.lhij5pu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['thesisDb'] # database name this will be created if not present
    collection = db['thesisCollection'] # collection name

    # Call the API endpoint to get processes data

    try:
        response = requests.get('http://127.0.0.1:5000/processes')
        response2 = requests.get('http://127.0.0.1:5000/active_tab')
        processes_data = response.json()
        visited_websites = response2.json()
        document = {"name" : "Miguel", "age" : 108, "processes" : processes_data, "visited_websites" : visited_websites}
        insertedDoc = collection.insert_one(document)
    except Exception as e:
        print("Error inserting document: ", e)


    print("Inserted Document Success")
    print("Document inserted with id: ", insertedDoc.inserted_id)

    client.close()