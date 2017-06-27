class LinkedNode:

    def __init__(self, key=None, value=None, next=None, pre=None):
        self.key = key
        self.value = value
        self.next = next
        self.pre = pre

class LRUCache(object):

    def __init__(self, capacity):
        self.hash_map = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_front(self, node):
        node.next = self.head
        node.prev = None
        self.head = node
        self.hash_map[node.key] = self.head

    def pop_tail(self):
        del self.hash_map[self.tail.key]
        self.tail = self.tail.prev
        self.tail.next = None

    def kick(self, node):
        if node.prev == None:
            # Current node is head
            return
        if node.next == None:
            # Current node is tail
            self.pop_tail()
            self.push_front(node)
            return
        node.prev.next = node.next
        self.push_front(node)

    def get(self, key):
        if key not in self.hash_map:
            return -1
        self.kick(self.hash_map[key])
        return self.hash_map[key].value

    def set(self, key, value):
        if key in self.hash_map:
            self.kick(self.hash_map[key])
        else:
            self.push_front(LinkedNode(key, value))
            if len(self.hash_map) > self.capacity:
                self.pop_tail()