import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
N=int(input())
M = int(input())
for i in range(M):
    a = list(input().split())
    if len(a) > 1:
        G.add_edge(a[0], a[1])
    else:
        G.add_node(a[0])            
nx.draw(G)
plt.savefig("simple_path.png") 
plt.show() 
