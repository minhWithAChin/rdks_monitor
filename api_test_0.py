from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, emit
# from werkzeug.middleware.proxy_fix import ProxyFix
from gen_testdata import generate_rdks_test_data_point as genRdks
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim'
socketio = SocketIO(app, cors_allowed_origins="*")


# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )

# Opening and reading the JSON file
with open('rdks_testdaten.json', 'r') as f:
    # Parsing the JSON file into a Python dictionary
    data = json.load(f)

d=[]

def addDatapoint(inList:list) -> list:
    inList.append(genRdks())
    return inList

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    return send_file('static/index.html')

@app.route("/api", methods=['GET'])
def sendData(): 
    return addDatapoint(d)

@socketio.on('message')
def handle_message(data):
    print(f'Empfangen: {data}')
    emit('response', f'Echo: {data}', broadcast=True)

@socketio.on('update')
def sendUpdate(data):
    print(f'update: {data}')
    emit('response', f'Echo: {data}', broadcast=True)

@socketio.on('connect')
def handle_connect():
    print('Client verbunden')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client getrennt')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)