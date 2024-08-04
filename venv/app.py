from flask import Flask, jsonify
from model.admin_model import user_model
from model.admin_model import customer_model
import admin_model


app = Flask(__name__)

@app.route("/")
def welcome():
    admin_model.user_update_model()

@app.route("/home")
def home():
    return "This is home page"


from controller import *


if __name__ == '__main__':
    app.run(debug=True)