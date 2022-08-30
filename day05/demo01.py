"""
封装----标准属性
作用：保护实例变量
   1、创建实例变量
   2、提供两个公开的读写方法
   3、使用@property修饰读取方法
      使用@属性名.setter修改写入方法
"""


class wife:
    def __init__(self, age = 26):
        self.age = age

    # @property  # 创建property对象，自动绑定下面的方法(读取)
    # def age(self):
    #     return self.__age

    # @age.setter  # 自动绑定下面方法(写入)
    def age(self, value):
        if 20 <= value <= 50:
            self.__age = value
        else:
            raise Exception("我不要")
    age = property(None,age)

w01 = wife(29)
print(w01.__dict__)
# w01.age = 280
# print(w01.age)
