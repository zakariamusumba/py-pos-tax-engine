class Market:
    def __init__(self, basic_goods, standard, luxury):
        self.bulk_discounts(basic_goods, standard, luxury)

    def bulk_discounts(self, basic_goods, standard, luxury):
        self.basic_goods = basic_goods
        self.standard = standard
        self.luxury = luxury

goods1 = Market("fish","70","0%")
print(goods1.basic_goods)
print(goods1.standard)
print(goods1.luxury)

class Bread(Market):
    def __init__(self,basic_goods, standard, luxury):
        self.val_discounts(basic_goods, standard, luxury)

    def val_discounts(self, basic_goods, standard, luxury):
        self.basic_goods = basic_goods
        self.standard = standard
        self.luxury = luxury

goods1 = Bread("bread", "65", "16%")
print(goods1.basic_goods)
print(goods1.standard)
print(goods1.luxury)