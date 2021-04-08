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

        if current:
            while current.next:
                current = current.next

            current.next = new_element
        
        else:
            self.head = new_element

    
    def get_position(self,position):

        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list.
        """

        current = self.head
        next = 1

        while current:

            if( position == next ):
                return current

            current = current.next
            next += 1

        # If position not exist return None
        return Element( None )


    def insert(self, new_element, position):

        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        
        """

        current = self.head
        next = 1

        if position == 1:
            new_element.next = self.head.next
            self.head = new_element

            return None

        while current:

            if current.next:
                if position == next + 1:
                    new_element.next = current.next 
                    current.next = new_element


            current = current.next
            next += 1


    def delete(self, value):
        """Delete the first node with a given value."""
        

        current = self.head

        # If the value is equal to head, replace it
        if current.next and current.value == value:
            self.head = current.next 
            return None

        while current:
            
            if current.next:
                if current.next.value == value:
                    current.next = current.next.next

            current = current.next


    def print_items(self):
        current = self.head
        position = 1

        while current:

            print(current.value, "pos: {0} ".format(position))
            current = current.next
            position += 1


        return None


        



# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


ll.insert(e4,3)
ll.print_items()
