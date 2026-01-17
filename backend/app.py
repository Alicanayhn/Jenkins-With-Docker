from flask import Flask, jsonify


app = Flask(__name__)


# API endpoint to return a JSON response with a numeric values
@app.route("/api/v1/users/control", methods=["GET"])
def api_control():
    num = 1500
    data = {"data": num}
    print(type(data))
    return jsonify(data)


# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return "OK", 200


# Readiness check endpoint
@app.route("/ready", methods=["GET"])
def readiness_check():
    return "READY", 200


# CREATE a simple route to test if the application is running
@app.route("/test", methods=["GET"])
def test():
    return "Application is running", 200


# Simple route for the root URL
@app.route("/")
def index():
    return "Uygulama Calisiyor!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
