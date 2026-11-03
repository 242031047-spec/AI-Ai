graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(graph, node, limit):
    print(node, end=" ")

    if limit == 0:
        return

    for neighbor in graph[node]:
        dls(graph, neighbor, limit - 1)

dls(graph, 'A', 2)