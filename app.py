from flask import Flask
from Controller.ProductController import PdtController

app = Flask(__name__)
app.register_blueprint(PdtController)

@app.route("/home")
def hello_world():
    return "<h1>Hello, world!</h1>"
