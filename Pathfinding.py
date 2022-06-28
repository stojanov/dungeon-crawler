
from collections import deque

GOODENOUGH_FIND = 15

class path_node(object):
    def __init__(self, cost, prev):
        self.cost = cost
        self.prev = prev

def find_neighbours(point):
    return [
        (point[0] - 1, point[1]),
        (point[0] + 1, point[1]),
        (point[0], point[1] - 1),
        (point[0], point[1] + 1),
    ]

# dijksta
def path_dijkstra_nodes(startpoint, grid, check_func, depth = None):
    nodes = {
        startpoint: path_node(0, None)
    }
    visited = {} # used as a hash set
    should_visit = deque()
    
    should_visit.append(startpoint)
    
    while len(should_visit) > 0:
        current_point = should_visit.popleft()

        if current_point in visited:
            continue
        
        visited[current_point] = True
        parent = nodes[current_point]
        
        if depth != None and parent.cost >= depth:
            continue
        
        for point in find_neighbours(current_point):
            if not point in grid or check_func(grid[point]):
                continue
            
            if not point in nodes:
                nodes[point] = path_node(parent.cost + 1, current_point)
                should_visit.append(point)
                continue
            
            node = nodes[point]
            newcost = parent.cost + 1
            
            if newcost < node.cost:
                node.cost = newcost
                node.prev = current_point
                
    return nodes

def path_find_best_point(nodes, currentpoint):
    bestpoint = None
    bestcost = 10000000
    
    if len(nodes) <= 0:
        return None
    
    for point in find_neighbours(currentpoint):
        if not point in nodes:
            continue

        node = nodes[point]
        
        if node.cost < bestcost:
            bestcost = node.cost
            bestpoint = point

    return bestpoint

def path_shortest(nodes, currentpoint, endpoint):
    point = currentpoint
    shortest_path = []
    while point != endpoint:
        point = path_find_best_point(nodes, point)
        shortest_path.append(point)
        
    return shortest_path

# dijkstra's algorithm
# should have implemented A* but in my use-case dijkstra should be fine
def findpath_dijkstra(startpoint, endpoint, grid, check_func, goodenough = None):
    nodes = {
        startpoint: path_node(0, None)
    }
    visited = {}
    should_visit = deque()
    
    should_visit.append(startpoint)
    
    found = False
    while len(should_visit) > 0:
        current_point = should_visit.popleft()
        if current_point == endpoint: 
            found = True
        
        if current_point in visited:
            continue
        
        visited[current_point] = True
        parent = nodes[current_point]
        
        for point in find_neighbours(current_point):
            if not point in grid or check_func(grid[point]):
                continue
            
            if not point in nodes:
                nodes[point] = path_node(parent.cost + 1, current_point)
                should_visit.append(point)
                continue
            
            node = nodes[point]
            newcost = parent.cost + 1
            
            if newcost < node.cost:
                node.cost = newcost
                node.prev = current_point
        
            if point == endpoint and goodenough != None and node.cost <= goodenough:
                should_visit = []
                found = True
                break
                
    shortest_path = []
    if found:
        current_point = endpoint
        # backtracking to find the shortest path
        while current_point != startpoint:
            min_point = None
            min_cost = 10000000
            
            for point in find_neighbours(current_point):
                if not point in nodes:
                    continue
                
                node = nodes[point]
                if node.cost < min_cost:
                    min_point = point
                    min_cost = node.cost
                    
            current_point = min_point
            
            shortest_path.append(min_point)
            
        if len(shortest_path) == 0:
            return None
        
        return shortest_path
    else:
        return None
