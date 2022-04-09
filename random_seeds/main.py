import random

test = random.randint(1, 10)

for i in range(11):
    random.seed(i)
    test = random.randint(1, 10)
    print(f"{i} = {test}")
    i += 1

random.seed(1)
print(random.randint(1, 10))


