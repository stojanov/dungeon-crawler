

class spatial_hash(object):
    def __init__(self):
        self.map = {}
    
    def get_at(self, pos):
        if pos in self.map:
            return self.map[pos]
        return []
    
    def put_at(self, pos, item):
        if pos in self.map:
            return self.map[pos].append(item)
        
        self.map[pos] = [item]
    
    def clear_at(self, pos):
        if pos in self.map:
            self.map[pos] = []
        
    def clear(self): 
        self.map.clear()