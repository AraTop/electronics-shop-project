from src.phone import Phone

def test_str():
   phone1 = Phone("iPhone 14", 120_000, 5, 2)
   assert str(phone1) == 'iPhone 14'

def test_repr():
   phone1 = Phone("iPhone 14", 120_000, 5, 2)
   assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_rename():
   phone1 = Phone("iPhone 14", 120_000, 5, 2)
   assert phone1.number_of_sim == 2

def test_harmonization():
   phone1 = Phone("iPhone 14", 120_000, 5, 2)
   assert phone1 + phone1 == 10