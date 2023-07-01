class Human:
  def __init__(self, fullname, nickname, age, gender, Birthday, HavePassport):
       self.fullname = fullname
       self.nickname = nickname
       self.age = age
       self.gender = gender
       self.Birthday = Birthday
       self.HavePassport = HavePassport


bouya = Human("Richard Jaroensawas", "Bouya", 10, "Male", "17th February 2013", True)
print(bouya.fullname)
print(bouya.nickname)
print(bouya.age)
print(bouya.gender)
print(bouya.Birthday)
print(bouya.HavePassport)