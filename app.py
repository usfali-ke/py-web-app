from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is an Updated Flask App/site!!</p>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
    #app.run(host='0.0.0.0', port=9000)
