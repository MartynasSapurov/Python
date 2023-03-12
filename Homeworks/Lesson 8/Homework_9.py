import random


def number_check(input_number: int, number_list: list) -> int:
    """Function returns  number of times provided number
    is present in list for number in range 0 to 9"""
    count = 0
    for x in range(len(number_list)):
        if number_list[x] == input_number:
            count += 1
    return count


random_number_list = [random.randint(1, 10) for x in range(200)]
number_count = {x: number_check(x, random_number_list) for x in range(1, 11)}
number_count = dict(sorted(number_count.items(),
                           key=lambda x: x[1], reverse=True))
print(random_number_list)

for x in number_count:
    print(f"Число {x} встречается в первоначальном списке {number_count.get(x)}",
          (lambda x: "разa" if x % 10 in range(2, 5) and x not in range(11, 15) else "раз")
          (number_count.get(x)))
