import getpass

passwords = {}

def create_password(website,password):
    passwords[website] = password
    print(f"Password created successfully for {website}")

def get_password(website):
    try:
        return passwords[website]
    except KeyError:
        return "Can't find the password for the given website"

running =True

while running:
    print("1 Create a password for the website")
    print('2. Get password which are already stored')
    print("3 Quit")

    choice =int(input("Enter any option: "))

    if choice == 1:
        website = input("Enter the name of the website: ")
        password = getpass.getpass("Enter the password: ")
        create_password(website,password)

    if choice == 2:
        website = input("Enter the name of the website: ")
        print(f"Password: {get_password(website)}")

    if choice == 3:
        running = False
        exit()    
