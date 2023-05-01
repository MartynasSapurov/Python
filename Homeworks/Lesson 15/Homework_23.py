def simple_generator(value, q, limit):
    while limit > 0:
        yield value
        value *= q
        limit -= 1


geometric_series = simple_generator(1, 2, 20)

for item in geometric_series:
    print(item)