from node import Node

class Connection(object):
    def __init__(self, backward, forward):
        self.backward = backward
        self.forward = forward
        self.weight = 0.0

class Layer(object):
    def __init__(self, N):
        self.nodes = [Node() for i in xrange(N)]
        self.forward_layers = []
        self.backward_layers = []

    def train(self):
        pass

    def connect(self, layer):
        for node in self.nodes:
            for forw_node in layer.nodes:
                node.forwards.append(Connection(node, forw_node))
                forw_node.backwards.append(Connection(node, forw_node))
        layer.backward_layers.append(self)
        self.forward_layers.append(layer)

    def set_values(self, values):
        if len(values)!=len(self.nodes):
            raise ValueError("Values have wrong leght")
        for i in xrange(len(values)):
            self.nodes[i].value = values[i]

    def get_values(self):
        return [node.value for node in self.nodes]

    def forward(self):
        for node in self.nodes:
            node.activate()
        return self.get_values()
