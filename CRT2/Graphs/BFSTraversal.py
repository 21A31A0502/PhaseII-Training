def initiateBFSTraversal(node, visited, adj, result):
    Q = [node]
    visited[node] = True
    while Q:
        currNode = Q.pop(0)
        result.append(currNode)
 
        for neighbour in adj[currNode]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)
 
def printBFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateBFSTraversal(node,visited, adj, result)
    print("BFS Traversal is: ", result)

n, m = map(int, input().split())
# n is no.of nodes 
# m is no.of edges 
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
#printBFSTraversal(adj, n)
printBFSTraversal(adj, n) 

#output
'''
3 3
1 2
2 1
0 1
BFS Traversal is:  [0, 1, 2]
'''   