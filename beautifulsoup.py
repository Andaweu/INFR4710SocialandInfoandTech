from bs4 import BeautifulSoup
import urllib2 as urllib
import networkx as nx
import matplotlib.pyplot as plt

def findUrls(root):
    #Your code here

    return graph


"""
CODE TO TEST YOUR FUNCTIONS BEGINS HERE (DON'T MODIFY)
"""

url = "http://google.ca"

graph = findUrls(url)
plt.subplot(111)
nx.draw(graph, with_labels=True)
plt.show()
print('\n Graph Nodes = ', graph.nodes)
print('\n Number of URLs = ', len(graph.nodes))
