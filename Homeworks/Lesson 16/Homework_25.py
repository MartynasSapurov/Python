MyExit = ("выход","exit", "quit", "e", "q")


def string_checker(my_input):
    initial_value = my_input
    negative_flag = False
    invalid_value = False
    fractional_flag = False
    zero_flag = False

    my_input = my_input.replace(',', '.')

    if my_input.rfind('+') > 0:
        invalid_value = True
    elif my_input.rfind('+') == 0:
        my_input = my_input.replace('+', '')

    if not invalid_value:
        if my_input.rfind('-') > 0:
            invalid_value = True
        elif my_input.rfind('-') == 0:
            my_input = my_input.replace('-', '')
            negative_flag = True

    if not invalid_value:
        if my_input.count('.') > 1:
            invalid_value = True
        elif my_input.count('.') == 1:
            fractional_flag = True
            if my_input.rfind('.') == 0:
                my_input = f'0{my_input}'
            if not my_input.replace('.', '').isdigit():
                invalid_value = True

    if not invalid_value and not fractional_flag:
            if not my_input.isdigit():
                invalid_value = True

    negative = "отрицательное" if negative_flag else "положительное"
    Negative = "дробное" if fractional_flag else "целое"

    if not invalid_value:
        if fractional_flag:
            number = float(my_input)
        else:
            number = int(my_input)

    if not invalid_value and negative_flag:
            number = number * -1

    if not invalid_value and number == 0:
        zero_flag = True

    if invalid_value:
        output = f'Вы ввели не корректное число: {initial_value}'
    elif zero_flag:
        output = 'Вы ввели ноль'
    else:
        output = f'Вы ввели {negative} {Negative} число: {number}'

    return output


while True:
    read = input("Введите число либо команду выходаn\n")
    read = read.lower()

    if read in MyExit:
        break

    print(string_checker(read))
