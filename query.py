from typing import Dict, Callable, Generator, Union, Iterable, Optional
from utils import filter_from_params, map_from_value, unique, sort_query, limit_qeury, find_regex

file: str = "data/apache_logs.txt"

command_for_func: Dict[str, Callable] = {
    "filter": filter_from_params,
    "map": map_from_value,
    "unique": unique,
    "sorted": sort_query,
    "limit": limit_qeury,
    "regex": find_regex

}


# файловый дискриптор
def open_logs(filename: str) -> Generator[str, None, None]:
    """Генератор чтения файла построчно"""

    with open(filename) as file:
        yield from file


def main_query(cmd: str, value: Union[str, int], res: Optional[Iterable[str]]) -> list[str]:
    if res is None:
        f = open_logs(file)
    else:
        f = res
    result = command_for_func[cmd](param=value, data=f)
    return list(result)
