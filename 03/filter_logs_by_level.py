error_type = {
   "info": "INFO",
   "debug": "DEBUG",
   "error": "ERROR",
   "warning": "WARNING"
}


def filter_logs_by_level(logs, error):
    if error in error_type:
       filtered_logs = list(filter(lambda x: x["log"] == error_type[error], logs))
       print(f"Деталі логів для рівня {error_type[error]}:")
       for item  in filtered_logs:
            print(f"{item["date"]} {item["time"]} - {item["message"]}")
    else:
        print(f"Error type: {error}  is not exist")
   