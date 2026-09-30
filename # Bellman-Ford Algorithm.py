# Bellman-Ford Algorithm

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges: source destination weight")

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex: "))

# Initially, distance is infinity
distance = [999999] * n
distance[source] = 0

# Relax all edges n-1 times
for i in range(n - 1):

    for u, v, w in edges:

        if distance[u] != 999999:

            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w


# Check for negative weight cycle
negative_cycle = False

for u, v, w in edges:

    if distance[u] != 999999:
        if distance[u] + w < distance[v]:
            negative_cycle = True
            break


if negative_cycle:
    print("Negative weight cycle exists")

else:
    print("\nShortest distances from", source)

    for i in range(n):
        print(source, "->", i, "=", distance[i])