from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is Chinna's python project running on Docker using jenkins !!"
