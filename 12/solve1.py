from collections import defaultdict

with open("./example.txt", "r") as f:
    data = f.read()

graph = defaultdict(list)
for line in data.splitlines():
    v1, v2 = line.split("-")
    # print(line, v1, v2)
    if v1 in graph.keys():
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]

    if v1 != "start" and v2 != "end":
        if v2 in graph.keys():
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]


visited = set()
paths = []
print(graph)


def prettyprint(X):
    for x in X:
        print(x, "\n")


def dfs(visited, graph, vertex, path=[]):
    try:

        path.append(vertex)
        if not vertex.isupper():
            visited.add(vertex)
        if vertex == "end":
            paths.append(path)
            # print("visited=", visited, "v=", vertex, "n=", graph[vertex], "path=", path)
        for neighbor in graph[vertex]:
            # print(v)
            if neighbor not in visited:
                dfs(visited.copy(), graph, neighbor, path.copy())
    except KeyError:
        return


dfs(visited, graph, "start")
prettyprint(paths)
print(len(paths))
