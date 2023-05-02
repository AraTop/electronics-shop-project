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