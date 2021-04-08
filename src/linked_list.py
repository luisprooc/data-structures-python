"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self,value):

        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self,head=None):

        self.head = head

    def append(self,new_element):
        current = self.head

        if self.head:
            while current.next:
                current = current.next

            current.next = new_element
        
        else:
            self.head = new_element

    
    def get_position(self,position):
        current = self.head
        next = 1

        while current:

            if( position == next ):
                return current

            current = current.next
            next += 1

        # If position not exist return None
        return Element( None )


        



# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print (ll.get_position(5).value)

