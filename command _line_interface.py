def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if not len(args) < 2:
        name, phone = args
    else:
        return "Name and Phone Number is needed!"
    try:
        contacts[name] = phone
        return f'Contact {name} with phone number: {phone} added.'
    except:
        return 'Contact {name} with phone number: {phone} could not be added.'

def show_phone(args, contacts):
    text = ("{:.<15}{:<10}\n".format('Name', 'Phone Number'))
    name = args[0]
    try:
        phone = contacts[name]
        text += "{:.<15}{:<10}".format(name, phone)
        return text
    except:
        return f'There is no phone number for {name} saved'
    
def show_all(contacts):
    text = "{:.<15}{:<10}\n".format('Name', 'Phone Number')
    try:
        for key, value in contacts.items():
            text += ("{:.<15}{:<10}\n".format(key, value))
        return text
    except:
        return f'There are no phone number saved'
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
