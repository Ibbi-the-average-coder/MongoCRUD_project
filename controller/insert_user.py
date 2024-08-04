from model.admin_model import customer_model

def main():
    admin_model = customer_model()

    name = input("Enter the user's name: ")
    email = input("Enter the user's email: ")
    number = input("Enter the user's phone number: ")
    password = input("Enter the user's password: ")

    try:
        number = int(number)
    except ValueError:
        print("Invalid number. Please enter numerical characters.")
        return

    data = {
        "name": name,
        "email": email,
        "number": int(number),
        "password": password
    }

    response = admin_model.user_addon_model(data)

    print(response)

if __name__ == "__main__":
    main()