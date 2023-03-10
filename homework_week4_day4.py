class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"<Node|{self.value}>"
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __get_node(self, value_to_get):
        check = self.head
        while check is not None:
            if check.value == value_to_get:
                return check
            check = check.next
        return None
        
    def push_on(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
            
    def insert_after(self, prev_value, new_value):
        prev_node = self.__get_node(prev_value)
        if prev_node is None:
            print(f"{prev_value} is not in linked list")
            return
        
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def traverse_list(self):
        node = self.head
        while node:
            print(node) 
            node = node.next
    
    def remove(self, value_to_remove):
        prev_node = self.head
        if prev_node.value == value_to_remove:
            self.head = prev_node.next
        while prev_node.next is not None:
            node_to_check = prev_node.next
            if node_to_check.value == value_to_remove:
                prev_node.next = node_to_check.next
            prev_node = prev_node.next
            
    
weekdays = LinkedList()
list_of_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in list_of_days:
    weekdays.append(day)

weekdays.traverse_list()
weekdays.remove('Wednesday')
weekdays.traverse_list()