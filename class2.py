class Human:
  def __init__(self, fullname, nickname, age, gender, Birthday, HavePassport):
       self.fullname = fullname
       self.nickname = nickname
       self.age = age
       self.gender = gender
       self.Birthday = Birthday
       self.HavePassport = HavePassport
  def tellMySecret(self):
    return self.nickname + " I am Alien "


bouya = Human("Richard Jaroensawas", "Bouya", 10, "Male", "17th February 2013", True)
print(bouya.tellMySecret())
