def input_error_add_contact(func):
    def wrapper(*args, **kwargs):
        try:
            if len(args[0]) != 2:
                raise ValueError("You must provide both name and phone.")
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
    return wrapper

@input_error_add_contact
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."