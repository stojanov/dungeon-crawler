from tkinter.tix import MAX


MAX_ENTITIES = 5000

class entity_container(object):
    def __init__(self):
        self.container = [None] * MAX_ENTITIES
        self.removed = {}
        self.size = 0
        
    def add(self, item):
        if len(self.removed) >= 1:
            idx = list(self.removed.keys())[0]
            self.container[idx] = item
            self.removed.pop(idx)
            return
        elif self.size + 1 > MAX_ENTITIES:
            print("Entities exceeded maximum limit")
            return
        
        self.container[self.size] = item
        self.size += 1
        
    def is_removed(self, idx):
        return idx in self.removed
        
    def get_last(self):
        return self.container[self.size - 1]
    
    def clean_up(self):
        if self.size <= 0:
            print("Cannot clean up the entitiy container since it's empty")
            return
        for idx in self.removed.keys():
            self.container[idx] = self.container[self.size - 1]
            self.removed.pop(idx)
            self.size -= 1
    
    def remove(self, idx):
        self.removed[idx] = True
    
    # RISKY! 
    def removeByIdx(self, idx):
        if self.size <= 0:
            return
        self.container[idx] = self.container[self.size - 1]
        self.size -= 1
    
    def count(self):
        return self.size
    
    def entities(self):
        return self.container
    
    def for_each(self, functor):
        for i in range(self.size):
            if i not in self.removed:
                continue
            functor(self.container[i])
        
    