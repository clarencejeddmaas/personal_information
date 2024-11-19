while True:
    
with open("./personal_info.txt", "w") as file_handle:
    file_handle.write(input("Enter your full name: "))
    file_handle.write(input("Enter your age: "))
    file_handle.write(input("Enter your date of birth: "))
    file_handle.write(input("Enter your address: "))
    file_handle.write(input("Enter your mobile number: "))
    file_handle.write(input("Enter your e-mail address: "))