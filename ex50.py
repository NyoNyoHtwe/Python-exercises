from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    greeting = "World"
    return f'Hello, {greeting}!'

if __name__ == "__name__":
    app.run()
