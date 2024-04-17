from flask import Flask, jsonify, request
import psutil

app = Flask(__name__)

@app.route('/processes', methods=['GET'])
def get_process():
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    print(processes, "\n")
    return jsonify(processes)

