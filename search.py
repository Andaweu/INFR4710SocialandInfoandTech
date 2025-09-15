from my_queue import Queue
from my_stack import Stack
import networkx as nx
import matplotlib.pyplot as plt

def BFS(graph, root):
    """
    Performs a Breadth-First Search on a given graph
    to output a spanning subgraph of the original graph,
	and the sequence of nodes are visited.
    """
    #Your code here


    visitedNodes = set()
    queue = Queue()
    queue.push(root)
    sequence = []
    spanningTree = nx.Graph()

    queue.push(root)
    visitedNodes.add(root)
    while not queue.is_empty():
        pointer = queue.pop()
        sequence.append(pointer)
        
        for i in graph.neighbors(pointer):
            if i not in visitedNodes:
                visitedNodes.add(i)
                queue.push(i)
                spanningTree.add_edge(pointer, i)
    return spanningTree, sequence


    


def DFS(graph, root):
    """
    Performs a Depth-First Search on a given graph starting
	from root node to output a spanning subgraph of the
	original graph, the sequence of visited nodes.
    """
    #Your code here

    visitedNode = set()
    stack = Stack()
    sequence = []
    spanningTree = nx.Graph()

    stack.push(root)
    visitedNode.add(root)

    while not stack.is_empty():
        pointer = stack.pop()
        sequence.append(pointer)

        for i in reversed(list(graph.neighbors(pointer))):
            if i not in visitedNode:
                visitedNode.add(i)
                stack.push(i)
                spanningTree.add_edge(pointer, i)
    return spanningTree, sequence

def show_graph(graph):
    plt.subplot(111)
    pos = nx.spring_layout(graph, seed=11)
    nx.draw(graph, with_labels=True, font_weight='bold', pos=pos)
    plt.show()

def create_tree():
    g = nx.Graph()
    for i in range(7):
        source = i if i != 3 else 0
        g.add_edge(source, i+1)
    return g


graph = nx.erdos_renyi_graph(12, 0.25, seed=42)

show_graph(graph)
BFSspan, BFSseq = BFS(graph, 0)
DFSspan, DFSseq = DFS(graph, 0)

print ("BFS Seguence: ", BFSseq)
print ("DFS Seguence: ", DFSseq)
show_graph(graph)

graph =  create_tree()
show_graph(graph)
BFSspan, BFSseq = BFS(graph, 0)
DFSspan, DFSseq = DFS(graph, 0)

print ("BFS Seguence: ", BFSseq)
print ("DFS Seguence: ", DFSseq)
show_graph(graph)


