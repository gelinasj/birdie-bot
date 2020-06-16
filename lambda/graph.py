from node import Node

class Graph:

    def __init__(self):
        self.node_map = {}
        self.edge_map = {}

    def __str__(self):
        return(self.node_map.__str__())

    def create_node_if_dne(self, word):
        return(self.node_map.setdefault(word, Node(word)))

    def get_node(self, word):
        return(self.node_map.get(word))

    def get_edge(self, edge_count):
        return(self.edge_map.get(edge_count))

    def create_edge(self, in_node, edge_count, out_node):
        edge = out_node.add_incoming_edge(in_node, edge_count)
        return(self.edge_map.setdefault(edge_count, edge))
