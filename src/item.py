import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
       

    def __repr__(self):
        return f"{self.__class__.__name__ }('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    @property  # геттер
    def name(self):
        return self.__name

    @name.setter  # сеттер
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

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

    @classmethod
    def instantiate_from_csv(cls, name_csvfile):
        with open(name_csvfile) as csvfile:
            csv_dict = csv.DictReader(csvfile)
            list_obj = []
            for el in csv_dict:
                item = Item(el['name'], el['price'], el['quantity'])
                list_obj.append(item)
            return list_obj

    @staticmethod
    def string_to_number(num):

        new_num = round(float(num))
        return new_num
