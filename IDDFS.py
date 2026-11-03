graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(graph, node, depth):
    print(node, end=" ")

    if depth == 0:
        return

    for neighbor in graph[node]:
        dls(graph, neighbor, depth - 1)

def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print("\nDepth", depth, ":")
        dls(graph, start, depth)

iddfs(graph, 'A', 2)