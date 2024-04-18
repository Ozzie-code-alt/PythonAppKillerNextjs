from flask import Flask, jsonify, request
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)

def get_chromium_urls():
    chromium_urls = []
    for process in psutil.process_iter(['pid', 'name']):
        
        if process.info['name'] in ['chrome', 'msedge', 'brave', 'chromium', 'operagx']:
            try:
                cmdline = process.cmdline()
                print(cmdline)
                for arg in cmdline:
                    # if arg.startswith('http://') or arg.startswith('https://'):
                    chromium_urls.append(arg)
            except psutil.AccessDenied:
                pass
    return chromium_urls

get_chromium_urls()

@app.route('/processes', methods=['GET'])
def get_process():
    processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
    return jsonify(processes)

@app.route('/chrome_urls', methods=['GET'])
def get_chrome_urls():
    chrome_urls = get_chromium_urls()
    return jsonify(chrome_urls)

if __name__ == '__main__':
    app.run(debug=True)
