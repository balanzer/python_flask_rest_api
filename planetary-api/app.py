from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!.'


@app.route("/super_simple")
def super_simple():
    data = [1, 2, 3, 4];
    return jsonify(content=data)


# http://127.0.0.1:5000/parameter?age=110&name=Murali

@app.route("/parameter")
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + " you are not authorized."), 401
    else:
        return jsonify(message="Hello " + name + " you are authorized."), 200


# http://127.0.0.1:5000/url_variable/m/19

@app.route("/url_variable/<string:name>/<int:age>")
def url_variable(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + " you are not authorized."), 401
    else:
        return jsonify(message="Hello " + name + " you are authorized."), 200


if __name__ == '__main__':
    app.run()
