import pytest
from src.phone import  Phone
from src.item import  Item
def test_Phone():
    exzample = Phone("iPhone 14", 120_000, 2, 5)
    assert exzample.name == "iPhone 14"
def test_Phone_number_of_sim():
    exzample = Phone("iPhone 14", 120_000, 2, 5)
    exzample1=Item("Смартфон", 10000, 20)
    assert exzample + exzample1 == 25
