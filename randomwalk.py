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

    pointer = root
    path = [pointer]
    visitedNodes = []

    while pointer != dest:
        adjacent = list(graph.neighbors(pointer))
        if not adjacent:
            break

        nextNode = random.choice(adjacent)
        visitedNodes.append((pointer, nextNode))
        pointer = nextNode
        path.append(pointer)

    
    subgraph = nx.Graph()
    subgraph.add_edges_from(visitedNodes)

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

    pointer = root
    path = [pointer]
    visitedNodes = []

    for i in range(hops):
        adjacent = list(graph.neighbors(pointer))
        if not adjacent:
            break
        nextNode = random.choice(adjacent)
        visitedNodes.append((pointer, nextNode))
        pointer = nextNode
        path.append(pointer)

    
    subgraph = nx.Graph()
    subgraph.add_edges_from(visitedNodes)


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
