graph = {}
print(graph)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1944
}

car.clear()
print(car)

a = car.copy()
print(a)

b = ('key1',' key2', 'key3')
c = 0
d = graph.fromkeys(b, c)
print(d)

e = car.get("model")
print(e)

f = car.items()
print(f)

g = car.keys()
print(g)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1944
}

car.pop("model")
print(car)

car.popitem()
print(car)

h = car.setdefault("model", "Bronco")
print(h)

car.update({"color": "White"})
print(car)

i = car.values()
print(i)
