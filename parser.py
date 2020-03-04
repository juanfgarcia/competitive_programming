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
nlibros = int(nums[0])
nlibrerias = int(nums[1])
dias = int(nums[2])

for i, j in enumerate(fd.readline().split()):
    libro = Libro(i ,j)
    libros.append(libro)

for i in range(nlibrerias):
    libreria = fd.readline().split()
    sp = libreria[1]
    p = libreria[2]
    libros_i = []
    for j in fd.readline().split():
        libros_i.append(libros[int(j)])
    
    libreria = Libreria(libros_i, sp, p)
    librerias.append(libreria)



def getDias():
    return dias

def getLibros():
    return libros

def getLibrerias():
    return librerias








