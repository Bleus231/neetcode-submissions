class Node:

    #Creates node in double linked list defaulting values to 0
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        #Create dummy head and tail nodes for O(1) look up times
        self.head = Node()
        self.tail = Node()

        #Linking head and tail together to create empty list
        self.head.next = self.tail
        self.tail.prev = self.head



    #Helper function to remove node in linked list
    #You remove node by ignoring its presence
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    #Helper fuction to insert node at tail of list
    def insert(self,node):
        old_prev = self.tail.prev
        new_prev = node


        old_prev.next = node
        new_prev.next = self.tail
        new_prev.prev = old_prev
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.insert(new_node)

        if len(self.cache) > self.capacity:
            #remove least recently used node from cache
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
