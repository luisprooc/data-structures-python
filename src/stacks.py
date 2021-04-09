from linked_list import LinkedList, Element

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first() 

    
    def print_items(self):

        current = self.ll.head

        while(current):
            print(current.value)

            current = current.next



e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


stack = Stack(e1)



stack.push(e2)
stack.push(e3)

stack.print_items()


print (stack.pop().value)

"""

print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)
"""