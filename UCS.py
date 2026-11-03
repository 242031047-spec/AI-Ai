import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1), ('G', 3)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def ucs(graph, start, goal):
    queue = [(0, start)]
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nTotal Cost:", cost)
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    queue, (cost + weight, neighbor)
                )

ucs(graph, 'A', 'G')