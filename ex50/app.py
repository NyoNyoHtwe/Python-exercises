from flask import Flask
from flask import render_templates

app = Flask(__name__)

@app.route("/")
def index():
    greenting = "Hello World"
    return render_templates("index.html", greenting=greenting)

if __name__ == "__main__":
    app.run()

