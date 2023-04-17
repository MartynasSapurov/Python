class Car:
    FUEL_TYPES = ['бензин', 'дизель', 'электричество', 'гибрид']

    COLORS = []

    NUMBER_OF_CARS = 0

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        if fuel_type in Car.FUEL_TYPES:
            return fuel_type
        else:
            return Car.FUEL_TYPES[0]

    @classmethod
    def get_used_colors(cls):
        return len(cls.FUEL_TYPES)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS

    def __init__(self, model, year, fuel_type, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = Car.is_valid_fuel_type(fuel_type)
        Car.NUMBER_OF_CARS += 1
        if not (color in Car.COLORS):
            Car.COLORS.append(color)
        self.number = Car.NUMBER_OF_CARS

    def __str__(self):
        return f"{self.model}, {self.year}, {self.fuel_type}, {self.color}"

    @property
    def numbers(self):
        return f'{self.number} from {Car.NUMBER_OF_CARS}'


car_1 = Car('Zaz', 1979, 'дизель', 'black')

car_2 = Car('BMW', 2000, 'бензин', 'red')

car_3 = Car('VOLVO', 2012, 'электричествоcccc', 'black')

car_4 = Car('Mersedes', 2012, 'гибрид', 'black')

print('COLORS:', car_1.get_used_colors())
print('NUMBER_OF_CARS:', car_2.get_number_of_cars())

for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
