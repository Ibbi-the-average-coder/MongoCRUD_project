from app import app
from flask import Flask, request, jsonify
from model.admin_model import customer_model

obj = customer_model()

@app.route("/user/addon", methods=["POST"])
def user_addon_controller():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"})
    return obj.user_addon_model(data)


