from src.item import Item

def test_calculate_total_price():
   user1 = Item("Валера", 5000, 10)
   assert user1.calculate_total_price() == 50000

def test_apply_discount_1():
   user1 = Item("Валера", 5000, 10)
   user1.apply_discount()
   assert user1.price == 5000

def test_apply_discount_2():
   user1 = Item("Валера", 5000, 10)
   user1.apply_discount()
   assert user1.price == 5000

def test_apply_discount_3():
   user1 = Item("Валера", 5000, 10)
   Item.pay_rate = 0.5
   user1.apply_discount()
   assert user1.price == 2500

def test_name():
   user1 = Item("Валера", 5000, 10)
   assert user1.name == "Валера"

def test_price():
   user1 = Item("Валера", 5000, 10)
   assert user1.price == 5000

def test_quantity():
   user1 = Item("Валера", 5000, 10)
   assert user1.quantity == 10  

def test_name():
   item = Item('Телефон', 10000, 5)
   item.name = 'Смартфон'
   assert item.name == 'Смартфон'

def test_instantiate_from_csv():
   Item.instantiate_from_csv()
   assert len(Item.all) == 5

def test_string_to_number():
   assert Item.string_to_number('5') == 5
   assert Item.string_to_number('5.0') == 5
   assert Item.string_to_number('5.5') == 5

def test_repr():
   item1 = Item("Смартфон", 10000, 20)
   assert repr(item1) =="Item('Смартфон', 10000, 20)"

def test_str():
   item1 = Item("Смартфон", 10000, 20)
   assert str(item1) == 'Смартфон'

def test_test():
   assert Item.instantiate_from_csv() == "FileNotFoundError: Отсутствует файл item.csv"