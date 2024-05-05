from collections import namedtuple, Counter, ChainMap
# from icecream import ic
#############Firs task
# //class Soda:
#     def __init__(self, add=None) -> None:
#         self.add = add

#     def show_my_drink(self):
#         if self.add:
#             return f"Газировка и {self.add}."
#         return "Обычная газировка."
    
# d1 = Soda()
# d2 = Soda('apple juce')
# ic(d1.show_my_drink())
# //ic(d2.show_my_drink())
###########Good good firs task is complete! iyyyy

######Task twoo lest gooooo
# //class CheckerTriangle:
#     def __init__(self, sides: list):
#         self.sides = sides

#     def is_triagle(self):
#         if type(self.sides[0]) is int and type(self.sides[1]) is int and type(self.sides[2]) is int:
#             if min(self.sides) > 0:
#                 if self.sides[0] + self.sides[1] > self.sides[2] and self.sides[0] + self.sides[2] > self.sides[1] and self.sides[1] + self.sides[2] > self.sides[0]:
#                     return "Ура, можно построить треугольник!"
#                 return "Жаль, но из этого треугольник не сделать."
#             return "С отрицательными числами ничего не выйдет!"
#         return "Нужно вводить только числа!"
    
# t1 = CheckerTriangle([4,6,7])
# t2 = CheckerTriangle([100,2,2])
# t3 = CheckerTriangle([1,4,-1])
# t4 = CheckerTriangle([5,6,'2'])
#// ic(t1.is_triagle(),t2.is_triagle(),t3.is_triagle(),t4.is_triagle())










#### Collections.namedtuple in python

# Card = collections.namedtuple('Card',['rank','suit'])

# class FenchDeck:
#     ranks = [i for i in range(2,11)] + list('JQKA')
#     suits =  'spades diamonds clubs hearts'.split()
    
#     def __init__(self):
#         self._cards = [Card(rank,suit) for suit in self.suits   
#                                        for rank in self.ranks] 

#     def __len__(self):
#         return len(self._cards)
    
#     def __getitem__(self,index):
#         return self._cards[index]
    

#Collections.Counter() and Counter().most_common() and Counter().elements()
# numbers = [1,2,1,2,3,3,4,5,9,9,9,9]
# lst = ['mango','avokado','mango','apple']
# strs = 'Haaah u loser'

# # coun = Counter(strs)
# # coun = Counter(strs).most_common(1) 
# coun = sorted(Counter(strs).elements())

# print(coun)


#Collections.defaultdict отличается от dict() лишь тем что при обрашении к не существующему ключу
# он не выдаст ошибку а вернет значение по умолчанию

#Collections.ChainMap
dic_1 = {'plane':'BM126','car':'BMW'}
dic_2 = {'red':1,'blue':5,'yellow':11}
dic_3 = {112:'Jonson',4445:'Alex'}

chain = ChainMap(dic_1,dic_2,dic_3)
lst_dicts = chain.maps
lst_keys_dict = list(chain.keys())

print(list(chain.values()))