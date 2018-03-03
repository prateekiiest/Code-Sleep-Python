#importing the required libraries
import matplotlib.pyplot as plt
from math import sin, cos, pi

def sgn(x):
	return ((x>0)-(x<0))*1

#parameter for marking the shape
a,b,n=200,200,0.5
na=2/n
# defining the accuracy
step=100
piece=(pi*2)/step
xp=[]
yp=[]
t=0
for t1 in range(step+1):
	# because sin^n(x) is mathematically the same as (sin(x))^n...
	x=(abs((cos(t)))**na)*a*sgn(cos(t))
	y=(abs((sin(t)))**na)*b*sgn(sin(t))
	xp.append(x);yp.append(y)
	t+=piece

plt.plot(xp,yp) # plotting all point from array xp, yp
plt.title("Superellipse with parameter "+str(n))
plt.show()
