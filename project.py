import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('_mpl-gallery')

def droite():
    x = []
    y = []
    for k in range(15):
        y.append(k+1)
        x.append(k)
    plt.plot(x, y)

    plt.show()

def parabole():
    x = []
    y = []
    for k in range (-15, 16):
        y.append(k**2 + 1)
        x.append(k)
    plt.plot(x, y)

    plt.show()

    rotation(x, y)

def paraboleTournee():
    x = []
    y = []
    for k in range (-15, 16):
        x.append(k**2 + 1)
        y.append(k)

    
    plt.plot(x, y)

    plt.show()

   

def rotation(x, y):
    for k in range(-15, 16):
        if x[k]==0:
            vector = [0 - x[k], 0 - y[k]]

    for k in range(-15, 16):
        x[k] += vector[0]
        y[k] += vector[1]

    rot = [math.cos(math.pi/2),-math.sin(math.pi/2), math.sin(math.pi/2),math.cos(math.pi/2)]
    xP = []
    yP = []

    for k in range(-15, 16):
        xP.append(rot[0] * x[k] + rot[1] * y[k])
        yP.append(rot[2] * x[k]+ rot[3] * y[k])

    for k in range(-15, 16):    
        xP[k] -= vector[0]
        yP[k] -= vector[1]

    plt.plot(xP, yP)

    plt.show()

def lagrange(points, x):
    P = 0
    for i in range(len(points)):
        l = 1
        for j in range(len(points)):
            if i != j:
                l *= (x - points[j][0]) / (points[i][0] - points[j][0])
        P += l * points[i][1]
    return P

'''
float lagrange(float[] points, float x)
{
    float P = 0;
    for (int i = 0; i < points.Length; i++)
    {
        float l = 1;
        for (int j = 0; j < points.Length; j++)
        {
            if(i != j)
            {
                l *= (x - points[j][0]) / (points[i][0] - points[j][0])
            }
        }
        P += l * points[i][1]
    }
    return P;
}
'''
#droite()
#parabole()
#paraboleTournee()
x = np.linspace(-15, 16, 30)
plt.plot (x, lagrange([[0,1],[math.pi/2, 0],[math.pi, -1],[math.pi*2, 0]],x))
plt.show()