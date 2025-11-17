from flask import Flask, render_template, send_file, send_from_directory
from flask_socketio import SocketIO, emit
# from werkzeug.middleware.proxy_fix import ProxyFix
from gen_testdata import generate_rdks_test_data_point as genRdks
import threading, time
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
    jsonData = json.load(f)

d=[]

def addDatapoint(inList:list) -> list:
    inList.append(genRdks())
    return inList

def genDatapoint():
    for i in range(10):
        time.sleep(2)
        addDatapoint(jsonData)
        print("new Datapoint added")
        socketio.emit("response",jsonData)
    print("finished")

threadGenrdks= threading.Thread(target=genDatapoint)

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
    print(type(jsonData))
    emit('response', jsonData)
    threadGenrdks.start()
    threadGenrdks.join()

@socketio.on('update')
def sendUpdate():
    print(f'update:')
    emit('response', jsonData, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print('Client verbunden')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client getrennt')




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)