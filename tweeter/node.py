from tweeter.edge import Edge

class Node:

    def __init__(self, word):
        self.word = word
        self.incoming = []
        self.outgoing = []

    def add_incoming_edge(self, incoming_node, edge_count):
        edge = Edge(incoming_node, edge_count, self)
        self.incoming.append(edge)
        incoming_node.outgoing.append(edge)
        return edge
