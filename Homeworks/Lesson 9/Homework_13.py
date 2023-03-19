import random
from datetime import datetime
time = [0, 0]


def my_decorator(func):
    def wrapper():
        time[0] = datetime.now()
        func()
        time[1] = datetime.now()
        print(time[1]-time[0])
    return wrapper


@my_decorator
def dummy_function_1():
    random_number_list = [random.randint(1, 10) for x in range(2000000)]


@my_decorator
def dummy_function_2():
    random_number_list = [random.randint(1, 10) for x in range(1000000)]


dummy_function_1()
dummy_function_2()
