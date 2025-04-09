
#initial commit
#Create a to do list (Kept on a txt file). Add items to the to do list. Mark item as complete. Delete item from to do list
# List to store To-Do items and their completion status
lst_todo = []
lst_complete = []

# Read existing to-do list data from file
with open("to_do_list/to_do_list.txt", "r") as file:
    txt_reader = file.read()  # Read entire file content
    temp_lst = txt_reader.split(",")  # Split into a list using commas

    # Populate the to-do and completion lists, skipping headers
    for i in range(2, len(temp_lst), 2):  
        lst_todo.append(temp_lst[i])
        lst_complete.append(temp_lst[i+1])

# Function to save the current To-Do list to file
def save_item():
    temp_lst = ["item", "completed?"]  # Header for the file
    for i in range(len(lst_todo)):
        temp_lst.append(lst_todo[i])  # Add task name
        temp_lst.append(lst_complete[i])  # Add completion status
    
    # Convert list back into a comma-separated string
    uploading = ",".join(temp_lst)  
    
    # Write to the file
    with open("to_do_list/to_do_list.txt", "w") as file:
        file.write(uploading)

    print("\n\nTo-Do list saved successfully.")

# Function to display the current To-Do list
def view_item():
    for i in range(len(lst_todo)):
        print(f"{i+1} - {lst_todo[i]} is {lst_complete[i]}")  # Display tasks with their status

# Function to add a new task to the To-Do list
def add_todo():
    while True:
        add_item = input("What is the name of the item you want to add to the To-Do list? ")
        
        # Prevent commas in task names (since the file format is CSV-like)
        if "," in add_item:
            print("Please, no commas.")
        else:
            break  # Valid input received
    
    lst_todo.append(add_item)  # Add new task
    lst_complete.append("Incomplete")  # Default status is "Incomplete"
    
    save_item()  # Save the updated list
    view_item()  # Show the updated list

# Function to mark an item as "Complete" or toggle its status
def complete():
    print("\nWhich would you like to toggle as completed?")
    
    # Display all tasks with their current status
    for i in range(len(lst_todo)):
        print(f"({i+1}) - {lst_todo[i]}, {lst_complete[i]}")
    
    # Add an exit option
    print(f"({len(lst_todo)+1}) - Exit to main menu")

    while True:
        try:
            select = int(input("\nPlease type the number corresponding to your selection: "))
            
            # Validate user input
            if select < 1 or select > len(lst_todo) + 1:
                print(f"Please only enter a number 1-{len(lst_todo)+1}")
            elif select == len(lst_todo) + 1:  # Exit option
                return
            else:
                break  # Valid selection made
        except ValueError:
            print("Please only enter a whole number.")

    # Toggle between "Complete" and "Incomplete"
    if lst_complete[select-1] == "Incomplete":
        lst_complete[select-1] = "Complete"
    else:
        lst_complete[select-1] = "Incomplete"

    save_item()  # Save changes
    view_item()  # Show updated list

# Function to delete an item from the To-Do list
def delete_item():
    print("\nWhich item would you like to delete?")
    
    # Display current tasks
    for i in range(len(lst_todo)):
        print(f"({i+1}) - {lst_todo[i]}, {lst_complete[i]}")
    
    # Add an exit option
    print(f"({len(lst_todo)+1}) - Exit to main menu")

    while True:
        try:
            select = int(input("\nPlease type the number corresponding to your selection: "))
            
            # Validate input
            if select < 1 or select > len(lst_todo) + 1:
                print(f"Please only enter a number 1-{len(lst_todo)+1}")
            elif select == len(lst_todo) + 1:  # Exit option
                return
            else:
                break  # Valid selection made
        except ValueError:
            print("Please only enter a whole number.")

    # Remove the selected task
    del lst_todo[select-1]
    del lst_complete[select-1]

    save_item()  # Save changes
    view_item()  # Show updated list

# Main function to run the To-Do list program
def main():
    while True:
        try:
            # Display menu options
            selection = int(input("\nPlease make your selection\n"
                                  "(1) View To-Do List\n"
                                  "(2) Add Item to To-Do List\n"
                                  "(3) Mark Item as Complete\n"
                                  "(4) Delete Item from To-Do List\n"
                                  "(5) Save and exit\n\n"
                                  "Please type the number corresponding to your selection: "))

            # Process user selection
            if selection == 1:
                view_item()
            elif selection == 2:
                add_todo()
            elif selection == 3:
                complete()
            elif selection == 4:
                if len(lst_todo) <= 1:
                    print("You need to have more than 1 item in your To-Do list to delete an item.")
                else:
                    delete_item()
            elif selection == 5:
                print("Thank you for using our To-Do list manager, come again soon.")
                save_item()
                break  # Exit the program
            else:
                print("Please only enter a number 1-5")
        except ValueError:
            print("Please only enter a whole number.")

# Run the program
#main()
