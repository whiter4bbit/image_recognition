from layer import Layer, Connection
from node import Node
#from utils.utils import pretty_print
#from utils.utils import normalize, denormalize

class InputLayer(Layer):
    def __init__(self, N):
        Layer.__init__(self, N)

class HopfieldLayer(Layer):
    def __init__(self, N):
        Layer.__init__(self, N)

    def train(self, X, k):
        backward = self.backward_layers[0]
        figure_node = self.nodes[k]
        weights = []
        for i in xrange(len(figure_node.backwards)):
            con = figure_node.backwards[i]
            con.weight = .5*X[i]
            weights.append(con.weight)

class HopfieldOutputLayer(Layer):
    def __init__(self, N, hopfield_prev):
        Layer.__init__(self, N)
        assert hopfield_prev
        self.hopfield_prev = hopfield_prev

    def forward(self, c):
        prev_values = [node.value for node in self.hopfield_prev.nodes]
        self.set_values(prev_values)
        for i in xrange(len(self.nodes)):
            filtered = []
            for j in xrange(len(prev_values)):
                if j!=i: filtered.append(prev_values[j])
            self.nodes[i].value -= c*sum(filtered)
        for node in self.nodes:
            if node.value<=0:
                node.value = 0
        self.hopfield_prev.set_values(self.get_values())
        return self.get_values()

class HammingNetw(object):
    def __init__(self, N, K):
        self.N = N
        self.K = K
        self.layers = []
        self.figures = 0
        self.max_iters = 100
        self.__init_layers()

    def __init_layers(self):
        self.layers.append(InputLayer(self.N))
        self.layers.append(HopfieldLayer(self.K))
        self.layers.append(HopfieldOutputLayer(self.K, self.layers[1]))
        self.layers[0].connect(self.layers[1])
        self.layers[1].connect(self.layers[2])

    def train(self, figure):
        self.layers[1].train(figure, self.figures)
        self.figures+=1

    def forward(self, figure):
        self.layers[0].set_values(figure)
        last = self.layers[1].forward()
        for iter_ in xrange(self.max_iters):
            current = self.layers[2].forward(.09)
            if current == last: break
            last = current
        recognized = 0
        for i in xrange(len(last)):
            if last[i]>0:
                recognized = i
                break
        return (iter_!=self.max_iters, recognized, iter_)

from parser import parse, from_array

if __name__=="__main__":
    train_figures = {'/home/whiter4bbit/programming/python/hopfild/test/images_trained/': ['0', '1', '2', '3','4', '5', '6', '7', '8', '9']}
    test_figures = {'/home/whiter4bbit/programming/python/hopfild/test/images_damaged/': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}
    netw = HammingNetw(100, 10)
    for path, figures in train_figures.iteritems():
        for figure in figures:
            ic = ImageConvertor(path+figure+'.png')
            array = from_array(ic.get_array(), '*')
            netw.train(normalize(array))

    for path, figures in test_figures.iteritems():
        for figure in figures:
            ic = ImageConvertor(path+figure+'.png')
            array = from_array(ic.get_array(), '*')
            res = netw.forward(normalize(array))
            if res[0]:
                print "%s {recognized=%d}{%d}[ok]" % (path+figure, res[1], res[2])
            else:
                print "%s{%d}[fail]" % (path+figure, res[2])
