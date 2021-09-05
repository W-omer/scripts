class Node:
    """
    An object for storing a single node of a linked list.
    Models two attritubes - data and the link to the next node in the list."""
    
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data 

    def __repr__(self):
        return "<Node Data: %s>" % self.data
       
 
class Linkedlist:
     """
     Singly linked list"""

     def __init__(self):
         self.head = None 

     def is_empty(self):
        return self.head == None
    
     def size(self):
        """
        Returns the nomber of nodes in the list 0(n) time"""
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

     def add(self, data):
         """
         Adds a new Node containing data at the head of the list
         Takes 0(1) time.
         """
         new_node = Node(data)
         new_node.next_node = self.head
         self.head = new_node

     def search(self, key):
         """
         Search for the first node containing data that matches the key
         Return the node or 'None' if not found
         
         Takes 0(n) time
         """
         current = key.head

         while current:
             if current.data == key:
                 return print("%s is present in this list" % current.data)
             else:
                 current = current.next_node
             return print("%s was not found in this list." % current.data)


     def insert(self, data, index):
         """
         Inserts a new Node containing data at index position
         Insertion takes 0(1) time but finding the node at the 
         insertion point takes 0(n) time
         
         Takes overall 0(n) time
         """
         if index == 0:
             self.add(data)

         if index > 0:
             new = Node(data)
             node = []
             

             position = index
             current = self.head
S
             while position > 1:
                 current = node.next_node
                 position -= 1

             prev_node = current
             next_node = current.next_node

             prev_node.next_node = new
             new.next_node = next_node


     def remove(self, key):
         """
         Removes Node containing data that matches the key
         Returns the node or None if key doesn't exit
         Takes 0(n)
         e"""

         current = self.head
         previous = None
         

         while current and True:
             if current.data == key and current == self.head:
                 self.head = current.next_node
             elif current.data == key:
                 previous.next_node = current.next_node
             break




     def __repr__(self):
         """ 
         Return a string representation of the list
         Takes 0(n) time
         """

         nodes = []
         current = self.head

         while current:
             if current is self.head:
                 nodes.append("[Head: %s]" % current.data)
             elif current.next_node is None:
                 nodes.append("[Tail: %s]" % current.data)
             else:
                 nodes.append("[%s]" % current.data)

             current = current.next_node
         return '-> '.join(nodes)

                

    
    