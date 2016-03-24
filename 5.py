import networkx as nx
def graf():
    G = {}
    M = int(input())
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        if a not in G:
            G[a] = {b:weight}
        else:
            G[a][b] = weight
        if b not in G:
            G[b] = {a:weight}
        else:
            G[b][a] = weight
    return G       
    
         
def deikstra(G,start):
    shortest_path={vertex:float('+inf') for vertex in G}
    shortest_path[start]=0
    queue=[start]
    while len(queue)!=0:
        current=queue.pop(0)
        print(current, shortest_path[current])
        for neighbour in G[current]:
            offering_shortest_path=shortest_path[current]+G[current][neighbour]
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour]=offering_shortest_path
                queue.append(neighbour)
    return shortest_path
    
    
def main():
    G=graf()
    start=input()
    shortest_path = deikstra(G,start)
    print('Кратчайшие пути:')
    for vertex in G:
	    print(vertex, shortest_path[vertex])
	    
if __name__ == '__main__':
    main()
	
