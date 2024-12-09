def display_log_counts(counts: dict):
    headers = ["Рівень логування", "Кількість"]
    separator = "-" * 25

    print(f"{headers[0]:<18} | {headers[1]}")
    print(separator)
    
    for level, count in counts.items():
        print(f"{level:<18} | {count}")

