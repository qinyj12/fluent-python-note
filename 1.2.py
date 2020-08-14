# class Students(object):
#     def __init__(self, list):
#         self.namelist = list
#     # 通过for ... in ... 来调用函数
#     def __iter__(self):
#         # 如果不返回迭代器的话，似乎会报错
#         return iter(self.namelist)

# class1 = Students(['dog', 'cat'])
# # 调用自定义的迭代函数
# for i in class1:
#     print(i)

# from math import hypot

# class Vector(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return 'Vector(%)'