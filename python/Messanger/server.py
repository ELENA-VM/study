import time

from flask import Flask, request, abort

app = Flask(__name__)

db = []

@app.route("/")
def hello():
    return "Hello, World 123!"

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)

    if len(data) != 2:
        return abort(400)

    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str) or \
            name == '' or text == '':
        return abort(400)

    message = {
        'time': time.time(),
        'name': name,
        'text': text
    }

    db.append(message)
    return {'ok': True}


@app.route("/messages")
def get_message():
    result = []

    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    for message in db:
        if message['time'] > after:
            result.append(message)
            if len(result) >= 100:
                break

    return {'messages': result}


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time': time.asctime()
    }


app.run()
