from model.admin_model import user_model

from bson import ObjectId


def user_delete_model(self):
    try:
        user_id = input("Enter the user's ID to delete: ")
        result = self.collection.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            return {"status": "Data deleted successfully"}
        else:
            return {"status": "No data was deleted, check the provided ID"}
    except Exception as e:
        print(f"An error occurred while deleting data: {e}")
        return {"error": "An error occurred while deleting data."}

