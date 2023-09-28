from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, number_of_sim, quantity=0) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.number_of_sim}, {self.quantity})"

    def __add__(self, other):
        if not isinstance(other, (Item, Phone)):
            raise ValueError("Справа от плюса классы Item или Phone")

        return int(self.quantity) + int(other.quantity)

    def __radd__(self, other):
        if not isinstance(other, (Item, Phone)):
            raise ValueError("Слева от плюса классы Item или Phone")
        return int(self.quantity) + int(other.quantity)
