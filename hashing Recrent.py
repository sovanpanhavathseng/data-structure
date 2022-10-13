hashing = {}
print(hashing)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


car.update({"Number": "60"})
print(car)

def recurrent(car):
  if car == 1:
    return 1
  else:
    return car * recurrent(car - 1)
print(recurrent(10))
