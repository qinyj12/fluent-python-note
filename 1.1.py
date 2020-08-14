from collections import namedtuple

# 这是一个工厂函数，创建一个命名为'Card'的tump，然后赋值给Card变量。
Card = namedtuple('Card', ['rank', 'suit'])

# 创建一个扑克牌类
class FrenchDeck:
    # [A,2,3,4,5,6,7,8,9,10,J,Q,K]
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # ['spades','diamonds','clubs','hearts']
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 给类赋值一个_cards参数，这个参数就是52张扑克牌的list
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    # 一定要命名为__len__，这样就能使用len()方法了
    def __len__(self):
        # 这个方法返回的是self._cards的长度。要知道self.cards本身就是个list，所以自带len()方法
        return len(self._cards)

    # 一定要命名为__getitem__，这样这个类所创建的实例就是可迭代的了，可以通过[x]来获取第x位的元素，也可以用for...in...来遍历
    def __getitem__(self, position):
        # 这个方法返回的是这个类所创建的实例的迭代后的结果。实际上self._cards本身就是个可迭代对象。
        return self._cards[position]

# 创建实例
deck = FrenchDeck()

# 调用自定义的__len__方法
print(len(deck))
# 调用自定义的__getitem__方法
print(deck[0])