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

print(graph)

visited = set()
paths = []


def prettyprint(X):
    for x in X:
        print(x, "\n")


C = defaultdict()
C = {x: 0 for x in graph.keys() if x.islower()}
C["end"] = 0
C["start"] = 0
print(C)


def dfs(visited, graph, vertex, path=[], cc=C):
    try:
        # if big cave, just append
        # if small cave, if we already visited an island twice,
        #   if cave to be added already visited twice, don't append
        #   else cave is not the one we visited twice before, so we append and add to visited
        # if small cave and we have no visited any island twice
        #   add path and increase count
        # another small cave already visited twice
        max_c = max(cc.values())
        # print(max_c, cc)
        if vertex.isupper():
            path.append(vertex)

        if vertex == "start" and cc["start"] == 1:
            visited.add(vertex)
            return

        if vertex == "end" and cc["end"] == 1:
            visited.add(vertex)
            return

        if vertex.islower() and max_c == 2:
            # print("lower", vertex)
            if cc[vertex] == 0:
                cc[vertex] += 1
                path.append(vertex)
            else:
                visited.add(vertex)
                return

        if vertex.islower() and max_c < 2:
            cc[vertex] += 1
            path.append(vertex)

        if vertex == "end":
            paths.append(path)
        for neighbor in graph[vertex]:
            # print("v=", vertex, "n=", neighbor, "graph=", graph[vertex], path)
            if neighbor not in visited:
                dfs(visited.copy(), graph, neighbor, path.copy(), cc.copy())
    except KeyError:
        pass


dfs(visited, graph, "start")
prettyprint(paths)
print(len(paths))
