def suma_besidalijant_is_3(iterable):
    return sum([x for x in iterable if x % 3 == 0])


data = [1, 3, 2, 3, 2, 3]
result = suma_besidalijant_is_3(data)
print(result)
