while True:
    full_name = input("Enter your name: ")
    age = (input("Enter your age: "))
    birthday = input("Enter date of birth: ")
    address = input("Enter your address: ")
    number = (input("Enter your phone number: "))
    email = input("Enter your email address: ")

    with open("./personal_information.txt", "a") as file_handle:
        file_handle.write("\nPersonal Information\n")
        file_handle.write(f"Name: {full_name}\n")
        file_handle.write(f"Age: {age}\n")
        file_handle.write(f"Date of Birth: {birthday}\n")
        file_handle.write(f"Address: {address}\n")
        file_handle.write(f"Phone Number: {number}\n")
        file_handle.write(f"E-mail address: {email}\n")

    another_entry = input("Do you want another entry? (YES/NO): ")

    if another_entry.lower() == 'no':
        break

