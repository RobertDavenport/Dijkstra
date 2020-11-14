import sys, heapq


# Parses the csv file into a graph
def create_graph(file):
    index = []  # This node at each index in the input adjacency matrix's header
    nodes = []  # List of nodes
    dists = {}  # Graph
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


def dijkstra(nodes, graph, start):
    MAX = 9999  # Max value, representing no connection in graph.
    dist = {}   # Stores distance from start to every node
    prev = {}   # Dictionary, stores shortest path to every node from start
    pq = []     # Stores unpathed nodes
    for n in nodes:
        dist[n] = MAX
        prev[n] = []
        pq.append(n)    # Adds all nodes to the unpathed list
    dist[start] = 0     # Distance from start -> start is 0

    while(len(pq) > 0): # Iterate through every unpathed node
        u = min_dist(MAX, dist, pq)     # Select the node with the lowest distance to start
        pq.remove(u)                    # Remove the node from the unpathed nodes
        for neighbor, weight in dists[u].items():
            # --------- Updates link values for nodes without direct connections
            for node2, weight2 in dists[neighbor].items():
                if(graph[u][neighbor]+graph[neighbor][node2] < graph[u][node2]):
                    graph[u][node2] = graph[u][neighbor]+graph[neighbor][node2]
                    graph[node2][u] = graph[u][neighbor]+graph[neighbor][node2]
            #-------------------------------------------------------------------
            distance = dist[u] + weight     # Compute distance to start node
            if distance <= dist[neighbor]:  # If this distance is less than the previous,
                dist[neighbor] = distance   # this is the new distance; add it to the path.
                prev[neighbor].append(u)
    return dist, prev

def bellman_ford(nodes, graph, start):
    MAX = 9999  # Max value, representing no connection in graph.
    dist = {}   # Stores distance from start to every node
    prev = {}   # Dictionary, stores shortest path to every node from start
    pq = []     # Stores unpathed nodes
    for n in nodes:
        dist[n] = MAX
        prev[n] = []
        pq.append(n)    # Adds all nodes to the unpathed list
    dist[start] = 0     # Distance from start -> start is 0


    for node in nodes:
        for neighbor, weight in graph[node].items():
            distance = dist[neighbor] + weight
            if(distance < dist[node]):
                dist[node] = distance
                prev[node].append(neighbor)
    for node in nodes:
        for neighbor, weight in graph[node].items():
            if(dist[node] + graph[node][neighbor] < dist[neighbor]):
                raise Exception("Negative Cycle")
"""
    while(len(pq) > 0): # Iterate through every unpathed node
        u = min_dist(MAX, dist, pq)     # Select the node with the lowest distance to start
        pq.remove(u)                    # Remove the node from the unpathed nodes
        for neighbor, weight in dists[u].items():
            # --------- Updates link values for nodes without direct connections
            for node2, weight2 in dists[neighbor].items():
                if(graph[u][neighbor]+graph[neighbor][node2] < graph[u][node2]):
                    graph[u][node2] = graph[u][neighbor]+graph[neighbor][node2]
                    graph[node2][u] = graph[u][neighbor]+graph[neighbor][node2]
            #-------------------------------------------------------------------
            distance = dist[u] + weight     # Compute distance to start node
            if distance <= dist[neighbor]:  # If this distance is less than the previous,
                dist[neighbor] = distance   # this is the new distance; add it to the path.
                prev[neighbor].append(u)
    return dist, prev"""

# Finds the node in the graph with the lowest
# distance value
def min_dist(max, dist, q):
    mind = max
    minn = q[0]
    for n in q:
        if(dist[n] < mind):
            mind = dist[n]
            minn = n
    return minn



# MAIN
# Run Dijkstra algorithm on source csv and user specified start node

nodes, dists = create_graph("topology-1.csv")