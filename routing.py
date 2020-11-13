import sys
import heapq


class Node(object):
    def __init__(self, name):
        self._name = name
        self._weights = {}
        
    def add_link(self, other, weight):
        self._weights[other.name] = (other, weight)

    @property
    def name(self):
        return self._name

    # Returns a dictionary of this node's links.
    # Each link is stored as a key,value pair of
    # the linked node's name as the key, and a tuple
    # of object representing the linked node, and
    # the link's weight as the value.
    def get_links(self):
        return self._weights

    def __str__(self):
        return self._name


# Returns a dictionary holding every node in the graph.
# The dictionary is addressable by the name (letter)
# representing a node.
def create_graph(file):
    graph = {}  # Stores the input data in a graph of nodes
    index = []  # This node at each index in the input adjacency matrix's header
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
            n = Node(line[i])
            graph[line[i]] = n
            index.append(line[i])

        # Process until the end-of-file
        while(True):
            line = topology.readline()
            # Strip the header line of whitespace
            line = line.strip('\n')
            # Split the header line into a list
            line = line.split(',')

            if(len(line) > 1):  # Detects EOF
                curr_node = graph[line[0]]
                for i in range(1, len(line)):
                    curr_node.add_link(graph[index[i]], int(line[i]))
            else:
                return graph


# does not wok yet, need to review with Alex.
def dijkstra(graph, start):
    shortestEdge = 9999
    for key, value in graph.items():
        if (key == start):
            # get edges
            for edge in value.get_links:
                if (edge < shortestEdge):
                    shortestEdge = edge


def dijkstra2(graph, start):
    start = graph[start]
    Q = []
    for node in graph.values():
        Q.append(node)
    MAX_EDGE = 9999
    dist = {}
    prev = {}

    for node in graph.values():
        dist[node.name] = MAX_EDGE
        prev[node.name] = []
    dist[start.name] = 0

    u = None
    ls = []
    while(len(Q) > 0):
        if(u is None):
            u = Q[0]
            Q.remove(u)
        else:
            u = min_dist(Q, dist, MAX_EDGE)

        for edge in u.get_links().values():
            alt = dist[u.name] + edge[1]
            if (alt < dist[edge[0].name]):
                dist[edge[0].name] = alt
                prev[edge[0].name].append(u)

    return dist, prev

def bellmanFord(graph, start):
    start = graph[start]
    Q = []
    for node in graph.values():
        Q.append(node)
    MAX_EDGE = 9999
    dist = {}
    prev = {}

    for node in graph.values():
        dist[node.name] = MAX_EDGE
        prev[node.name] = []
    dist[start.name] = 0

    u = None
    ls = []

    for node in graph.values():
        #this won't work
        print("NODE-----------------")
        for edge in node.get_links().values():
            #print(edge)
            tempDist = dist[edge[node]]
            print(tempDist)
            # if(tempDist < dist[node.name]):
            dist[edge[0].name] = tempDist
            prev[edge[0].name].append(node.name)

    return dist, prev


def min_dist(Q, dist, MAX_EDGE):
    minv = MAX_EDGE
    ret = Q[0]
    for node in Q:
        if(dist[node.name] < minv):
            minv = dist[node.name]
            ret = node
    Q.remove(ret)
    return(ret)

# MAIN
# Run dikstra algorithim on source csv and user specified start node
dist,prev = dijkstra2(create_graph("topology-1.csv"), "u")

print("shortest path tree for node:" + "u")
print 
print("DIST: ",dist)
print("PREV:")
for key, list in prev.items():
    print(key)
    for node in list:
        print(node.name,end="\t")

beldist, belprev = bellmanFord(create_graph("topology-1.csv"), "u")
print("BELFORD DIST : ", beldist)


# for node in dist.keys():
#     dist, prev = bellmanFord(create_graph(sys.argv[1]), node)
#     vector = dist.values()
#     print("Distance vector for node {}: {}".format(node, vector))
