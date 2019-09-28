import random


def union_vertices(G, v, u):
    # unions 2 vertices, self loops are removed
    G[u] = [z for z in G[u] if z != v]
    G[v] = [z for z in G[v] if z != u]
    for x in G[v]:
        G[u].append(x)
        G[x] = [z if z != v else u for z in G[x]]
    G[v] = []
    return G


def count_probable_min_cuts(G):
    # tries to count the min cuts.
    # probablity to succeed is low.
    # so it should be executed multiple times and the
    # min value of all executions should be remembered
    vertices_remaining = [i for i in range(len(G))]

    while len(vertices_remaining) > 2:
        r = random.randint(0, len(vertices_remaining)-1)
        x = vertices_remaining.pop(r)
        y = random.choice(G[x])
        union_vertices(G, x, y)

    for u in range(len(G)):
        if len(G[u]) > 0:
            return len(G[u])

    return 0
