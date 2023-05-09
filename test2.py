
import tkinter

class Node():
    def __init__(self, value=None,next=None):
        self.value = value
        self.next = next


class ListNode():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

    def __str__(self):
        if self.length!=0:
            h = self.head
            result = f"ListNode [{h.value}"

            while h.next !=None:
                h = h.next
                result +=f", {h.value}"

            result +="]"
            return result
        else:
            return "ListNode []"
    
    def add(self, n):
        self.length+=1

        if self.head == None:
            self.head = self.tail = Node(n,None)
        else:
            self.tail.next = self.tail = Node(n, None)


    def reverse(self):
        h = self.head
        lst = [h]
        while h.next !=None:
            h = h.next
            lst.append(h)

        # lst.reverse()

        lst[-1].next = lst[-2]
        self.head = lst[-1]
        lst[0].next = None
        for i in range(1,len(lst)):
            try:
                lst[-i].next = lst[-i-1]
            except:
                break
        




l = ListNode()

for i in range(100):
    l.add(i)
print(l)
l.reverse()
print(l)