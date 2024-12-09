
def input_error_change_contact(func):
    def wrapper(*args, **kwargs):
        try:
            if(len(args[0]) != 2):
                raise ValueError("You must provide both name and phone.")
            name, _ = args[0]  
            contacts = args[1]  
            if name not in contacts:
                raise KeyError(f"Contact '{name}' not found.")
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: {e}"
    return wrapper


@input_error_change_contact
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."
