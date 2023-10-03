from src.keyboard import Keyboard


def test_keyboard():
    keyboard = Keyboard('Dark Project KD87A', 9600, 5)
    assert keyboard.language == "EN"

    assert keyboard.change_lang() == "RU"
    assert keyboard.change_lang() == "EN"
