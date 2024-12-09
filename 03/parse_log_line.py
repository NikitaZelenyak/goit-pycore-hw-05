def parse_log_line(line):
    data_holder = {"date": "", "time": "", "log": "", "message": ""}
    parts = line.split(" ", 3)  
    data_holder["date"] = parts[0] if len(parts) > 0 else ""
    data_holder["time"] = parts[1] if len(parts) > 1 else ""
    data_holder["log"] = parts[2] if len(parts) > 2 else ""
    data_holder["message"] = parts[3].replace("\n", "") if len(parts) > 3 else ""

    return data_holder

    