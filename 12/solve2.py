from collections import defaultdict

with open("./input.txt", "r") as f:
    data = f.read()

graph = {}
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


def prettyprint(X):
    for x in X:
        print(x, "\n")


C = {x: 0 for x in graph.keys() if x.islower()}


def dfs(visited, graph, vertex, path=[], cc=C):
    try:
        max_c = max(cc.values())
        if vertex.isupper():
            path.append(vertex)

        if vertex == "start" and cc[vertex] == 1:
            return

        if vertex == "end":
            paths.append(path)
            return

        if vertex.islower() and max_c >= 2:  # already visited a small cave twice
            if cc[vertex] == 0:  # new visit
                cc[vertex] += 1
                path.append(vertex)
            else:  # visited twice
                visited.add(vertex)
                return

        if vertex.islower() and max_c < 2:
            cc[vertex] += 1
            path.append(vertex)

        for neighbor in graph[vertex]:
            # print("v=", vertex, "n=", neighbor, "graph=", graph[vertex], path)
            if neighbor not in visited:
                dfs(visited.copy(), graph, neighbor, path.copy(), cc.copy())
    except KeyError:
        pass


dfs(visited, graph, "start")
# prettyprint(paths)
print(len(paths))
