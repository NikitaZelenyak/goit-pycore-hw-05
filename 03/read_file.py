
def read_data(dir, filename):
    try:
        with open(dir / filename, "r") as file:
            return file.readlines()
    except:
        return "Something went wrong" 