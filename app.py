from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello ,world!"

@app.route("/hello1")
def hello_world1():
    return "hello ,world1!"

@app.route("/hello2")
def hello_world2():
    return "hello ,world2!"


@app.route("/test_fun")
def test():
    a = 5+6
    return "this my first fun in flask {}".format(a)

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)

if __name__ == "__main__" :
    app.run(host= "0.0.0.0")


