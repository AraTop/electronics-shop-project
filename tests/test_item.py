from src.item import Item

def test_item1():
   user1 = Item("Валера", 5000, 10)
   assert user1.calculate_total_price() == 50000

def test_item2():
   user1 = Item("Валера", 5000, 10)
   user1.apply_discount()
   assert user1.price == 5000

def test_item3():
   user1 = Item("Валера", 5000, 10)
   user1.apply_discount()
   assert user1.price == 5000

def test_item4():
   user1 = Item("Валера", 5000, 10)
   Item.pay_rate = 0.5
   user1.apply_discount()
   assert user1.price == 2500

def test_item5():
   user1 = Item("Валера", 5000, 10)
   assert user1.name == "Валера"

def test_item6():
   user1 = Item("Валера", 5000, 10)
   assert user1.price == 5000

def test_item7():
   user1 = Item("Валера", 5000, 10)
   assert user1.quantity == 10  

def test_item8():
   item = Item('Телефон', 10000, 5)
   item.name = 'Смартфон'
   assert item.name == 'Смартфон'

def test_item9():
   Item.instantiate_from_csv()
   assert len(Item.all) == 5

def test_item10():
   assert Item.string_to_number('5') == 5
   assert Item.string_to_number('5.0') == 5
   assert Item.string_to_number('5.5') == 5