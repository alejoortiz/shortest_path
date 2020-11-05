#!/usr/bin/python3

# original code and explanation is on the following link
# https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/

import time

def lookup(shortest_paths,end):
    current_node = end
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

def dijsktra(nodes,links, initial, end):
    # init variable with root node
    current_node = initial
    # shortest paths is a dict of nodes
    shortest_paths = {initial: (None, 0)}
    # keep track of visited nodes
    visited = []
    # counter for check steps
    counter = 0

    # check if source node and destination are not the same
    while current_node != end:

        print("Step = "+str(counter))
        print("Current node = ",current_node)
        print("Visited = ",visited)

        visited.append(current_node)
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
        
        counter += 1
        print("shortest_paths = ",shortest_paths)
        print("Next node = ",current_node)
        print("\n")
        # time.sleep(5)
    return shortest_paths

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
        ('mexico', 'peru'): 2,
        ('peru', 'mexico'): 2,
        ('costa_rica','colombia'): 2,
        ('colombia', 'costa_rica'): 2,
        ('costa_rica', 'venezuela'): 1,
        ('venezuela', 'costa_rica'): 1,
        ('colombia', 'chile'): 1,
        ('chile', 'colombia'): 1,
        ('venezuela', 'chile'): 2,
        ('chile', 'venezuela'): 2,
        ('venezuela', 'peru'): 1,
        ('peru', 'venezuela'): 1,
        ('peru', 'chile'): 1,
        ('chile', 'peru'): 1
        }
    
    shortest_paths = dijsktra(nodes,links,'mexico','chile')

    print("Path to colombia = ",lookup(shortest_paths,'colombia'))
    print("Path to chile = ",lookup(shortest_paths,'chile'))
    print("Path to venezuela = ",lookup(shortest_paths,'venezuela'))

if __name__ == '__main__':
    main()