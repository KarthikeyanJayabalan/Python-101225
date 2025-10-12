x = range(1, 6)
print(list(x))
print(tuple(x))
print(set(x))

for i in x:
    print(i)

carName = ["Audi", "BMW", "Honda", "Tata"]

for index, i in enumerate(carName):
    print(f"{index+1}.", i)