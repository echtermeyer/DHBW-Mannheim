class LinkedListNode:
    def __init__(self, value, pointer=None):
        self.value = value
        self.next = pointer


ll = LinkedListNode(1)
ll.next = LinkedListNode(2)
ll.next.next = LinkedListNode(3)


while ll:
    print(ll.value)
    ll = ll.next
