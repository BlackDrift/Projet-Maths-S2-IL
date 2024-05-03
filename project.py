import matplotlib.pyplot as plt
import numpy as np
import math

plt.style.use('_mpl-gallery')

listePoints = [(2, 3, -0.2), (1.8, 5, -0.1), (4, 7, -0.2), (6, 7, 0.2), (4, 9, -1), (8, 9, -5/3), (7.8, 6.8, 5/6), (9, 5, 0.6), (5.8, 2.8, 1), (6, 2, -0.4)]

def hermiteInterpolation(point1, point2, nombrePoints):

    #On calcule la valeur du delta x entre les deux points (delta y n'étant pas utile ici, il n'a pas été instancié)
    deltaX = point2[0] - point1[0]

    #On instancie les listes pour stocker les points interpolés
    interpolatedXs = []
    interpolatedYs = []

    #Pour chaque valeur de t, on va faire une interpolation
    for i in range(nombrePoints):
        t = i / (nombrePoints - 1)  # Variation de t entre 0 et 1
        t2 = t * t
        t3 = t2 * t

        #On calcule les 4 coefficients de l'interpolation
        phi0 = 2 * t3 - 3 * t2 + 1 #2t^3 - 3t² + 1
        phi1 = t3 - 2 * t2 + t # t^3 - 2t² + t
        phi2 = -2 * t3 + 3 * t2 #-2t^3 + 3t²
        phi3 = t3 - t2 #t^3 - t²

        #On calcule la valeur du point interpolé
        interpolatedY = phi0 * point1[1] + phi1 * point1[2] + phi2 * point2[1] + phi3 * point2[2]

        #ainsi que son abscisse, pour pouvoir tracer correctement.
        interpolatedX = point1[0] + t * deltaX
        interpolatedXs.append(interpolatedX)

        #On ajoute le point interpolé à la liste de ces derniers
        interpolatedYs.append(interpolatedY)
    return interpolatedXs, interpolatedYs

# Test de la fonction

def display(listeDePoints=listePoints,nombrePoints=100):

    #on instancie une liste qui contiendra l'entièreté de toutes les abscisses obtenues de toutes les interpolations
    totalinterpolatedXs = []

    #pareil mais pour les ordonnées
    totalinterpolatedYs = [] 

    #on parcourt presque toute la liste, le dernier cas est à part
    for i in range(len(listeDePoints) - 1): 
        interpo = hermiteInterpolation(listeDePoints[i], listeDePoints[i + 1], nombrePoints) 
         #on ajoute au fur et à mesure les abscisses et ordonnées obtenues dans leurs listes respectives
        totalinterpolatedXs.append(interpo[0])
        totalinterpolatedYs.append(interpo[1])

    #le dernier cas : le dernier point de la liste et le premier
    interpo = hermiteInterpolation(listeDePoints[len(listeDePoints) - 1],listeDePoints[0], nombrePoints)
    totalinterpolatedXs.append(interpo[0])
    totalinterpolatedYs.append(interpo[1])

    #pour vérifier la cohérence des valeurs on les affichait dans la console
    #print(totalinterpolatedXs)
    #print(totalinterpolatedYs)
    
    #et on affiche la figure fraîchement obtenue
    plt.plot(totalinterpolatedXs,totalinterpolatedYs)
    plt.show()

def setFigure(n=10):

    #On met en place une liste vide qui contiendra les données des n points 
    listeSetPoints = []

    #Pour chacun des points :
    for i in range(n):
        while True:
            #On va vérifier que toutes les infos données sont correctes, donc on ESSAIE...
            try:
                #...De demander à l'utilisateur une valeur pour x
                setX = float(input("Veuillez entrer la valeur d'abscisse pour le {0}e(r) point : ".format(i + 1)))

                #On vérifie que c'est bien un nombre (Python peut traduire un entier en flottant)
                assert isinstance(setX, float)

                #On recommence avec une valeur pour y...
                setY = float(input("Veuillez entrer la valeur d'ordonnée pour le {0}e(r) point : ".format(i + 1)))

                assert isinstance(setY, float)

                #Et une valeur pour y'
                setYPrime = float(input("Veuillez entrer la valeur de la dérivée première pour le {0}e(r) point : ".format(i + 1)))

                assert isinstance(setYPrime, float)

                #Si tout s'est passé sans encombre, on sort du WHILE
                break
            #Sinon on gère les exceptions
            except ValueError:
                #Ici, une erreur de Valeur...
                print("Veuillez entrer un nombre valide.")

            except AssertionError as e:
                #Et ici une erreur d'Assertion (la valeur n'était pas un nombre)
                print(e)
        #Quand tout est bon, on peut sortir du While et reprendre la boucle for
        listeSetPoints.append((setX, setY,setYPrime))
        #Et on vérifie bien entendu que toutes les données ont été implantées correctement dans listeSetPoints
        #print(listeSetPoints)
        
    #Une fois tous les points entrés, on peut tout simplement afficher la figure (qui devrait ressembler à peu de choses près à ce dont l'utilisateur pensait)
    display(listeSetPoints)

# la masse est celle d'un SNA Type Rubis, de 2 670 tonnes en plongée
# la force moteur (de poussée) a été calculée comme une division de la puissance (en W) du moteur (de 0.5x10^7 ) par la vitesse de l'hélice, qui après calcul et recherches a été trouvée come égale à 20.94 m/s
def Nautilus(masse = 2670000, forceMoteur = 238777, distance = 1000, temps=150):
    #on sait que la somme des forces extérieures est égale au produit de la masse et de l'accéleration
    #mais également que ces forces extérieures peuvent se résumer à la poussée moteur elle-même
    #en partant du principe que les frottements dans l'eau sont négligeables et que le Poids et la Poussée d'archimède s'annulent
    accel = forceMoteur / masse
    print("L'accélération est de :" + str(accel) + " m/s².") #l'accélération avec les valeurs par défaut devrait être environ égale à 0.09 m/s² 
    #l'accéleration étant désormais calculée, on peut donc en déduire la vitesse, sachant que l'on part du principe que notre sous-marin parcourt 1000 m
    #le calcul de la vitesse comprend normalement la vitesse initiale sommée au produit de 2x l'accélération x la distance totale parcourue
    vitesse = math.sqrt(2 * accel * distance)
    print("La vitesse obtenue est de : " + str(vitesse) + " m/s.") #la vitesse devrait être environ égale à 13 m/s.
    #le Nautilus vient d'être mis à flots au bord du quai, qui est notre origine du repère.
    X = [0]
    Y = [0]
    for i in range(1, temps):
        X.append(i)
        Y.append(Y[i - 1] - vitesse * i - 0.5 * accel * i**2)
    plt.plot(X,Y)   
    plt.show() 


display()
setFigure()
Nautilus()

