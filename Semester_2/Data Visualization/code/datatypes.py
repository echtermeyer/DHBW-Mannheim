class LinkedList:
    def __init__(self, value, pointer=None):
        self.value = value
        self.next = pointer

my_list = [LinkedList(1, LinkedList(7), LinkedList(20, None))]
print(my_list)
print(my_list[0].value)
print(my_list[0].next)
