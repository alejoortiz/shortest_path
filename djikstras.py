#!/usr/bin/python3

# https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

from collections import defaultdict

def dijsktra(nodes,links, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = nodes[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = links[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def main():
    nodes = {
        'mexico': ['costa_rica', 'peru'],
        'costa_rica': ['mexico', 'colombia', 'venezuela'],
        'peru': ['mexico', 'venezuela', 'chile'], 
        'colombia': ['costa_rica', 'chile'], 
        'venezuela': ['costa_rica', 'chile', 'peru'], 
        'chile': ['colombia', 'venezuela', 'peru']
        }
    
    links = {
        ('mexico', 'costa_rica'): 1,
        ('costa_rica', 'mexico'): 1,
        ('mexico', 'peru'): 1,
        ('peru', 'mexico'): 1,
        ('costa_rica','colombia'): 1,
        ('colombia', 'costa_rica'): 1,
        ('costa_rica', 'venezuela'): 1,
        ('venezuela', 'costa_rica'): 1,
        ('colombia', 'chile'): 1,
        ('chile', 'colombia'): 1,
        ('venezuela', 'chile'): 1,
        ('chile', 'venezuela'): 1,
        ('venezuela', 'peru'): 1,
        ('peru', 'venezuela'): 1,
        ('peru', 'chile'): 1,
        ('chile', 'peru'): 1
        }
    
    print(dijsktra(nodes,links,'mexico','chile'))

if __name__ == '__main__':
    main()