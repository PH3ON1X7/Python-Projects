# Password Manager - This program will encrypt the passwords and then store them.
# Performed by Ojaswin Khamkar

# If you have this key only then can you view the details in their original form
master_key = 'B3Nidict@123'


# Function to encrypt the data using Ceasar Cipher
def encrypt(data, shift):
    encrypted = ""

    for i in range(len(data)):
        char = data[i]

        if char.isupper():
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            encrypted += chr((ord(char) + shift - 97) % 26 + 97)

        elif char.isdigit():
            number = (int(char) + shift) % 10
            encrypted += str(number)

        else:
            encrypted += char

    return encrypted


# Function to decrypt the data
def decrypt(data, shift):
    decrypted = ""

    for i in range(len(data)):
        char = data[i]

        if char.isupper():
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)

        elif char.islower():
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)

        elif char.isdigit():
            number = (int(char) - shift) % 10
            decrypted += str(number)

        else:
            decrypted += char

    return decrypted


menu = ''
while menu != '1' or menu != '2':
    menu = input('What would you like to do? '
                 '\n1. Add a NEW password'
                 '\n2. VIEW existing passwords'
                 '\n3. Exit'
                 '\n--> ')

    # If user wants to enter new password
    if menu == '1':
        softwareName = input("\nEnter Software you are using: ")
        username = input("Enter Username: ")
        pwd = input("Enter Password: ")

        shift = 6
        with open('SecurePasswords.txt', 'a') as f:
            f.write(encrypt(softwareName, shift) + ' | ' +
                    encrypt(username, shift) + ' | ' + encrypt(pwd, shift) + '\n')

    # If user wants to view the existing passwords
    elif menu == '2':

        f = open("SecurePasswords.txt", 'r')
        validation = input("Enter the Master-Key: ")

        if validation == master_key:
            for line in f:
                shift = 6
                data = line.split('|')
                print('\nSoftware: ' + decrypt(data[0], shift) +
                      '\nUsername: ' + decrypt(data[1], shift) +
                      '\nPassword: ' + decrypt(data[2], shift))
            f.close()

        else:
            print("INCORRECT MASTER KEY!")

    # If user wants to quit
    elif menu == '3':
        print("THANK YOU for using the program.")
        break

    # Default menu
    else:
        print("INVALID CHOICE")
