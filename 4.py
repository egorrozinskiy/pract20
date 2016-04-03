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

def bfs_fire(G, P, start, fired):
    fired.add(start)
    queue=[start]
    while len(queue)!=0:
        current = queue.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                P.add_edge(current, neighbour)
                fired.add(neighbour)
                queue.append(neighbour)
    for i in G:
        if i not in fired:
            bfs_fire(G, P, i, fired)

P = nx.Graph()
fired = set()
G = graf()
komponents = 0
for j in G:
    if j not in fired:
        komponents+=1
if komponents==1:
    print('Граф связный')
else:
    print('Граф не связный')

bfs_fire(G,P,'1', fired)
print('Компоненты связности:', fired)
