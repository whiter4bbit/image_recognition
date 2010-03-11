import Image

class ImageConvertor(object):
    def __init__(self,path):
       self.path = path
       self.img = Image.open(path)

    def get_array(self):
       w,h = self.img.size
       self.matr = [['-' for i in xrange(w)] for j in xrange(h)]
       for y in xrange(h):
          for x in xrange(w):
	     color = self.img.getpixel((x,y))
	     if color == (0,0,0,255):
	        self.matr[y][x]='*'
       return self.matr

import sys

def pretty_out(txt, f):
    for i in xrange(len(txt)):
        line = ''
    	for j in xrange(len(txt[0])):
	   line+=txt[i][j]
	f.write(line+'\n')

def output_numbers(dir, txt, order = [1,2,3,4,5,6,7,8,9,0], offset=0, width=7):
     ic = ImageConvertor(txt)
     array = ic.get_array()    
     with open(dir+'/all','w') as f:
     	pretty_out(array, f)
     cnt = 0
     for i in xrange(offset,len(order)*width, width):
        num = [a[i:i+width] for a in array]
	number = str(order[cnt])
	with open(dir+'/'+number, 'w') as f:
	   pretty_out(num, f)
	cnt+=1
	   
if __name__=="__main__":
     if len(sys.argv)==3:
     	img_path = sys.argv[1]
	out_path = sys.argv[2]
	ic = ImageConvertor(img_path)
	array = ic.get_array()
	with open(out_path, 'w') as f:
	   pretty_out(array, f)
	

    
