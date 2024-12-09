
def input_error_show_phone(func):
    def wrapper(*args, **kwargs):
        name = args[0] 
        try:
            if(len(name) == 0):
                raise ValueError("You must provide name.")
             
            contacts = args[1]  
            if name not in contacts:
                raise KeyError(f"Contact '{name}' not found.")
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Error: {e}"
    return wrapper
@input_error_show_phone
def show_phone(name, contacts):
     return contacts[name]