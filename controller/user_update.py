from model.admin_model import user_model

def main():
    admin_model = user_model()

    user_id = input("Enter the user's ID to update: ")
    name = input("Enter the new name: ")
    age = input("Enter the new age: ")
    number = input("Enter the new number")
    password = input("Enter the new password")

    try:
        age = int(age)
        number = int(number)
    except ValueError:
        print("Invalid type for age or number. Please enter in numerical format.")
        return

    update_data = {
        "name": name,
        "age": age,
        "number": number,
        "password": password
    }

    response = admin_model.user_update_model(user_id, update_data)

    print(response)

if __name__ == "__main__":
    main()



