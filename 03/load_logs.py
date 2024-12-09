from pathlib import Path
from read_file import read_data
from parse_log_line import parse_log_line
from count_logs_by_level import count_logs_by_level
from display_log_counts import display_log_counts
from filter_logs_by_level import filter_logs_by_level

def load_logs(p, error= ""):
    logs_list = []
    *args, fileName = p.split("/")
    path = Path(*args)
    if not path.exists():
        print("Path is not exist")
    else:
         res = read_data(path, fileName)
         for line in res:
            res = parse_log_line(line)
            logs_list.append(res)
    res = count_logs_by_level(logs_list)
    display_log_counts(res)
    if len(error):
        filter_logs_by_level(logs_list, error)
    
 


         

