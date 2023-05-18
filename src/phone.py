from src.item import Item

class Phone(Item):
   count_cards = None

   def __init__(self, name: str, price: float, quantity: int, count_cards) -> None:
      super().__init__(name, price, quantity)
      self.count_cards = count_cards

   def __str__(self) -> str:
      return f'{self.name}'
   
   def __repr__(self) -> str:
      return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.count_cards})"
   
   @property
   def number_of_sim(self):
        return self.count_cards
   
   @number_of_sim.setter
   def number_of_sim(self, numbers):
      if self.count_cards <= 0:
         raise Exception(f"ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
      else:
         self.count_cards = numbers

   def __add__(self, other):
      if isinstance(other, self.__class__):
         return self.quantity + other.quantity  
      return None