input_data = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
new_list = list(filter(lambda x: x[::-1].lower() == x.lower(), input_data))

print(new_list)
