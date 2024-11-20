find_fullname = input("Enter a full name to search: ")

found = False

with open("./personal_information.txt", "r") as file_handle:
    data = file_handle.read()
    lines = data.split("\n\n")
    for line in lines:
        if find_fullname in line:
            print("Information found!")
        print(line.strip())