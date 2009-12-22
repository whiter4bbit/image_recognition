from utils import multiply, apply, sign
from params import MAX_ITERS

class HopfieldNetw:
    def __init__(self, N, M):
        self.M = M
        self.N = N
        self.L = M*N
        self.w = [[0 for i in xrange(self.L)] for j in xrange(self.L)]
        self.figures = []

    def learn(self, figure):
        self.figures.append(figure)
        for i in xrange(self.L):
            for j in xrange(self.L):
                if i==j:
                    self.w[i][j] = 0
                else:
                    self.w[i][j] += figure[i]*figure[j]

    def recognize(self, figure):
        self.X = [figure]
        iters = 0
        while iters<MAX_ITERS:
            new = apply(multiply(self.X, self.w), sign)
            if self.X == new:
               break
            self.X = new
            iters+=1
        if iters==MAX_ITERS:
            return (False, self.X, iters)
        return (True, self.X, iters)

class HammingNetw:
    def __init__(self, N, M, K):
        self.M = M
        self.N = N
        self.K = K
        self.L = M*N

from parser import parse
from utils import normalize, pretty_print, denormalize

class Recognize(object):
    def __init__(self, train_path, train_sequence):
       self.load_figures(train_path, train_sequence)
       self.netw = HopfieldNetw(self.n, self.m)
       self.train()

    def load_figures(self, path, sequence):
       self.figures = []
       for fig in sequence:
          figure_path = path+'/'+fig
          array = parse(figure_path , '*')
          self.n, self.m = len(array), len(array[0])
          self.figures.append(normalize(array))

    def train(self):
       for figure in self.figures:
          self.netw.learn(figure)

    def recognize(self, path):
       figure = parse(path, '*')
       res = self.netw.recognize(normalize(figure))
       if res[0]:
           print "%s[ok] in %d iters" % (path, res[2])
           pretty_print(denormalize(res[1], self.m, self.n))
       else:
           print "%s[fail]" % path
           pretty_print(denormalize(res[1], self.m, self.n))


if __name__=="__main__":
    r = Recognize('trained_images', ['0', '1', '2'])
    test = {'damaged_images': ['0', '1', '2']}
    for path, files in test.iteritems():
         for file in files:
            r.recognize(path+'/'+file)


