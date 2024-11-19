while True:
    full_name = input("Enter your name: ")
    age = (input("Enter your age: "))
    birthday = input("Enter date of birth: ")
    address = input("Enter your address: ")
    number = (input("Enter your phone number: "))
    email = input("Enter your email address: ")

    with open("./personal_information.txt", "a") as file_handle:
