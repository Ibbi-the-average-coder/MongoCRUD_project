from app import app
from model.admin_model import user_model
from flask import request
obj = user_model()
@app.route("/user/readall", methods=["GET"])
def user_readall_controller():
    return obj.user_readall_model()

