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
        for neighbor, weight in graph[u].items():
            # --------- Updates link values for nodes without direct connections
            for node2, weight2 in graph[neighbor].items():
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
            # --------- Updates link values for nodes without direct connections --------
            for node2, weight2 in graph[neighbor].items():
                if (graph[node][neighbor] + graph[neighbor][node2] < graph[node][node2]):
                    graph[node][node2] = graph[node][neighbor] + graph[neighbor][node2]
                    graph[node2][node] = graph[node][neighbor] + graph[neighbor][node2]
            # ---------------------------------------------------------------------------
            distance = dist[neighbor] + weight
            if(distance < dist[node]):
                dist[node] = distance
                prev[node].append(neighbor)
    for node in nodes:
        for neighbor, weight in graph[node].items():
            if(dist[node] + graph[node][neighbor] < dist[neighbor]):
                print("Negative Cycle")
    return dist, prev


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

file = "topology-1.csv"
source_node = input("Please, provide the source node: ")
print("Shortest path tree for node {}:".format(source_node))

nodes, graph = create_graph(file)  # Create the graph from the input file.

# Find the shortest path tree and cost of least-cost
# paths using Dijkstra's algorithm.
dists, paths = dijkstra(nodes, graph, source_node)
for i, path in enumerate(paths.values()):   # Prints shortest paths.
    for char in path:
        print(char, end="")
    if(i+1<len(paths)):
        print(", ", end="")
print()
print("Costs of the least-cost paths for node u:")
for i, item in enumerate(dists.items()):    # Prints cost of least cost paths.
    if(i+1<len(dists)):
        print(item[0]+":"+str(item[1]), end=", ")
    else:
        print(item[0] + ":" + str(item[1]), end="\n\n")

# Print the distance vectors the the graph using the
# BellmanFord equation
for start in nodes:
    dist, prev = bellman_ford(nodes, graph, start)
    d_vector = ""
    for val in dist.values():
        d_vector += str(val) + " "
    print("Distance vector for node {}: {}".format(start, d_vector))
