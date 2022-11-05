import os

from utils import filter_from_params, map_from_value, unique, sort_query, limit_qeury

file = "data/apache_logs.txt"

command_for_func = {
    "filter": filter_from_params,
    "map": map_from_value,
    "unique": unique,
    "sorted": sort_query,
    "limit": limit_qeury

}


# файловый дискриптор
def open_logs(filename):
    with open(filename) as file:
        for row in file:
            yield row


def main_query(cmd, value, res):
    if res is None:
        f = open_logs(file)
    else:
        f = res
    result = command_for_func[cmd](param=value, data=f)
    return list(result)
