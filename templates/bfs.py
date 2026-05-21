from collections import deque

def bfs(graph, start):
    visited = set([start])
    q = deque([start])

    while q:
        node = q.popleft()

        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    return visited