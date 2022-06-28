MAX_ENTITIES = 5000

class entity_container(object):
    def __init__(self):
        self.container = [None] * MAX_ENTITIES
        self.size = 0
        
    def add(self, item):
        if self.size + 1 > MAX_ENTITIES:
            print("Entities exceeded maximum limit")
            return
        self.container[self.size] = item
        self.size += 1
        
    def get_last(self):
        return self.container[self.size - 1]
    
    def remove(self, idx):
        if self.size <= 0:
            return
        self.container[idx] = self.container[self.size - 1]
        self.size -= 1
    
    def count(self):
        return self.size
    
    def entities(self):
        return self.container
        
    