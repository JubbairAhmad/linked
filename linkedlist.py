class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0
    
    def __str__(self):
        x = self.head
        container = []
        while(x!=None):
            container.append(x.data)
            x = x.next
        return ('-->'.join(f'{i}' for i in container) + '-->None')
    

    def __len__(self):
        return self.size
    
    def addHead(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        
        else:
            node.next = self.head # curr head
            self.head = node #updated the head value
        self.size += 1
        return

    def addTail(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return
    
    def addAtIndex(self, data, index):
        if index < 0:
            raise IndexError("Index cant be negative.")
        
        if index == 0:
            return self.addHead(data)
        
        if index >= self.size-1:
            return self.addTail(data)
        
        node = Node(data)
        i = 0
        x = self.head
        while(i != index-1):
            x = x.next
            i += 1
        node.next = x.next
        x.next = node
        self.size += 1
        return
    
    def clear(self):
        x = self.head
        while x!= None:
            next = x.next
            # del x
            x.data = None
            x.next = None
            x = next
        return
    
    def removeHead(self):
        if self.size == 0:
            raise Exception("Linkedlist is already emnpty")
        else:
            x = self.head
            self.head = self.head.next
            x.data = None
            x.next = None
            self.size -= 1
            return
    
    def removeTail(self):
        if self.size == 0:
            raise Exception('Linkedlist is already emnpty')

        if self.size == 1:
            return self.removeHead()
        
        else:
            new_tail = self.head
            i = 0
            while (i != self.size-2):
                new_tail = new_tail.next
                i += 1
            x = self.tail
            self.tail = new_tail
            new_tail.next = None
            x.data = None
            self.size -= 1
            return
    
    def removeatIndex(self, index):
        if index < 0:
            raise IndexError("Index value is minimum 0")
        if index == 0:
            return self.removeHead()
        if index >= self.size -1:
            return self.removeTail()
        else:
            pointer1 = self.head
            pointer2 = self.head
            i = 0
            while (i != index - 1):
                pointer1 = pointer1.next
                pointer2 = pointer2.next 
                i += 1
            pointer1 = pointer1.next
            pointer1.next = pointer2.next
            pointer1.data = None
            pointer1.next = None
            self.size -=1
            return


def traverse_ll(head):
    #write your code
    jub = head
    while jub is not None:
        print(jub.data)
        jub = jub.next
    pass

if __name__ == '__main__':
    ll = LL()
    ll.addHead(5) # |1|
    ll.addHead(6) # |2|
    ll.addTail(10) # |3|
    ll.addAtIndex(4, 1) # |3|
    print(ll)
    traverse_ll(ll.head)
    