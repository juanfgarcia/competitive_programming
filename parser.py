<<<<<<< HEAD
from data import Libreria
from data import Libro
import sys

f = sys.argv[1]
fd = open(f)

nlibros = 0
nlibreria = 0
dias = 0
libros = []
librerias = []

nums = fd.readline().split()
nlibros = nums[0]
nlibreria = nums[1]
dias = nums[2]

for i, j in enumerate(line.split()):

for line in fd:
    if linecounter==0:
        nums = line.split()
        nlibros = nums[0]
        nlibreria = nums[1]
        dias = nums[2]
    elif linecounter == 1:
        for i, j in enumerate(line.split()):
            libro = Libro(i ,j)
            libros.append(libro)

    else:


        
    

        




    linecounter+=1 


def getDias():
    return dias

def getLibros():
    return libros





=======
import sys

>>>>>>> bf507bc1b61bf81547278fac1720eecc9af8a376
