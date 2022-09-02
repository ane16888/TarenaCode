class Person:
    def __init__(self, name=""):
        self.name = name

    def use_skill(self,emp):
        emp.attack()

class Atk:
    def attack(self):
        pass

class Lonelysword(Atk):
    def attack(self):
        print("使用独孤九剑")

class StarSuckingGreatSkill(Atk):
    def attack(self):
        print("使用独孤九剑")

p01 = Person("风清扬")
p02 = Person("任我行")
p02.use_skill(StarSuckingGreatSkill())