Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Ticket:
...     def __init__(self, name, base_price):
...         self.__name = name
...         self.base_price = base_price
... 
...     def get_name(self):
...         return self.__name
...  
...     def price(self):
...         return self.base_price
...  
...  
... concert = Ticket("Concert", 200)
... museum = Ticket("Museum", 150)
... print(concert.name, concert.price())
... print(museum.name, museum.price())
