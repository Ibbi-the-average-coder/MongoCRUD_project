from pymongo import MongoClient
from flask import jsonify
from bson import ObjectId
from controller import delete_user, user_update, insert_user


class base_model:
    def __init__(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client.flask_project
            print("Connection Successful")
        except Exception as e:
            print(f"Some error occurred: {e}")


class user_model(base_model):
    def __init__(self):
        super().__init__()
        self.collection = self.db.Users

    def user_readall_model(self):
        try:
            documents = self.collection.find()
            result = list(documents)
            if not result:
                print("No documents found in the collection.")
            for document in result:
                document['_id'] = str(document['_id'])
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while retrieving data: {e}")
            return jsonify({"error": "An error occurred while retrieving data."})

    def user_update_model(self, user_id, update_data):
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(user_id)},
                {'$set': update_data}
            )
            if result.modified_count == 1:
                return {"status": "Data updated successfully"}
            else:
                return {"status": "No data was updated, check the provided ID"}
        except Exception as e:
            print(f"An error occurred while updating data: {e}")
            return {"error": "An error occurred while updating data."}

    def user_delete_model(self):
        try:
            delete_user.user_delete_model(self)
            return "successful call"

        except:
            return "unsuccessful call"


class customer_model(base_model):
    def __init__(self):
        super().__init__()
        self.collection = self.db.Users

    def user_addon_model(self, data):
        try:
            result = self.collection.insert_one(data)
            inserted_id = str(result.inserted_id)
            return {"status": "Data inserted", "id": inserted_id}
        except Exception as e:
            print(f"An error occurred while inserting data: {e}")
            return {"error": "An error occurred while inserting data."}
