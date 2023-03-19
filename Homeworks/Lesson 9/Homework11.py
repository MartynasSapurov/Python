my_list = [1, 7, 8, 'name', 'a', (1, 2, 4)]

new_list = list(map(lambda x: str(x) if isinstance(x, int) else x, my_list))
print(my_list)
print(new_list)
