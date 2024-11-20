# start using while loop
# set variable for a specific type of information for a user to input, such as full name, age, date of birth, address, phone number, and email address
# ask user to input full name, age, date of birth, address, phone number, and email address, then store it
# open "personal_info.txt" in append method
# write the full name, age, address, phone number, and email address with proper label and newlines
# ask user if it wants to input another entry
# if the user enters 'yes', the program will ask the user again for another input
# if the user enters 'no', the loop will break out

while True:
    full_name = input("Enter your full name: ")
    age = (input("Enter your age: "))
    birthday = input("Enter date of birth (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    number = (input("Enter your phone number: "))
    email = input("Enter your email address: ")

    with open("./personal_information.txt", "a") as file_handle:
        file_handle.write("\nPersonal Information\n")
        file_handle.write(f"\nName: {full_name}\n")
        file_handle.write(f"Age: {age}\n")
        file_handle.write(f"Date of Birth: {birthday}\n")
        file_handle.write(f"Address: {address}\n")
        file_handle.write(f"Phone Number: {number}\n")
        file_handle.write(f"E-mail address: {email}\n")

    another_entry = input("Do you want another entry? (YES/NO): ")

    if another_entry.lower() == 'no':
        break

