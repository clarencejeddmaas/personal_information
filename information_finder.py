# 1. Start with while loop to search multiple names.
# 2. Initialize a found flag.
# 3. Open the file in read mode.
# 4. Read the entire file content.
# 5. Split file content in double newline.
# 6. Use for loop for each line.
# 7. Check if the full name was found in the line.
# 8. If the full name was in the line, print the information found.
# 9. Update the found flag into True, and exit the loop.
# 10. Print a message if no information was found.
# 11. Ask the user if it wants to search another full name.
# 12. If the user type 'no', the program will print an exit.

while True:
    find_fullname = input("Enter a full name to search: ")

    found = False

    with open("./personal_information.txt", "r") as file_handle:
        data = file_handle.read()
        lines = data.split("\n\n")
        for line in lines:
            if find_fullname in line:
                print("Information found!")
                print(line.strip())
                
                found = True 

                break

    if not found:
        print(f"No information found for {find_fullname}.")

    another_search = input("\nDo you want another search? (YES/NO): ")
    if another_search.lower() == "no":
        print("Program exiting. Thank you.")
