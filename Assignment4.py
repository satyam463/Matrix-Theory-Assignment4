
import numpy as np
import matplotlib.pyplot as plt

def parab_gen(y,a):
	x = y**2/a
	return x
simlen = 100
y = np.linspace(-1,1,simlen)
x = parab_gen(y,4)

#Parabola points
#Standard Parabola Vertex
O = np.array([0,0])

#Focus
F= np.array([1/4,0])

#Point on the directrix
D = -F

#Plotting the parabola
plt.plot(x,y,label='standard parabola')

#Plotting the directrix
plt.axvline(x= - 0.25 , label='Directrix',color='r')
#Labeling the coordinates
parab_coords = np.vstack((O,F, D)).T
plt.scatter(parab_coords[0,:], parab_coords[1,:])
vert_labels = ['O','F','D']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (parab_coords[0,i], parab_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()
