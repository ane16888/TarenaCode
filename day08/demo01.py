class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "x的分量是%d，y的分量是%d"%(self.x,self.y)
    # +
    def __add__(self, other):
        return Vector2(self.x+other.x,self.y+other.y)
    # +=
    def __iadd__(self, other):
        self.x +=other.x
        self.y +=other.y
        return self
    # -
    def __sub__(self, other):
        return Vector2(self.x-other.x,self.y-other.y)
    # -=
    def __isub__(self, other):
        self.x -=other.x
        self.y -=other.y
        return self
    # <
    def __lt__(self, other):
        return self.x+self.y < other.x + other.y
    # ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
pos=Vector2(1,2)
dir=Vector2(0,1)
pos -= dir
print(pos)
list01 = [Vector2(1,2),
          Vector2(6,3),
          Vector2(7,2),
          Vector2(5,9)]
# sorted升序：内部在循环调用每个元素的__lt__
for item in sorted(list01):
    print(item)
# in的内部也在循环调用每个元素的__eq__方法
print(Vector2(1,3) in list01)
