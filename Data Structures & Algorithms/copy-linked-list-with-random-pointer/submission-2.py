"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        #loop one through first time to create duplicates
        curr = head
        while curr:
            #Create replica of current node
            new_node = Node(curr.val)
            new_node.next = curr.next

            #make current node connect to new node
            curr.next = new_node
            curr = curr.next.next
        
        curr = head
        #Loop 2 to assign random pointers
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        
        #Loop 3 to assign            
        clone_head = head.next
        curr = head

        while curr:
            copy = curr.next

            #1. Restore the original list's next pointer
            curr.next = copy.next

            #2. Connect the current clone to the next clone (if it exists)
            copy.next = copy.next.next if copy.next else None

            #3. Move curr forward to the next original node
            curr = curr.next

        return clone_head

        
