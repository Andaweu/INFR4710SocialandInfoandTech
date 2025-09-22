import networkx as nx
import matplotlib.pyplot as plt
import random

def RandomWalkDest(graph, root, dest):
    """
    Performs a Random Walk on the graph from the root to the dest node.
    Returns the list of the nodes in the order they were visited and a
    graph to visualize it
    Each run should return a different path.
    """
    #Your code here

    pointer = root #set the pointer to the root position
    path = [pointer] #start the path at the pointer
    visitedNodes = [] #create a list for nodes visited

    while pointer != dest: #run while not at destination node
        adjacent = list(graph.neighbors(pointer)) #create a list of neighboring nodes to the pointer
        if not adjacent: #if no adjacent nodes, break the code
            break

        nextNode = random.choice(adjacent) #chose a random adjacent node
        visitedNodes.append((pointer, nextNode)) #collect the next node and where it came from
        pointer = nextNode #move the pointer to the next node
        path.append(pointer) #append the new pointer to the path

    
    subgraph = nx.Graph()
    subgraph.add_edges_from(visitedNodes) #add the pathways from visitedNodes to the graph

    return subgraph, path


def RandomWalkHops(graph, root, hops):
    """
    Performs a Random Walk on the graph from the root and makes a given number
    of random hops through the graph.
    Returns the list of the nodes in the order they were visited and a
    graph to visualize it
    Each run should return a different path.
    """
    #Your code here

    pointer = root #set the pointer to the root position
    path = [pointer] #start the path at the pointer
    visitedNodes = [] #create a list for nodes visited

    for i in range(hops): #runs until travelled the desired number of hops
        adjacent = list(graph.neighbors(pointer)) #create a list of neighboring nodes to the pointer
        if not adjacent: #if no adjacent nodes, break the code
            break
        nextNode = random.choice(adjacent) #chose a random adjacent node
        visitedNodes.append((pointer, nextNode)) #collect the next node and where it came from
        pointer = nextNode #move the pointer to the next node
        path.append(pointer) #append the new pointer to the path

    
    subgraph = nx.Graph()
    subgraph.add_edges_from(visitedNodes) #add the pathways from visitedNodes to the graph


    return subgraph, path

"""
CODE TO TEST YOUR FUNCTIONS BEGINS HERE (DON'T MODIFY)
"""

graph = nx.erdos_renyi_graph(20, 0.4, 4170)
plt.subplot(111)
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()


RandomGraph, RandomSeq = RandomWalkDest(graph, 0, 19)
plt.subplot(111)
nx.draw(RandomGraph, with_labels=True, font_weight='bold')
print("Random Walk Sequence: ", RandomSeq)
plt.show()
   
RandomGraph, RandomSeq = RandomWalkHops(graph, 0, 20)
plt.subplot(111)
nx.draw(RandomGraph, with_labels=True, font_weight='bold')
print("Random Walk Sequence: ", RandomSeq)
plt.show()
