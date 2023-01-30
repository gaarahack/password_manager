import getpass

passwords ={}

def create_passwords(website,password):
    passwords[website] = password
    print(f"Password for {website} is created succefully")

def get_password(website):
    try:
        return passwords[website]    
    except KeyError:
        return "Password for this website is not found"

running = True

while running:
    print("Welcome to the password manager")
    print("1. create a password for a website")
    print("2. Know your created password")
    print("3. Quit")

    choice = int(input("Enter the option: "))

    if choice == 1:
        website = input("Enter the name of the website: ")
        password = input("Enter the password for the website")
        create_passwords(website,password)

    if choice == 2:
        website = input("Enter the name of the website: ")
        print(f"Password: {get_password(website)}")

    if choice == 3:
        running =False
        exit()
