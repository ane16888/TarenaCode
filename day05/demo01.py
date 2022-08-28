class dog:
    def __init__(self,variety,pet_name,age,sex):
        self.variety = variety
        self.pet_name = pet_name
        self.age = age
        self.sex = sex
    def eat(self):
        print(self.pet_name + "吃")

eat1 = dog("哈巴狗","毛毛",2,"雄性")
eat2 = dog("土狗","小毛毛",3,"雌性")
eat1.eat()
eat2.eat()