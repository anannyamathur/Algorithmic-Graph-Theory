import networkx as nx
 
#importing the matplotlib library for plotting the graph
import matplotlib.pyplot as plt

def k_edge(n,p,k):
    G=nx.erdos_renyi_graph(n,p)

    cc=sorted(map(sorted, nx.k_edge_components(G, k)))
    
    max_cc=0
    for i in range(len(cc)):
        max_cc=max(max_cc,len(cc[i]))
    return cc, len(cc), max_cc

print(k_edge(10,0.5,3))