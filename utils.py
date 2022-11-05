def filter_from_params(param, data):
    return filter(lambda x: param in x, data)


def map_from_value(param, data):
    param = int(param)
    return map(lambda x: x.split(" ")[param], data)

#в случае если она может принять именнованные и позиционные арг
def unique(data,*args,**kwargs):
    return set(data)


def sort_query(param, data):
    return sorted(data, reverse=param == "desc")


def limit_qeury(param, data):
    limit = int(param)
    return list(data)[:limit]
