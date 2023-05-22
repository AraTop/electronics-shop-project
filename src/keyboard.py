from src.item import Item


class Mixin:
   pass


class KeyBoard(Item,Mixin):
   language = None

   def __init__(self,name, price, quantity) -> None:
      super().__init__(name, price, quantity)
      self.language = "EN"

   def change_lang(self):
      if self.language == "EN":
         self.language = "RU"
      elif self.language == "RU":
         self.language = "EN"

   def __str__(self) -> str:
      return f"{self.language}"

   def __str__(self) -> str:
      return f"{self.name}"
   
   @property
   def language_(self):
      return self.language
   
   @language_.setter
   def language_(self, name):
      if name in "EN":
         self.language = name

      elif name in "RU":
         self.language = name
         
      else:
         raise Exception("AttributeError: property 'language' of 'KeyBoard' object has no setter")
