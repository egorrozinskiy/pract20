def graph_input():
    G={}
    M=int(input())
    for i in range (M):
        a,b,weight = input().split()
        weight=float(weight)
        if a not in G:
            G[a]={b:weight}
        else:
            G[a][b]=weight
        if b not in G:
            G[b]={a:weight}
        else:
            G[b][a]=weight
    return G
def dejkstra(G,start):
    shortest_path={vertex:float('+inf') for vertex in G}
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current=queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current]+(G[current][neighbour])
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour]=offering_shortest_path
                queue.append(neighbour)
    return shortest_path
G=graph_input()
start=input()
shortest_path=dejkstra(G, start)
for vertex in G:
    print(vertex,shortest_path[vertex])
finish = input()                 
shortest_path = dejkstra(G, start)
path  = [finish]    
current = finish
while current != start:
       for vertex in G[current]:
           if current != start:
               if shortest_path[current] - G[current][vertex] == shortest_path[vertex]:
                   current = vertex
                   path.append(current) 
           else:
               break
print(path[::-1])
