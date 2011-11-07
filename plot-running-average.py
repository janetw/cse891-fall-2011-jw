#import random
import math
from matplotlib import pyplot
from pylab import*
import random

print random

def roll():
    avgs = []
    x = []
    y = []
    for i in range(150):
        y.append(random.randint(1, 1000))
        x.append(i)
        avgs.append( sum(y) / float(len(y)))
    return x, avgs

x,y = roll()
pyplot.plot( x, y )


x, y = roll()
pyplot.plot( x, y, 'r--' )

x, y = roll()
pyplot.plot( x, y, 'b+' )
 

min_x, max_x = 0, 40
min_y, max_y = 0, 1000
pyplot.axis([min_x, max_x, min_y, max_y])
 

pyplot.clf()

def roll2():
    x = []
    for i in range(150):
        x.append(random.randint(1, 1000))
    return sum(x) / 150.0

avgs = []
for i in range(100):
    avgs.append(roll2())

pyplot.hist(avgs, 50)
show()

