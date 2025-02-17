class Car:
  def __init__(self, max_speed, speed_unit):
    self.speed_unit = speed_unit
    self.max_speed = max_speed

  def __str__(self):
    return (f"Car with the maximum speed of {self.max_speed} {self.speed_unit}")  
  pass

class Boat:
  def __init__(self, max_speed):
    self.max_speed = max_speed

  def __str__(self):
    return (f"Boat with the maximum speed of {self.max_speed} tonks")

x = Car("21", "km/h")
y = Boat("50")
print(x,"\n",y)