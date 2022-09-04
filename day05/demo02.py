class enemy:
    def __init__(self,name="",blood_volume=0,attack=0):
        self.name=name
        self.blood_volume=blood_volume
        self.attack=attack
    @property
    def blood_volume(self):
        return self.__blood_volume
    @property
    def attack(self):
        return self.__attack
    @blood_volume.setter
    def blood_volume(self,blood_volume_value):
        if 0<=blood_volume_value<=100:
            self.__blood_volume = blood_volume_value
        else:
            raise Exception("血量不对")

    @attack.setter
    def attack(self, attack_value):
        if 1 <= attack_value <= 50:
            self.__attack = attack_value
        else:
            raise Exception("攻击力不对")
a01=enemy("孙悟空",2,10)
a01.attack = 20
a01.blood_volume=300
print(a01.blood_volume,a01.attack)


