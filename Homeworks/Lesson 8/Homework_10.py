import random

number = random.randint(0, 200)

print(f"Число {number}",
      (lambda x: "ноль" if x == 0 else "не чётное" if (x % 2) else "чётное")
      (number))
