def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)

    for nxt in graph[node]:
        if nxt not in visited:
            dfs(graph, nxt, visited)

    return visited