a = [(1, 2, 3), [1, 2, 3], 'abc', 1254, {1, 2, 3}]


result = {}
for item in a:
    if isinstance(item, list):
        item = tuple(item)
    elif isinstance(item, set):
        item = set(item)

    item_type = type(item)
    result[item] = item_type

print(result)