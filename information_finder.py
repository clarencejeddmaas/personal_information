find_fullname = input("Enter a full name to search: ")

found = False

with open("./personal_information.txt", "r") as file_handle:
    lines = file_handle.readlines()
    for line in lines: 
        print(line.strip())