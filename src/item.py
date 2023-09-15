from accessify import private
import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.price = price
        self.quantity=quantity
        Item.all.append(self)
        @private
        def name(self):
            self.name = name

    @property
    def get_name(self):
        return self.name
    @get_name.setter
    def set_name(self, name):
        if len(name ) <=10:
            self.name =name
        else:
            self.name = name[:10]



    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * Item.pay_rate


item = Item("Смартфон", 10000, 20)
# encode("utf8")
#print(item.price )

with open('/Users/dinara/PycharmProjects/electronics-shop-project/src/items.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

