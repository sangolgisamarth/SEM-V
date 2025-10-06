def dijkstra(graph, source):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0  # distance to itself is 0

    for _ in range(n):
        # pick the unvisited vertex with smallest distance
        min_dist = float('inf')
        # u will store the index of the unvisited vertex with the smallest distance in this
        u = -1 ## we initialize becouse we haven't find the any vertex
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        visited[u] = True  # mark it visited

        # update distances of neighbors
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist

# Example usage
graph = [
    [0, 1, 4, 0],
    [1, 0, 4, 2],
    [4, 4, 0, 3],
    [0, 2, 3, 0]
]

source = 0  # starting from vertex 0
distances = dijkstra(graph, source)
print("Shortest distances from vertex 0:", distances)
