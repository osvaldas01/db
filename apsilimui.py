a = [25, (1, 2, 3), [1, 2, 3], 'abc', 1254, {1, 2, 3}]
result = {}

for item in a:
    try:
        result[item] = type(item).__name__
    except:
        result[str(item)] = type(item).__name__


print(result)
