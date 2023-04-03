import json
import random
import csv


def number_generator():
    operators = ['095', '066', '098', '096', '050', '097']
    number = "".join([str(random.randint(0, 10)) for x in range(6)])
    number = f"{operators[random.randint(0, 5)]}{number}"
    return number


name_of_fields = ["ID", "Имя", "Возраст", "Телефон"]

with open('Homework_16.txt') as f:
    output_data = json.load(f)

for key in output_data:
    output_data[key].append(number_generator()) if random.randint(0, 3) else output_data[key].append("")

with open("Homework_17.csv", mode='w', encoding='utf8', newline='') as file:
    file_writer = csv.writer(file)
    file_writer.writerow(name_of_fields)
    for key in output_data:
        output_data[key].append(number_generator()) if random.randint(0, 3) else output_data[key].append("")
        file_writer.writerow(output_data[key])
