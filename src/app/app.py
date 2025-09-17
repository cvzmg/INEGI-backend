from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def mainPage():
    return "Main Page!"
@app.route("/hello-world", methods=["GET"])
def helloWorld():
    return "hello world!"
@app.route('/process', methods=['POST'])
def process():
    # Get JSON data from request
    data = request.get_json()
    # Example: add a message to the received data
    response = {
        "received": data.get('name'),
        "message": "JSON received successfully!"
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)