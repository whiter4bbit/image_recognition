def multiply(a,b):
    c = [[0 for i in xrange(len(b[0]))] for j in xrange(len(a))]
    for i in xrange(len(a)):
        for j in xrange(len(b[0])):
           s = 0
           for k in xrange(len(b)):
               s+=a[i][k]*b[k][j]
           c[i][j] = s
    return c

def sign(x):
    if x>=0: return 1
    return -1

from copy import deepcopy

def apply(arr, func):
    res = deepcopy(arr)
    for i in xrange(len(arr)):
       for j in xrange(len(arr[0])):
          res[i][j] = func(res[i][j])
    return res

def normalize(figure):
    normalized = []
    for i in xrange(len(figure)):
       for j in xrange(len(figure[0])):
          normalized.append(figure[i][j])
    return normalized

def pretty_print(arr):
    for i in xrange(len(arr)):
        line = ''
        for j in xrange(len(arr[0])):
            if arr[i][j]==1: line+='*'
            else: line+='-'
        print line

from collections import deque

def denormalize(figure, w, h):
    matr = [[0 for i in xrange(w)] for j in xrange(h)]

    figure_ = deque(deepcopy(figure))
    for i in xrange(h):
        for j in xrange(w):
           matr[i][j] = figure_.popleft()
    return matr

