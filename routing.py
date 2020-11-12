import csv
import sys


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
                
# MAIN
# Run dikstra algorithim on source csv and user specified start node
dijkstra(create_graph(sys.argv[1]), sys.argv[2])
