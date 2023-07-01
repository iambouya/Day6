class Car:
  def __init__(self, brand, color, totalseat, weight, speed):
       self.brand = brand
       self.color = color
       self.totalseat = totalseat
       self.weight = weight
       self.speed = speed
      
  def drive(self, speed):
     self.speed = speed
  
  def brake(self):
     self.speed = 0

  def info(self):
     print("Brand - " + self.brand)
     print("Color - " +self.color)
     print("Totalseat - " + str(self.totalseat) )
     print("Weight - " + str(self.weight) )
     print("Speed - " + str(self.speed) )
   

car = Car("Nissan", "Blue", 4, 1.5, 55)
car.drive(127)
car.info()
print("-----*BRAKE*------")
car.brake()
car.info()


