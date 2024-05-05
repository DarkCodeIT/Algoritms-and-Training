#Связаные списки!! lets gooooo
#Создаем класс узла связаного списка:
# class Node:
#     def __init__(self, data=None, next=None):
#         #Присваеваем значение узла
#         self.data = data

#         #Ссылка на следующий узел
#         self.next = next

# def construct(keys):
#     head = None
#     #Начинаем создовать связаный список с конца
#     for i in reversed(range(len(keys))):
#         #Создаем новый узел head будет объектов класса Node
#         head = Node(data=keys[i],next=head)

#     return head

# def printNodeList(NodeList : Node):
#     ptr = NodeList
#     while ptr is not None:
#         print(ptr.data)
#         ptr = ptr.next
#     print('None') 

# keys = [9,8,7,6]
# head = construct(keys)




#Еще один способ создания связаного списка

#Создаем класс узлов
class Node:
    #Инициализируем переменные val-значение next-ссылка на следующий узел
    def __init__(self,val,next=None) -> None:
        self.val = val
        self.next = next

    #Создадим функции для узла
    def get_val(self):
        return self.val
    
    def set_val(self,val):
        self.val = val
        return

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next
    
#Создадим класс связаного списка
class LinkedList:
    #Создадим начальный элемент и размер списка
    def __init__(self,head=None) -> None:
        self.head = head
        self.size = 0
    #Создадим функции для класса связаного списка
    def get_size(self):
        return self.size
    
    def add_node(self,val,next=None):
        node = Node(val=val,next=next)
        self.head = node

        self.size += 1
        return
    
    def del_node(self,val):
        curr = self.head
        prev = None
        while curr:
            if curr.get_val() == val:
                if prev:
                    prev.set_next(curr.get_next())
                else:
                    self.head = curr.get_next()
                return True
            prev = curr
            curr = curr.get_next()
        return False
    
    def find_node(self,val):
        curr = self.head
        while curr:
            if curr.get_val() == val:
                return True
            else:
                curr = curr.get_next()
        return False
            
    def printLL(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.get_next()
        return
            
