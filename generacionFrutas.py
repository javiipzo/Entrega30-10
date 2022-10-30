#---- IMPORTAR MÓDULOS --  
import random
import pandas as pnd

#---- CARACTERÍSTICAS------  

#CEREZAS 
caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]

#ALBARICOQUES  
caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]] 

cantidadObservaciones = 2000 
#Generamos 2000 cerezas y 2000 albaricoques.
#Generación de las cerezas  
cerezas = []
random.seed()
for iteration in range(cantidadObservaciones):
    #elección al azar de una característica  
    cereza = random.choice(caracteristicasCerezas)
    #Generación de un diámetro  
    diametro = round(random.uniform(cereza[0], cereza[1]),2)
    #Generación de un peso  
    peso = round(random.uniform(cereza[2], cereza[3]),2)
    print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
    cerezas.append([diametro,peso])

#Generación de los albaricoques  
albaricoques = []
random.seed()
for iteration in range(cantidadObservaciones):
    #elección al azar de una característica  
    albaricoque = random.choice(caracteristicasAlbaricoques)
    #Generación de un diámetro  
    diametro = round(random.uniform(albaricoque[0], albaricoque[1]),2)
    #Generación de un peso  
    limiteMinPeso = albaricoque[2] / 1.10
    limiteMaxPeso = albaricoque[2] * 1.10
    peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
    print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
    albaricoques.append([diametro,peso]) 

#Constitución de las observaciones  
frutas = cerezas+albaricoques
print(frutas)

#Mezcla de las observaciones  
random.shuffle(frutas)

dataFrame = pnd.DataFrame(frutas)
dataFrame.to_csv("datas/frutas.csv", index=False,header=False)