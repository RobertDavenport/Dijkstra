import sys


def create_graph(file):
    index = []  # This node at each index in the input adjacency matrix's header
    nodes = []
    dists = {}
    with open(file) as topology:

        # ================== Process header line
        line = topology.readline()
        # Strip the header line of whitespace
        line = line.strip('\n')
        # Split the header line into a list
        line = line.split(',')
        # the (0,0) of the adjacency matrix is null
        index.append("")

        for i in range(1, len(line)):
            index.append(line[i])

        # Process until the end-of-file
        while(True):
            line = topology.readline()
            # Strip the header line of whitespace
            line = line.strip('\n')
            # Split the header line into a list
            line = line.split(',')

            if(len(line) > 1):  # Detects EOF
                nodes.append(line[0])
                dists[line[0]] = {}
                for i in range(1, len(line)):
                    dists[line[0]][index[i]] = int(line[i])
            else:
                return nodes, dists


def dijkstra(nodes, dists, start):
    MAX = 9999
    dist = {}
    prev = {}
    pq = []

    for n in nodes:
        dist[n] = MAX
        prev[n] = []
        pq.append(n)

    dist[start] = 0
    while(len(pq) > 0):
        u = min_dist(MAX, dist, pq)
        pq.remove(u)
        for node, weight in dists[u].items():
            d = dist[u] + weight
            if d <= dist[node]:
                dist[node] = d
                prev[node].append(u)
                if(node == 'z' or u == 'z'):
                    print(prev[node])


    return dist, prev


def min_dist(max, dist, q):
    mind = max
    minn = q[0]
    for n in q:
        if(dist[n] < mind):
            mind = dist[n]
            minn = n
    return minn


def path(prev,u):
    print(u, prev[u])
    print()


# MAIN
# Run Dijkstra algorithm on source csv and user specified start node
# dist, prev = dijkstra(create_graph("topology-1.csv"), "u")

nodes, dists = create_graph("topology-1.csv")
#print(nodes)
#print(dists)
dist, prev = dijkstra(nodes, dists, "u")

#for node in dist.keys():
#    dist, prev = dijkstra2(create_graph("topology-1.csv"), node)
#    print("Distance vector for node {}: {}".format(node, dist.values()))


print("DIST: ", dist)
for node in nodes:
    path(prev, node)
"""
print("PREV:")
for u in nodes:
    u2 = u
    S = []
    if (prev[u] is not None):
        while u is not None:
            S.append(u)
            try:
                u = prev[u].pop()
            except:
                break
    print(u2, "::", S[::-1], end=" ")
    tot = 0
    for i in range(len(S) - 1):
        links = graph[S[i]].get_links()
        tot += links[S[i + 1]][1]
    print(tot)"""

