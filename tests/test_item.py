"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from  src.item import Item
@pytest.fixture()
def item_zero():
    return Item("Смартфон", 10000, 20)
def tests_Item_init(item_zero ):
    assert item_zero.name ==  "Смартфон"
    assert item_zero.price == 10000
    assert item_zero.quantity == 20

def tests_Item_calculate_total_price(item_zero ):
    assert item_zero.calculate_total_price()  ==200000
def tests_Item_apply_discount(item_zero ):
    assert item_zero.apply_discount() == 10000
