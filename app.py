from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "LW <a href=''>Hello, World</a>!!!!! <img src='https://sdfdgfhghy.blob.core.windows.net/mystttt/vimal_photo.jpg' />"
