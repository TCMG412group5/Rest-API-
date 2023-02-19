# If Flask is not installed, run this command: pip install Flask

from flask import Flask, jsonify, request
from hashlib import md5

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# Route for the /md5 endpoint
# The 3 routes are to account for no parameters passed
@app.route("/md5", methods=["GET"])
@app.route("/md5/", methods=["GET"])
@app.route("/md5/<path:data>", methods=["GET"])
def get_md5(data = ""):
    # Test cases to consider:
    # 1) What happens if a space is in the string passed? 
    # A: It is automatically converted to %20% in the browser
    # 2) What happens if the GET method is not used?
    # A: A 405 error is raised
    # 3) What happens if a non-string is passed?
    # A: It is still treated like a string and a md5 hash is returned
    # 4) What happens if a special character is passed?
    # A: It is passed as a string and a md5 hash of the special character is returned
    # 5) What happens if nothing is passed?
    # A: A JSON object is returned with {"md5_hash": null}
    # 6) What happens if a / is used in the middle of the string?
    # A: The / is treated as a string and the md5 hash is returned
    # 7) What happens if a / is present at the beginning of the argument?
    # A: 
    if data == "":
        md5_hash = None
    else:
        md5_hash = md5(data.encode()).hexdigest()
    return jsonify({"md5_hash": md5_hash}), 200

# @app.errorhandler(405)
# def method_not_allowed(error):
#     return "", 405
@app.route("/is-prime", methods=["GET"])
@app.route("/is-prime/", methods=["GET"])
@app.route("/is-prime/<path:data>", methods=["GET"])
def get_isprime(data = ""):
    primecheck = True
    if data == "":
        primenumber = None
        primecheck = "No input provided"
    else:
        primenumber = int(data)
        if primenumber > 1:
            for i in range(2, int(primenumber**0.5)+1 ):
                if primenumber % i == 0:
                    primecheck = False
                    break
                else:
                    primecheck = True
        else:
            primecheck = False
    return jsonify({"input:": primenumber, "output:" : primecheck}), 200






if __name__ == '__main__':
    app.run(debug=True)