Dictionary = {}
print(Dictionary)

Dictionary.clear()
print(Dictionary)

Dictionary.copy()
print(Dictionary)

a = {'key1', 'key2', 'key3'}
b = 0

c = Dictionary.fromkeys(a, b)
print(c)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

d = car.get("model")
print(d)

e = car.items()
print(e)

car.pop("model")
print(car)

car.popitem()
print(car)

f = car.setdefault("model", "Bronco")
print(f)

car.update({"model":"ford"})
print(car)

g = car.values()
print(g)
