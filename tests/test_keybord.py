from src.keyboard import KeyBoard

def test_str_item():
   kb = KeyBoard('Dark Project KD87A', 9600, 5)
   assert str(kb) == "Dark Project KD87A"

def test_str_lang():
   kb = KeyBoard('Dark Project KD87A', 9600, 5)
   assert str(kb.language) == "EN"

def test_str_lang_2():
   kb = KeyBoard('Dark Project KD87A', 9600, 5)
   kb.change_lang()
   assert str(kb.language) == "RU"

def test_str_lang_more():
   kb = KeyBoard('Dark Project KD87A', 9600, 5)
   kb.change_lang()
   kb.change_lang()
   kb.change_lang()
   assert str(kb.language) == "RU"