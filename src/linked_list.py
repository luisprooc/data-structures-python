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

    
    def get_position(self,position) -> object:

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


    def insert(self, new_element, position) -> None:

        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        
        """

        current = self.head
        next = 1

        while current:

            if current.next:
                if position == next + 1:
                    new_element.next = current.next 
                    current.next = new_element


            current = current.next
            next += 1


    def delete(self, value) -> None:
        """Delete the first node with a given value."""
        
        current = self.head

        while current:
            
            if current.next:
                if current.next.value == value:
                    current.next = current.next.next

            current = current.next


    def insert_first(self, new_element) -> None:
        "Insert new element as the head of the LinkedList"
          
        new_element.next = self.head
        self.head = new_element

      

    def delete_first(self) -> object:
        "Delete the first (head) element in the LinkedList as return it"
        prev = self.head

        if self.head.next:
            self.head = self.head.next
            prev.next = None
            return prev

        return prev


    def print_items(self) -> None:
        current = self.head
        position = 1

        while current:

            print(current.value, "pos: {0} ".format(position))
            current = current.next
            position += 1


        return None


    def size(self) -> int:
        current = self.head
        length = 0

        while current:
            current = current.next
            length += 1


        return length


        


# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


print(ll.size())