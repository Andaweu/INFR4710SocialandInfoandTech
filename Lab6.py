import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
import community as community_louvian
from cdlib import algorithms
from cdlib import evaluation
import igraph as ig



def load(gmlFile):
    try: #attempts to read the gml file
        graph = nx.read_gml(gmlFile)
        print("Graph loaded")
        return graph #returns the graph as a file
    except Exception as e: #exit if graph cannot load
        print("Failed to load graph")
        exit()


def averageDegree(graph):

    degrees = dict(graph.degree()) 
    averageDegree = sum(degrees.values()) / len(degrees) #calculates for the average degree
    return averageDegree

    

def largestComponent(graph):
    if not nx.is_connected(graph): #checks if the graph is connected
        GCC = max(nx.connected_components(graph), key=len)
        subGraph = graph.subgraph(GCC).copy()
        print("Not connected, Largest Component used")
    else:
        subGraph = graph #if not connected, returns the largest subgraph
    return subGraph


def averagePath(graph):
    try:
        usedGraph = largestComponent(graph) #takes either the connected graph or largest component
        return nx.average_shortest_path_length(usedGraph) #returns the shortest path on the graph
    except Exception as e: #error code should the graph not work
        return "Error computing path length."
    
def largerDiameter(graph):
    try:
        usedGraph = largestComponent(graph) #takes either the connected graph or largest component
        return nx.diameter(usedGraph) #returns the diameter of the graph
    except Exception as e: #error code should the graph not work
        return "Error computing diameter"
    

    
def greatestDegree(graph):
    degrees = dict(graph.degree())
    return max(degrees.items(), key=itemgetter(1)) #returns the highest degree from the node dictionary

def greatestBetweenness(graph):
    betweenness = nx.betweenness_centrality(graph)
    return max(betweenness.items(), key=itemgetter(1)) #returns the value with the highest betweenness

def betweenness(graph):
    return nx.betweenness_centrality(graph) #returns the betweenness of the graph



#community algorithms

def louvianAlgorithm(graph):
    partition = community_louvian.best_partition(graph) #uses the louvian algorithm to find communities
    return len(set(partition.values())) #returns the number of communities found

def supriseAlgorithms(graph):
    communities = algorithms.surprise_communities(graph) #uses the suprise algorithm to find communities
    return len(communities.communities) #returns the number of communities found

def walkTrapAlgorithm(graph):
    igGraph = ig.Graph() #creates an empty graph
    igGraph.add_vertices(list(graph.nodes())) #adds the graphs vertices
    igGraph.add_edges(list(graph.edges())) #adds the graphs edges

    walktrap = igGraph.community_walktrap() #uses the walktrap algorithm to find communities
    clusters = walktrap.as_clustering() #converts the result into clusters
    return len(clusters) #returns the number of communities found


#graph plotting

def betweennessPlot(graph):
    #plots a graph using the maxBetweenness
    maxBetweenness = nx.betweenness_centrality(graph)

    values = list(maxBetweenness.values())
    plt.figure(figsize=(10,10))
    values.sort(reverse=True)
    plt.loglog(values, marker="o", linestyle='None')
    plt.title("LogLog Betweenness")
    plt.grid(True)
    plt.show()


#running the functions

test = load("netscience.gml")
print(averageDegree(test))
print(averagePath(test))
print(largerDiameter(test))
print(greatestDegree(test))
print(greatestBetweenness(test))
print("Louvian Communities detected: ", louvianAlgorithm(test))
print("Suprise Communities detected: ", supriseAlgorithms(test))
print("WalkTrap Communities detected", walkTrapAlgorithm(test))



betweennessPlot(test)


