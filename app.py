import json, config
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/webhook", methods=['POST'])
def whatever():
    data = json.loads(request.data)
    if data['passphrase'] != config.WEBHOOK_PASSPHRASE:
        print(config.WEBHOOK_PASSPHRASE)
        return {
            "code": "error",
            "message": "Nice try, invalid passphrase"
        }
    print(data['passphrase'])
    print(data["ticker"])
    print(data['bar'])
    return {
        "code": "success",
        "message": str(request.data)
    }
