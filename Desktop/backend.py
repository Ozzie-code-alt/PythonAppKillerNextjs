from flask import Flask, jsonify, request
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)
@app.route('/processes', methods=['GET'])
def get_process():
    # Initialize an empty set to store unique process names
    unique_process_names = set()
    # Initialize an empty list to store the final list of processes
    unique_processes = []

    # Iterate over all processes
    for p in psutil.process_iter(['pid', 'name']):
        # If the process name is not in the set, add it to the set and the list
        if p.info['name'] not in unique_process_names:
            unique_process_names.add(p.info['name'])
            unique_processes.append(p.info)

    # Print the unique processes
    print(unique_processes)
    # Return the unique processes as JSON
    return jsonify(unique_processes)

if __name__ == '__main__':
    app.run(debug=True)
