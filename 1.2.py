from math import hypot

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 用print调用
    def __repr__(self):
        # %r是把参数原样打印出来，这里用%s其实也是可以的
        return 'Vector(%r, %r)' % (self.x, self.y)
    # 用abs()调用
    def __abs__(self):
        return hypot(self.x, self.y)
    # 用 Vector(x, y) + Vector(x, y) 调用，就是普通的加号
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    # 用for ... in ...调用
    # 似乎一定要返回一个iter()对象，而根据文档，iter()只能返回iterator即迭代器,而迭代器自身又要有__iter__()方法，晕了。
    # 反正这里如果直接返回一个list是会报错的，返回迭代器就没问题
    def __iter__(self):
        return iter([self.x, self.y])

for i in Vector(3, 4):
    print(i)