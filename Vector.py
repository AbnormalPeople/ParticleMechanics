#!/Users/alexandre/opt/anaconda3/envs/Coding/bin/python
import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.coordinates = [x, y]

    @property
    def norm(self):
        return math.sqrt(self.x*self.x + self.y*self.y)

    @norm.setter
    def norm(self, newnorm):
        mynorm = self.norm
        self.x = self.x*newnorm/mynorm
        self.y = self.y*newnorm/mynorm

    @property
    def x(self):
        return self.coordinates[0]
    
    @x.setter
    def x(self, x):
        self.coordinates[0] = x

    @property
    def y(self):
        return self.coordinates[1]

    @y.setter
    def y(self, y):
        self.coordinates[1] = y

    def __str__(self):
        return "( {0} ; {1} )".format(self.x, self.y)

    def __add__(self, v):
        result = Vector2D()
        result.coordinates[0] = self.x + v.x
        result.coordinates[1] = self.y + v.y
        return result
 
    def __sub__(self, v):
        result = Vector2D()
        result.coordinates[0] = self.x - v.x
        result.coordinates[1] = self.y - v.y
        return result

    def __mul__(self, num):
        if isinstance(num,int) or isinstance(num, float):
            return type(self)(self.x*num, self.y*num)
        return type(self)(0,0)

# v1 = Vector2D(5, 6)
# v2 = Vector2D(10, 6)

# v2.x=123
# print(v2)

# #v3 = v1 + v2
# #print(v3)
# print(v1.coordinates[0])
# print(v1.x)
# print(v1.y)
# print(v1)
# print(v1.norm)
# v3 = v1 + v2
# print("{0} + {1} = {2}".format(v1, v2, v3))
# print(v3.norm)
# v3.norm=5
# print(v3)
# print(v3.norm)
