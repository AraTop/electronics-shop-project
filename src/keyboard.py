class KeyBoard:
   language = None

   def __init__(self,item, price, quantity) -> None:
      self.language = "EN"
      self.item = item
      self.price = price
      self.quantity = quantity

   def change_lang(self):
      if self.language == "EN":
         self.language = "RU"
      elif self.language == "RU":
         self.language = "EN"

   def __str__(self) -> str:
      return f"{self.language}"

   def __str__(self) -> str:
      return f"{self.item}"
   
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
