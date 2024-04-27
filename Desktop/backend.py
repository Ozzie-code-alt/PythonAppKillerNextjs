from flask import Flask, jsonify, request, session
from flask_cors import CORS
import psutil
from LocalBrowser import  pass_visited_website, initialize_driver

app = Flask(__name__)
app.secret_key = 'abuhsaduash21321' # Replace 'your_secret_key' with a secure, random string
CORS(app, origins=["*"])

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


@app.route('/active_tab', methods=['GET'])
def get_Tab():
    driver = initialize_driver()
    visited_websites = pass_visited_website(driver)
    # Quit the driver after use
    return jsonify(visited_websites)


@app.route('/process-data', methods=['GET', 'POST'])
def grab_data():
    if request.method == 'POST':
        if request.content_type != 'application/json':
            return jsonify({'error': 'Content-Type must be application/json', "content-type is" : request.content_type}), 400
        
        print("Processing data")
        print("Request method:", request.method)
        print("Request headers:", request.headers)
        
        if 'data' in request.json:
            data = request.get_json(force=True)
            print("this is flask data ", data)
            # Store the data in the session
            session['processed_data'] = data
            print('Data: processed')
            return jsonify(data) # Return the result as JSON
        else:
            return jsonify({'error': "Missing 'data' key in request"}, 400)
    else:
        # Handle GET requests if needed
        return jsonify({'message': 'GET request to /grab-process-data'})

@app.route('/grab-process-data', methods=['GET'])
def grab_processed_data():
    # Retrieve the data from the session
    data = session.get('processed_data', None)
    if data is None:
        return jsonify({'error': 'No processed data available'}), 404
    else:
        return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)