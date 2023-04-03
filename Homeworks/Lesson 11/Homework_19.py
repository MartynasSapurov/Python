import time


class Auto(object):

    def __init__(self, brand, age, mark, color="Red", weight=1000):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('«move»')

    def stop(self):
        print('«stop»')

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="Red", weight=1000):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print('«attention»')
        super().move()
        

    def load(self):
        time.sleep(1)
        print('«load»')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="Red", weight=1000):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        print(f"«max speed is {self.max_speed}»")


truck_1 = Truck("Ford", 5, "650", 40000)
truck_2 = Truck("Volvo", 7, "740", 35000)

car_1 = Car("Saab", 3, "960", 260)
car_2 = Car("Subaru", 9, "Impreza", 290)

print(truck_1.age)
truck_1.load()
truck_1.move()
truck_1.stop()
truck_1.birthday()
print(truck_1.age)

truck_2.color = "Blue"
truck_2.weight = 1000

print(truck_2.brand)
print(truck_2.age)
print(truck_2.mark)
print(truck_2.max_load)
print(truck_2.color)
print(truck_2.weight)

print(car_1.age)
car_1.move()
car_1.stop()
car_1.birthday()
print(car_1.age)

car_2.color = "Blue"
car_2.weight = 1000

print(car_2.brand)
print(car_2.age)
print(car_2.mark)
print(car_2.max_speed)
print(car_2.color)
print(car_2.weight)
