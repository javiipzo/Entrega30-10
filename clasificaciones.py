#Carga del modelo  
from joblib import load
modelo = load('modelos/kmean.joblib')

#CEREZA: 26,98 mm de diámetro,8,75 gramos  
#ALBARICOQUE: 55,7  mm de diámetro, 102,16 gramos  

cereza = [[26.98,8.75]]
numCluster = modelo.predict(cereza)
print("Número de clúster de las cerezas: "+ str(numCluster))

albaricoque = [[55.7,102.16]]
numCluster = modelo.predict(albaricoque)
print("Número de clúster de los albaricoques: " + str(numCluster)) 

if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza!") 

cereza = [[26.98,8.75]]
numCluster = modelo.predict(cereza)
if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza!")


albaricoque = [[55.7,102.16]]
numCluster = modelo.predict(albaricoque)
if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza!") 

