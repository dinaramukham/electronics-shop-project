import pytest
from src.item import Item, InstantiateCSVError
def tests_instantiate_FileNotFound():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('items - items.csv.csv')
def tests_instantiate_InstantiateCSV():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('/Users/dinara/PycharmProjects/electronics-shop-project/src/items - items— копия.csv.csv')
