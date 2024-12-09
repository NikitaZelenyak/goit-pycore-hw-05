from collections import Counter
def count_logs_by_level(logs_list):
    log_levels = (item["log"] for item in logs_list)
    return dict(Counter(log_levels))