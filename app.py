from flask import Flask, jsonify, request, send_from_directory, render_template
import json
import os

app = Flask(__name__, static_folder='static')

ENTRIES_FILE = 'entries.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-entries')
def get_entries():
    with open(ENTRIES_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/update-entries', methods=['POST'])
def update_entries():
    updated_data = request.json
    with open(ENTRIES_FILE, 'w') as f:
        json.dump(updated_data, f, indent=2)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
