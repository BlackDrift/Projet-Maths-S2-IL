import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('_mpl-gallery')

listePoints = [(2, 3, -0.2), (2, 7, 1), (4, 7, -0.2), (6, 7, 0.2), (4, 9, -1), (8, 9, -5/3), (8, 7, 1), (9, 5, 0.6), (6, 3, 5/3), (6, 2, -0.4)]
allXPoints = []
allYPoints = []
def interpolationHermite(point1:tuple,point2:tuple, nombrePoints:int)->None:
    X = []
    Y = []
    X.append(point1[0])
    Y.append(point1[1])
    H = 0
    d = int(math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2))
    print(d)
    if point1[0] != point2[0]:
        for x in range(1, nombrePoints + 1):
            t = ((x / 100) - point1[0])/(point2[0] - point1[0])
            f1 = ((t - 1) ** 2) * (2 * t + 1)
            f2 = t ** 2 * (-2 * t + 3)
            f3 = t * ((t - 1) ** 2)
            f4 = (t ** 2) * (t - 1)
            H = point1[1] * f1 + point2[1] * f2 + point1[2] * f3 + point2[2] * f4
            X.append(point1[0] - (x / nombrePoints))
            Y.append(H)
    else :
        for x in range(1, nombrePoints + 1):
            a0 = point1[1]
            a1 = point1[2]
            a2 = point1[2]
            a3 = 0
            H = a0 + a1 * ((x / 100) - point1[0]) + a2 * ((x / 100) - point1[0]) ** 2 + a3 * ((x / 100) - point1[0]) ** 3
            X.append(point1[0] - (x / nombrePoints))
            Y.append(H)
    print(X) 
    print(Y)
    allXPoints.append(X)
    allYPoints.append(Y)

def afficheForme(listeAbscisses=allXPoints, listeOrdonnees=allYPoints):
    for x in range(len(listeAbscisses)):
        plt.plot(listeAbscisses[x],listeOrdonnees[x])
    plt.show()

# def penteTangente():
#     pT = []
    
#     for i in range(len(listePoints)):
#         pT.append(())

interpolationHermite(listePoints[1],listePoints[2], 100)
interpolationHermite(listePoints[2],listePoints[3], 100)
#afficheForme()
print('\n')
interpolationHermite(listePoints[0],listePoints[1], 100)

# la masse est celle d'un SNA Type Rubis, de 2 670 tonnes en plongée
# la force moteur (de poussée) a été calculée comme une division de la puissance (en W) du moteur (de 0.5x10^7 ) par la vitesse de l'hélice, qui après calcul et recherches a été trouvée come égale à 20.94 m/s
def Nautilus(masse = 2670000, forceMoteur = 238777, distance = 1000, temps=150):
    #on sait que la somme des forces extérieures est égale au produit de la masse et de l'accéleration
    #mais également que ces forces extérieures peuvent se résumer à la poussée moteur elle-même
    #en partant du principe que les frottements dans l'eau sont négligeables et que le Poids et la Poussée d'archimède s'annulent
    accel = forceMoteur / masse
    print("L'accélération est de :" + str(accel) + "m/s².") #l'accélération avec les valeurs par défaut devrait être environ égale à 0.09 m/s² 
    #l'accéleration étant désormais calculée, on peut donc en déduire la vitesse, sachant que l'on part du principe que notre sous-marin parcourt 1000 m
    #le calcul de la vitesse comprend normalement la vitesse initiale sommée au produit de 2x l'accélération x la distance totale parcourue
    vitesse = math.sqrt(2 * accel * distance)
    print("La vitesse obtenue est de : " + str(vitesse) + "m/s.") #la vitesse devrait être environ égale à 13 m/s.
    #le Nautilus vient d'être mis à flots au bord du quai, qui est notre origine du repère.
    X = [0]
    Y = [0]
    for i in range(1, temps):
        X.append(i)
        Y.append(Y[i - 1] - vitesse * i - 0.5 * accel * i**2)
    plt.plot(X,Y)   
    plt.show() 

Nautilus()

'''
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

#droite()
#parabole()
#paraboleTournee()
x = np.linspace(-15, 16, 30)
plt.plot (x, lagrange([[0,1],[math.pi/2, 0],[math.pi, -1],[math.pi*2, 0]],x))
plt.show()
'''