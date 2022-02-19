# Password Manager by Ojaswin Khamkar

# Function for viewing the existing passwords
def view():

    with open('passwords.txt', 'r') as f:

        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User:', user, '| Password:', passw)


# Function for adding new passwords
def newpwd():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # If 'with' is used you don't need to close the file manually, Python does it for you.
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + pwd + '\n')


while True:

    print('''What would you like to do?
1. Add NEW password.
2. View EXISTING passwords.
3. Quit''')
    ch = int(input())

    # If user wants to quit the program
    if ch == 3:
        print("Thank You, for using the program.")
        break

    # If user wants to add a new password
    if ch == 1:
        newpwd()

    # If user wants to view the existing passwords
    elif ch == 2:
        view()

    # Default Case
    else:
        print("INVALID CHOICE")
        continue
