def bfs(graph, capacity, flow, source, sink, parent):
    queue = [source]
    visited = {source}

    while queue:
        current = queue.pop(0)
        for neighbor in graph.get(current, []):
            residual = capacity.get((current, neighbor), 0) - flow.get((current, neighbor), 0)
            if neighbor not in visited and residual > 0:
                visited.add(neighbor)
                parent[neighbor] = current
                if neighbor == sink:
                    return True
                queue.append(neighbor)
    return False

def edmonds_karp(graph, capacity, source, sink):
    flow = {}
    max_flow = 0
    parent = {}

    while bfs(graph, capacity, flow, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            u = parent[s]
            residual = capacity.get((u, s), 0) - flow.get((u, s), 0)
            path_flow = min(path_flow, residual)
            s = u

        v = sink
        while v != source:
            u = parent[v]
            flow[(u, v)] = flow.get((u, v), 0) + path_flow
            flow[(v, u)] = flow.get((v, u), 0) - path_flow
            v = u

        max_flow += path_flow

    return max_flow

def main():
    filename = 'roads.csv'
    graph = {}
    capacity = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            farms = [x.strip() for x in file.readline().split(',')]
            shops = [x.strip() for x in file.readline().split(',')]

            for line in file:
                parts = [x.strip() for x in line.split(',')]
                if len(parts) == 3:
                    u, v, cap = parts[0], parts[1], int(parts[2])

                    if u not in graph:
                        graph[u] = []
                    if v not in graph:
                        graph[v] = []
                    graph[u].append(v)
                    graph[v].append(u)

                    capacity[(u, v)] = cap

        source = 'SOURCE'
        sink = 'SINK'

        if source not in graph:
            graph[source] = []
        if sink not in graph:
            graph[sink] = []

        for farm in farms:
            graph[source].append(farm)
            graph[farm].append(source)
            capacity[(source, farm)] = float('inf')

        for shop in shops:
            graph[shop].append(sink)
            graph[sink].append(shop)
            capacity[(shop, sink)] = float('inf')

        maxflow = edmonds_karp(graph, capacity, source, sink)
        print(f"Maximum number of cars: {int(maxflow)}")

    except FileNotFoundError:
        print("File roads.csv is not found.")

if __name__ == "__main__":
    main()


