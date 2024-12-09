import sys
from load_logs import load_logs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, надайте шлях до директорії як аргумент.")
    else:
        print(sys.argv)
        directory_path = sys.argv[1]
        error_type = sys.argv[2] if len(sys.argv) >= 3 else ""
        load_logs(directory_path, error_type)