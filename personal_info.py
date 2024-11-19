while True:
    full_name = input("Enter your name: ")
    age = (input("Enter your age: "))
    birthday = input("Enter date of birth: ")
    address = input("Enter your address: ")
    number = (input("Enter your phone number: "))
    email = input("Enter your email address: ")

    another_entry = input("Do you want another entry? (YES/NO): ")

    if another_entry.lower() == 'no':
        break

with open("./personal_info.txt", "a") as file_handle:
    file_handle.write(input("Enter your full name: "))
    file_handle.write(input("Enter your age: "))
    file_handle.write(input("Enter your date of birth: "))
    file_handle.write(input("Enter your address: "))
    file_handle.write(input("Enter your mobile number: "))
    file_handle.write(input("Enter your e-mail address: "))