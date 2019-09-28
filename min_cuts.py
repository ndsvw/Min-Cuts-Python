import random


def union_vertices(G, v, u):
    G[u] = [z for z in G[u] if z != v]
    G[v] = [z for z in G[v] if z != u]
    for x in G[v]:
        G[u].append(x)
        G[x] = [z if z != v else u for z in G[x]]
    G[v] = []
    return G


def count_probable_min_cuts(G):
    vertices_remaining = [i for i in range(len(G))]

    while len(vertices_remaining) > 2:
        r = random.randint(0, len(vertices_remaining)-1)
        x = vertices_remaining.pop(r)
        y = random.choice(G[x])
        union_vertices(G, x, y)

    for u in range(len(G)):
        if len(G[u]) > 0:
            return len(G[u])
