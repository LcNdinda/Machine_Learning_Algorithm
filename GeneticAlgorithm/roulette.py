import random
#fitness
a = 4
b = 22
c = 100
d = 14
# obtaining total fitness
total_fitness = a + b + c + d
number = random.randint(0, total_fitness)
print(f"The random value selected is {number}")

# subtracting each fitness from the number
value = number - a
if value < 0:
    total_fitness = b + c + d
    print(f"The first parent is a = {a}")
    number = random.randint(0, total_fitness)
    print(f"The random value selected is {number}")
    value = number - b
    if value < 0:
        print(f"The second parent is b = {b}")
    value = number - c
    if value < 0:
        print(f"The second parent is c = {c}")
    value = number - d
    if value < 0:
        print(f"The second parent is d = {d}")

value = value - b
if value < 0:
    total_fitness = a + c + d
    print(f"The first parent is b = {b}")
    number = random.randint(0, total_fitness)
    print(f"The random value selected is {number}")
    value = number - a
    if value < 0:
        print(f"The second parent is a = {a}")
    value = number - c
    if value < 0:
        print(f"The second parent is c = {c}")
    value = number - d
    if value < 0:
        print(f"The second parent is d = {d}")

value = value - c
if value < 0:
    total_fitness = a + b + d
    print(f"The first parent is c = {c}")
    number = random.randint(0, total_fitness)
    print(f"The random value selected is {number}")
    value = number - a
    if value < 0:
        print(f"The second parent is a = {a}")
    value = number - c
    if value < 0:
        print(f"The second parent is b = {b}")
    value = number - d
    if value < 0:
        print(f"The second parent is d = {d}")

value = value - d
if value < 0:
    total_fitness = a + c + b
    print(f"The first parent is d = {d}")
    number = random.randint(0, total_fitness)
    print(f"The random value selected is {number}")
    value = number - a
    if value < 0:
        print(f"The second parent is a = {a}")
    value = number - c
    if value < 0:
        print(f"The second parent is c = {c}")
    value = number - d
    if value < 0:
        print(f"The second parent is b = {b}")
