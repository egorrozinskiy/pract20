import networkx as nx

def graf():
    N = int(input())
    G = {}
    for i in range(int(input())):
        a, b = input().split()
        if a not in G:
            G[a] = {b}
        else:
            G[a].add(b)
        if b not in G:
            G[b] = {a}
        else:
            G[b].add(a)
    return G  
    
def bfs_fire(G,start,fired):
    Q=[start]
    fired.add(start)
    while len(Q)!=0:
        current=Q.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                P.add_edge(current, neighbour)                    
                fired.add(neighbour)
                Q.append(neighbour)
P = nx.Graph()
G = graf()
fired=set()
bfs_fire(G,'1', fired)
print('??????? ? ?????????? ?????????:', fired)