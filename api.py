import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from modules import Computer

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return "<h1 style='text-align:center'>Welcome To API</h1>"

@app.route("/info/get", methods=['GET'])
def info_get():
    try:
        TIME,RAM, CPU, SSD= Computer.get_computer_info()
        data = {
            "TIME": TIME,
            "RAM": RAM,
            "CPU": CPU,
            "SSD": SSD
        }
        return jsonify(data)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    with open("config.json") as f:
        data = json.load(f)
        port = data['port']
    app.run(debug=True, port=port)
    # app.run(host='0.0.0.0', port=port)
