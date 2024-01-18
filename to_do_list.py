import pprint
# pre-set to-do list database
to_do_list = {
    1: {
        "Title": "Gorceries",
        "Content": "Buy lettuce, ham, cheese and milk",
        "Deadline": "20 Jan"
    },
    2: {
        "Title": "Pay Bill",
        "Content": "Settle down the water and electricity bill",
        "Deadline": "End of each month"
    },
    3: {
        "Title": "Dental checking",
        "Content": "Regular check on my precious teeth",
        "Deadline": "Every three months"
    }
}

# Define a function for getting valid integer
def get_valid_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Define the function for the main programme
def to_do_prog():
    user_name = input("Hello, welcome to the to-do-list application.\nCan I ha\
ve your name please? ")
    print(f"Welcome, {user_name}. What would you like to do?")
    action = ""
    while action != "a" or "b" or "u" or "d" or "e":
        if len(to_do_list.keys()) == 1:
            print(f"\nWe now have {len(to_do_list.keys())} to-do item.")
        elif len(to_do_list.keys()) > 1:
            print(f"\nWe now have {len(to_do_list.keys())} to-do items.")
# Main menu
        print("""
(A)dding new to-do
(B)rowsing all to-do
(U)pdate to-do
(D)elete to-do
(E)xit the application
""")
        action = input("Please input an action code: A, B, U, D or E: \
").lower()
        if not action.isalpha(): # Check if input valid
            print("\nInput not valid, please enter an alphabet letter action c\
ode: A, B, U, D or E: ")
        elif len(action) > 1: # Check if input valid
            print("\nPlease enter 1 aplphabet letter action code: A, B, U, D o\
r E: ")
        elif action == "a": # Call add_to_do function, returning new to-do
            new_to_do = add_to_do(user_name)
            if new_to_do != None:
# If there are already some to-do exist, check any missing index
# Fill the new entry with the missing index, or index it with latest index + 1
                if len(to_do_list.keys()) != 0: 
                    for i in range(len(to_do_list.keys())):
                        if (i+1) not in to_do_list.keys():
                            new_to_do_index = (i+1)
                            break
                        new_to_do_index = (i+2)
# If no any index exist, index the new entry as no.1
                else:
                    new_to_do_index = 1
                to_do_list[new_to_do_index] = new_to_do 
        elif action == "b": # Call the respective function
            browse_to_do(user_name)
        elif action == "u":
            update_to_do(user_name)
        elif action == "d":
            delete_to_do(user_name)
        elif action == "e": # Exit programme
            print(f"Goodbye {user_name}!")
            return

# Define the function of sub-programme adding new to-do
def add_to_do(user_name):
    while True:
        # Ask for info input for the to-do
        title = input(f"\n{user_name}, please give the new to-do a title: ")
        content = input("Pleaes give me the content for the task: ")
        deadline = input("Please mark the dead line for the task: ")
        new_to_do = {
            "Title": title,
            "Content": content,
            "Deadline": deadline
        }
        print()
        print(f"Title: {new_to_do['Title']}")
        print(f"Content: {new_to_do['Content']}")
        print(f"Deadline: {new_to_do['Deadline']}")
        confirm = input(f"{user_name}, please confirm if the information is co\
rrect? Y or N: ").lower()
        if confirm == "y" or "yes":
            return new_to_do # Return the new entry
        else:
            again = input("\nWould you like to input again? Y or N: ").lower()
            if again == "n":
                return

# Define the function of sub-programme browsing to-do(s)
def browse_to_do(user_name):
    while True:
        print(f"{user_name}, we have {len(to_do_list)} tasks to do.")
# If no to-do exists, remind user and return to main menu
        if len(to_do_list) == 0:
            print("Oops, seems there is nothing we can look through at the mom\
ent! Time to input some. :P Going back to the main menu!")
            return
        for i in to_do_list: # Print out index and to-dos' title
            print(f"{i}: {to_do_list[i]['Title']}")
        print()
        choice = input("Which one you would like to check with?\nPlease input \
the number or input 'All'. ").lower()
        if choice == 'all':
            pprint.pprint(to_do_list, sort_dicts=False)
            finish_task = input("\nWould you like to countinue browsing? Pleas\
e input N to back to main menu. ").lower()
            if finish_task == "n":
                return
        else:
            for i in to_do_list:
                if choice == str(i):
                    pprint.pprint(to_do_list[i], sort_dicts=False)
            finish_task = input("\nWould you like to countinue browsing? Pleas\
e input N to back to main menu. ").lower()
            if finish_task == "n":
                return

# Define the function of sub-programme updating to-do(s)
def update_to_do(user_name):
    while True:
        print(f"{user_name}, we have {len(to_do_list)} tasks to do.")
# If no to-do exists, remind user and return to main menu
        if len(to_do_list) == 0:
            print("Oops, seems there is nothing we can update at the moment! T\
ime to input some for updating. :P Going back to the main menu!")
            return
        for i in to_do_list:
            print(f"{i}: {to_do_list[i]['Title']}")
        print()
        choice = get_valid_integer("Which one you would like to update with?\n\
Please input the number. ")
        if choice in to_do_list:
            for i in to_do_list:
                if choice == i:
                    pprint.pprint(to_do_list[i], sort_dicts=False)
            item_choice = input("Which item you would like to update, Title, C\
ontent or Deadline?\nPlease input T, C or D. Input E to back to main menu. \
").lower()
            if item_choice == "e":
                return
            elif item_choice == "t" or "c" or "d":
                new_content = input("Please input to update the item: ")
                if item_choice == "t":
                    to_do_list[choice]["Title"] = new_content
                elif item_choice == "c":
                    to_do_list[choice]["Content"] = new_content
                elif item_choice == "d":
                    to_do_list[choice]["Deadline"] = new_content
                pprint.pprint(to_do_list[choice], sort_dicts=False)
            finish_task = input("\nWould you like to countinue editing? Please\
 input N to back to main menu. ").lower()
            if finish_task == "n":
                return
        else:
            finish_task = input("\nWould you like to countinue editing? Please\
 input N to back to main menu. ").lower()
            if finish_task == "n":
                return

# Define the function of sub-programme deleting to-do(s)
def delete_to_do(user_name):
    while True:
        print(f"{user_name}, we have {len(to_do_list)} tasks to do.")
# If no to-do exists, remind user and return to main menu
        if len(to_do_list) == 0:
            print("Hooray! We have cleared all tasks! Time to input some new o\
ne. Going back to the main menu!")
            return
        for i in to_do_list:
            print(f"{i}: {to_do_list[i]['Title']}")
        print()
        choice = get_valid_integer("Which one you would like to delete?\nPleas\
e input the number. ")
        if choice in to_do_list:
            for i in to_do_list:
                if choice == i:
                    pprint.pprint(to_do_list[i], sort_dicts=False)
            del_choice = input("Are you sure to delete this entry? Y or N: \
").lower()
            if del_choice == "y":
                to_do_list.pop(choice)
                print(f"Now we have {len(to_do_list)} tasks to do.")
                for i in to_do_list:
                    print(f"{i}: {to_do_list[i]['Title']}")
                print()
                finish_task = input("\nWould you like to countinue deleting? P\
lease input N to back to main menu. ").lower()
                if finish_task == "n":
                    return
            else:
                finish_task = input("\nWould you like to countinue deleting? P\
lease input N to back to main menu. ").lower()
                if finish_task == "n":
                    return

# Run the programme
to_do_prog()
