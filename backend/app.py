from flask import Flask,jsonify


app = Flask(__name__)

@app.route("/api/v1/users/control", methods = ['GET'])
def api_control():
    num = 1500
    data = {'data': num}

    return jsonify(data)

@app.route("/")
def index():
    return "Uygulama Calisiyor!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)