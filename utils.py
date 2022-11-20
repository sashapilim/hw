import re
from typing import Iterable, Iterator, Set, Any, List,Match


def filter_from_params(param: str, data: Iterable[str]) -> Iterator[str]:
    return filter(lambda x: param in x, data)


def map_from_value(param, data: Iterable[str]) -> Iterator[str]:
    param: int = int(param)
    return map(lambda x: x.split(" ")[param], data)


# в случае если она может принять именнованные и позиционные арг
def unique(data, *args, **kwargs):
    return set(data)


def sort_query(param: str, data: Iterable[str]) -> List[str]:
    return sorted(data, reverse=param == "desc")


def limit_qeury(param: str, data: Iterable[str]) -> List[str]:
    limit: int = int(param)
    return list(data)[:limit]


def find_regex(param: str, data: Iterable[str]) -> Iterator[str]:
    regex = re.compile(fr"{param}")
    return filter(lambda x: regex.search(x), data)


# {"qeuries": [
#     {
#         "cmd": "filter",
#         "value": "POST"},
#     {
#         "cmd": "limit",
#         "value": "3"
#     },
#     {
#         "cmd": "map",
#         "value": "0"
#     }, {
#         "cmd": "regex",
#         "value": "^37"}
#
# ]
# }