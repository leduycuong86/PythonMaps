import os

from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', 'GOOGLE_MAPS_API_KEY')


@app.context_processor
def get_user():
    return dict(GOOGLE_MAPS_API_KEY=GOOGLE_MAPS_API_KEY)


def recv_basic(the_socket):
    total_data = []

    while True:
        data = the_socket.recv(1)
        if not data:
            break
        total_data.append(data)
    return ''.join(total_data)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/map")
def map():
    import ast

    start = request.args.get('start', '')
    dest = request.args.get('dest', '')

    try:
        coords = ast.literal_eval('((' + str(start) + '),(' + str(dest) + '))')

        if len(coords[0]) != 2 or len(coords[1]) != 2:
            raise IndexError()
    except (IndexError, SyntaxError):
        return redirect(url_for('index'))

    import socket

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))

    clientsocket.send(str(coords))

    returnData = recv_basic(clientsocket)

    # clientsocket.close()

    if returnData == '':
        returnData = "{\"none\": \"true\"}"

    return render_template('map.html', json_data=returnData)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
