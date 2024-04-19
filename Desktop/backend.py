from flask import Flask, jsonify, request
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)

polished_data = []  
@app.route('/processes', methods=['GET'])
def get_process():
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    
    return jsonify(processes)

if __name__ == '__main__':
    app.run(debug=True)
