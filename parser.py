"""
loads figure from text file
"""
def parse(path, up):
   lines = []
   with open(path, 'r') as f:
       lines = f.readlines()
   lines = [line.strip() for line in lines]
   matr = [[-1 for i in xrange(len(lines[0]))] for j in xrange(len(lines))]
   for i in xrange(len(lines)):
      for j in xrange(len(lines[0])):
      	 if lines[i][j]==up:
	    matr[i][j] = 1
   return matr
   
  
