# If Flask is not installed, run this command: pip install Flask
from flask import Flask, jsonify
from hashlib import md5
import requests

app = Flask(__name__)


# Default route if no endpoint is provided; returns "Hello, world!"
@app.route("/")
def hello_world():
    return "Hello, World!"


# Route for the /md5 endpoint
@app.route("/md5/<string:data>", methods=["GET"])
def get_md5(data=""):
    # If an endpoint is provided with no data, return a value of None
    if data == "":
        md5_hash = None

    # Otherwise, use the MD5 algorithm on the provided data
    else:
        md5_hash = md5(data.encode()).hexdigest()
    return jsonify({"input": data, "output": md5_hash}), 200


# Route for the /is-prime endpoint
@app.route("/is-prime/<int:data>", methods=["GET"])
def get_isprime(data=""):
    primecheck = True
    if data == "":
        primenumber = None
        primecheck = "No input provided"
    else:
        primenumber = int(data)
        if primenumber > 1:
            for i in range(2, int(primenumber**0.5)+1):
                if primenumber % i == 0:
                    primecheck = False
                    break
                else:
                    primecheck = True
        else:
            primecheck = False
    return jsonify({"input": primenumber, "output": primecheck}), 200


# Route for the /slack-alert endpoint
@app.route("/slack-alert/<string:data>", methods=["GET"])
def slack_alert(data=""):
    # Returns a 400 error if there's no input
    if data == "":
        return jsonify({"input": data, "output": False}), 400

    else:
        # Uses the webhook url from web_hook.txt
        slack_webhook = open("web_hook.txt", "r").read().replace('\n', '')
        message = str({"text": data})

        # Sends a post request to the webhook url with the message payload
        response = requests.post(slack_webhook, data=message)

        # If a 200 code with an ok message is returned, return a JSON with
        # {"output": True}
        if response.status_code == 200 and response.text == "ok":
            return jsonify({"input": data, "output": True}), 200

        # If anything else is returned, return a JSON with
        # {"output": False}
        else:
            return jsonify({"input": data, "output": False}), 400


# Route for factorial
@app.route("/factorial/<int:num>", methods=['GET'])
def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial*i

    return jsonify({'input': num, 'output': factorial})


# Route for fib seqeunce
@app.route("/fibonacci/<int:num>", methods=['GET'])
def fib(num):
    l = []
    a = 0
    b = 1
    while a <= num:
        l.append(a)
        a, b = b, a+b
    return jsonify({"input": num, "output": l})


# Runs the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000)
