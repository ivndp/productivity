import datetime  # import datetime for compare date and date entry
import os  # import os for checking file

task_dict = {}
# creating dictionary for storing task data
if not os.path.exists("task.txt"):
    with open("task.txt", "w") as default_file:
        pass

with open("task.txt", "r") as file:
    for line in file:
        data = line.strip("\n").split("|")
        task_dict[int(data[0])] = [
            data[1], data[2], data[3], data[4], data[5], data[6]
        ]

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    user_p = user.split(";")
    username = user_p[0]
    username_password[user_p[0]] = user_p[1]


# define function for registering user name
def reg_user():
    while True:
        new_user = input("New username: ")
        if new_user in username_password.keys():
            print("User already exist.")
            return
        new_password = input("Password for the user:")
        confirm_password = input("Confirm password: ")
        if new_password == confirm_password:
            with open("user.txt", "a+") as file:
                file.write("\n" + new_user + ";" + new_password)
            print(f"Username {new_user} have been registered!")
            return
        else:
            print("Password not match, please try again.")


# define a function to check if username input exist in the username file
def check_user(prompt):
    while True:
        user = input(prompt)
        if not user in username_password.keys():
            print("User not registered. Please input a username registered.")
        else:
            return user


# define function for adding new task
def add_task():
    while True:
        # Ask for input for the task
        title = input(f"\nPlease give the new task a title: ")
        assigned_to = check_user("Whom would this task be assigned to: ")
        content = input("Could give me the description for the task: ")
        deadline = input("Please mark the due date for the task(YYYY-MM-DD): ")
        serial_no = list(task_dict.keys())[-1]+1
        date_assigned = datetime.date.today()
        task_complete = "No"
# print the info out for user to confirm if it is correct
        print(f"""
-------------------------------------------------------------------------------
Serial no.:                 {serial_no}
Task:                       {title}
Assigned to:                {assigned_to}
Date assigned:              {date_assigned}
Due date:                   {deadline}
Task completed?             {task_complete}
Task description:
    {content}
-------------------------------------------------------------------------------
""")
        confirm = input(f"Please confirm if the information is correct? Y or N\
: ").lower()
# if correct, add it into the task dictionary, and use the dictionary to
# rewrite the task text file
        if confirm == "y":
            task_dict[serial_no] = [
                title, assigned_to, date_assigned, deadline, task_complete,
                content
            ]
            with open("task.txt", "w+") as file:
                for key, value in task_dict.items():
                    file.write(f"{key}|{value[0]}|{value[1]}|{value[2]}|\
{value[3]}|{value[4]}|{value[5]}\n")
            print("Task recorded!")
            return
# if not correct, ask user would like to start again
        else:
            again = input("\nWould you like to input again? Y or N: ").lower()
            if again == "n":
                return


# define function to view all tasks at once
def view_all():
    print("Here are all the tasks recorded:")
    for key, value in task_dict.items():
        print(f"""
-------------------------------------------------------------------------------
Serial no.:                 {key}
Task:                       {value[0]}
Assigned to:                {value[1]}
Date assigned:              {value[2]}
Due date:                   {value[3]}
Task completed?             {value[4]}
Task description:
    {value[5]}
-------------------------------------------------------------------------------
""")
    return


# define function to view tasks that is assigned to the user name using
def view_mine(user_name):
# setup a for loop to check if there is any task assigned to the user name
    no_task_for_user = True
    for value in task_dict.values():
        if user_name == value[1]:
            no_task_for_user = False
# if no task assgined yet, tell the user to assign new task and go back to main
# menu
    if no_task_for_user:
        print(f"""
Sorry {user_name}, no task have been assigned for you at the moment.
You could assign some choosing \"Add a new task\" at the main menu.
Going back to main menu now.

""")
        return
# countinue to the loop for printing brief view of tasks assigned to the user 
    while True:
        task_no = []
        task_list = ""
        for key, value in task_dict.items():
            if value[1] == user_name:
                task_list += f"{key}  ------  {value[0]}\n"
                task_no.append(key)
        print(f"Here is all the task assigned to {user_name}:")
        print(task_list)
# ask user to choose a task to view in detail or go back to main menu
        choice = get_valid_integer("\nPlease input the task number or -1 to re\
turn to main menu. ")
        if choice == -1:
            return
# print out the task in detail and ask user if they want to edit it
        elif choice in task_no:
            print(f"""

-------------------------------------------------------------------------------
Serial no.:                 {choice}
Task:                       {task_dict[choice][0]}
Assigned to:                {task_dict[choice][1]}
Date assigned:              {task_dict[choice][2]}
Due date:                   {task_dict[choice][3]}
Task completed?             {task_dict[choice][4]}
Task description:
    {task_dict[choice][5]}
-------------------------------------------------------------------------------
""")
            while True:
                in_choice = input("""
Would you like to (e)dit the task, (m)ark the task as completed or (b)ack to v\
iew tasks? E, M or B: 
""").lower()
                if in_choice == "e" and task_dict[choice][4] == "No":
# use while loop to ask for what item to edit and the content to be updated
                    while True:
                        edit_choice = get_valid_integer(f"""
Which item you would like to edit?
Please input the number:
1 ----------- Task:          {task_dict[choice][0]}
2 ----------- Assigned to:   {task_dict[choice][1]}
3 ----------- Due date:      {task_dict[choice][3]}
4 ----------- Task description:
    {task_dict[choice][5]}
""")
                        edit_content = input("Please input the updated content\
: ")
                        if edit_choice == 1:
                            print(f"""
Task:                       {edit_content}
""")
                            confirm = input("Is this correct? Y or N ").lower()
                            if confirm == "y":
                                task_dict[choice][0] = edit_content
                                with open("task.txt", "w+") as file:
                                    for key, value in task_dict.items():
                                        file.write(f"{key}|{value[0]}|\
{value[1]}|{value[2]}|{value[3]}|{value[4]}|{value[5]}\n")
                                print("Task updated!")
                                break
                            else:
                                print("Okay, back to edit menu.")
                        elif edit_choice == 2:
                            print(f"""
Assigned to:                {edit_content}
""")
                            confirm = input("Is this correct? Y or N ").lower()
                            if confirm == "y":
                                task_dict[choice][1] = edit_content
                                with open("task.txt", "w+") as file:
                                    for key, value in task_dict.items():
                                        file.write(f"{key}|{value[0]}|\
{value[1]}|{value[2]}|{value[3]}|{value[4]}|{value[5]}\n")
                                print("Task updated!")
                                break
                            else:
                                print("Okay, back to edit menu.")
                        elif edit_choice == 3:
                            print(f"""
Due date:                   {edit_content}
""")
                            confirm = input("Is this correct? Y or N ").lower()
                            if confirm == "y":
                                task_dict[choice][3] = edit_content
                                with open("task.txt", "w+") as file:
                                    for key, value in task_dict.items():
                                        file.write(f"{key}|{value[0]}|\
{value[1]}|{value[2]}|{value[3]}|{value[4]}|{value[5]}\n")
                                print("Task updated!")
                                break
                            else:
                                print("Okay, back to edit menu.")
                        elif edit_choice == 4:
                            print(f"""
Task description:
    {edit_content}
""")
                            confirm = input("Is this correct? Y or N ").lower()
                            if confirm == "y":
                                task_dict[choice][5] = edit_content
                                with open("task.txt", "w+") as file:
                                    for key, value in task_dict.items():
                                        file.write(f"{key}|{value[0]}|\
{value[1]}|{value[2]}|{value[3]}|{value[4]}|{value[5]}\n")
                                print("Task updated!")
                                break
                            else:
                                print("Okay, back to edit menu.")
                elif in_choice == "e" and task_dict[choice][4] == "Yes":
# if task is completed, tell user not accept further edition
                    print("Sorry, the task is completed, could not be edited.")
                elif in_choice == "m":
                    task_dict[choice][4] = "Yes"
                    with open("task.txt", "w+") as file:
                        for key, value in task_dict.items():
                            file.write(f"{key}|{value[0]}|{value[1]}|\
{value[2]}|{value[3]}|{value[4]}|{value[5]}\n")
                    print("Task updated!")
                    break
                elif in_choice == "b":
                    break


# define function to generate reports regarding tasks and users
def generate_report():
# setup variables to be used in the report
    task_generated = 0
    completed_task = 0
    uncompleted_task = 0
    overdue_task = 0
    user_no = 0
    user_task_dict = {}
    try:
# user try-except to avoid error of no task file created before
        with open("task.txt", "r") as file:
            for line in file:
                data = line.strip("\n").split("|")
                if data[5] == "Yes":
                    completed_task += 1
                elif data[5] == "No":
                    uncompleted_task += 1
                    deadline = datetime.datetime.strptime\
(data[4], "%Y-%m-%d").date()
                    today = datetime.date.today()
                    if today > deadline:
                        overdue_task += 1
                if int(data[0]) > task_generated:
                    task_generated = int(data[0])
    except FileNotFoundError:
        print("No task have been recorded yet.")
# no try-except here as only admin could use report-generate action
# not quite possible to be here if the user is not admin or no exist
# user name data file
    with open("user.txt", "r") as file:
        for line in file:
            user_no += 1
            user = line.strip("\n").split(";")
            for key, value in task_dict.items():
                user_task = 0
                user_task_completed = 0
                user_task_uncompleted = 0
                user_overdue_task = 0
                if value[1] == user[0]:
                    user_task += 1
                    if value[4] == "Yes":
                        user_task_completed += 1
                    elif value[4] == "No":
                        user_task_uncompleted += 1
                        deadline = datetime.datetime.strptime\
(value[3], "%Y-%m-%d").date()
                        today = datetime.date.today()
                        if today > deadline:
                            user_overdue_task += 1
                    if not user[0] in user_task_dict.keys():
                        user_task_dict[user[0]] = [
                            user_task, user_task_completed,
                            user_task_uncompleted, user_overdue_task
                        ]
                    elif user[0] in user_task_dict.keys():
                        user_task_dict[user[0]][0] += user_task
                        user_task_dict[user[0]][1] += user_task_completed
                        user_task_dict[user[0]][2] += user_task_uncompleted
                        user_task_dict[user[0]][3] += user_overdue_task
# collected all data needed in the report
# start writing data into report 
    with open("task_overview.txt", "w") as file:
        file.write(f"""
Total number of tasks have been generated: {task_generated}
Total number of completed tasks: {completed_task}
Total number of incompleted tasks: {uncompleted_task}
Total number of incompleted and overdue tasks: {overdue_task}
Incompleted tasks percentage: {percentage(uncompleted_task, task_generated)}
Overdue tasks percentage: {percentage(overdue_task, task_generated)}
""")
    print("Generated report - task_overview.txt")
    with open("user_overview.txt", "w") as file:
        file.write(f"Total number of users registered: {user_no}")
        for key, value in user_task_dict.items():
            file.write(f"""
-------------------------------------------------------------------------------
User: {key}
Total number assigned to {key}: {value[0]}
Percentage of number of task assigned over total number of tasks: \
{percentage(value[0], task_generated)}
Percentage of completed tasks over tasks assigned: \
{percentage(value[1], value[0])}
Percentage of incompleted tasks over tasks assigned: \
{percentage(value[2], value[0])}
Percentage of overdue tasks over tasks assigned: \
{percentage(value[3], value[0])}
-------------------------------------------------------------------------------
""")
    print("Generated report - user_overview.txt")
    return


# define function to display data inside overview report
def display_stat():
    try:
# use try-except to create reports to display if there isn't any report 
# generated before
        with open("task_overview.txt", "r") as file:
            print(file.read())
        with open("user_overview.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        generate_report()
        with open("task_overview.txt", "r") as file:
            print(file.read())
        with open("user_overview.txt", "r") as file:
            print(file.read())
    return


# define function to calculate percentage
def percentage(part, whole):
    percentage = round(part/whole * 100)
    return str(percentage) + "%"


# define function to get valid integer input
def get_valid_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Define the function for the main programme
def main():
    logged_in = False
    while not logged_in:
        print("LOGIN")
        curr_user = input("Username: ")
        curr_pass = input("Password: ")
        if curr_user not in username_password.keys():
            print("User does not exist")
            continue
        elif username_password[curr_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True
    print(f"Hello {curr_user}, welcome to the Task Manager.")
    print("What would you like to do?")
    while True:
# Main menu
        print("""
(R)egister a new user
(A)dd a new task
(V)iew (A)ll tasks
(V)iew (M)y tasks
(G)enerate (R)eports
(D)isplay (S)tatistics
(E)xit the application
""")
        action = input("Please input an action code(R, A, VA, VM, GR, DS or E)\
: ").lower()
        if not action.isalpha():  # Check if input valid
            print("\nInput not valid, please enter an alphabet letter action c\
ode(R, A, VA, VM, GR, DS or E): ")
        elif len(action) > 2:  # Check if input valid
            print("\nPlease enter aplphabet letter action code(R, A, VA, VM, G\
R, DS or E): ")
        elif action == "r":  # call reg_user function
            reg_user()
        elif action == "a":  # Call add_task function
            add_task()
        elif action == "va":  # Call view_all function
            view_all()
        elif action == "vm":  # Call view_mine function
            view_mine(curr_user)
        elif action == "gr":
            if curr_user == "admin":  # call generate_report function
                generate_report()
            else:
                print("The action is limited to admin only.")
                print("Please select another action.")
        elif action == "ds":
            if curr_user == "admin":  # call display_stat function
                display_stat()
            else:
                print("The action is limited to admin only.")
                print("Please select another action.")
        elif action == "e":  # Exit programme
            print(f"Goodbye {curr_user}. See you next time.")
            return


main()
