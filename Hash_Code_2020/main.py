from data import Libreria
from data import Libro
from copy import deepcopy as dc
import sys


def parse(inf):
    fd = open(inf)

    # B: numero de libros
    # L: numero de librerias
    # D : numero de dias

    B, L, D = list(map(int, fd.readline().strip().split()))
    
    libros = []
    for i,j in enumerate(fd.readline().strip().split()):
        libro = Libro(i,int(j))
        libros.append(libro)
    
    librerias = []
    for i in range(L):
        # n: numero de libros
        # sp: numero de dias de signup
        # p: numero de libros que puede escanear al dia

        n, sp, p = list(map(int, fd.readline().strip().split()))

        libros_i = []
        
        for j in fd.readline().split():
            libros_i.append(libros[int(j)])

        libros_i.sort()

        avg = sum([x.score for x in libros_i])/n
        libreria = Libreria(i, n, libros_i, sp, p, avg)
        librerias.append(libreria)    

    return  B, L, D, libros, librerias

def solve(librerias, D):
    pipeline = {}
    librerias_restantes = dc(librerias)
    fin = False
    dia = 0

    while not fin:
        if len(librerias_restantes)==0:
            fin = True
            break
        # Buscamos la libreria con mayor productividad para el dia actual
        flag = 0
        max_prod = 0
        max_id = 0 
        for lib in librerias_restantes:
           
            prod_i = lib.productividad(dia, D)
            if prod_i > 0:
                flag = 1
            
            if prod_i > max_prod:
                max_prod = prod_i
                max_id = lib.id
        
        if flag==0:
            fin = True

        else:
            pipeline[max_id] = librerias[max_id].getLibros(dia, D)
            dia = dia+librerias[max_id].sp       
            for lib in librerias_restantes:
                if lib.id == max_id:
                    librerias_restantes.remove(lib)

    print(pipeline)
    return pipeline 




def main():
    data = {'in/a_example.txt' : 'out/a_example.out',
            'in/b_read_on.txt' : 'out/b_read_on.out',
            'in/c_incunabula.txt' : 'out/c_incunabula.out',
            'in/d_tough_choices.txt': 'out/d_tough_choices.out' ,
            'in/e_so_many_books.txt' :  'out/e_so_many_books.out',
            'in/f_libraries_of_the_world.txt' : 'out/f_libraries_of_the_world.out'}        

    
    for d in data:
        print(d)
        B, L, D, _, librerias = parse(d)
        print(B, L, D)
        '''
        pipeline = solve(librerias, D)

        out = open(data[d], 'w+')
        out.write(str(len(pipeline)) + '\n')
        
        for lib in pipeline:
            out.write( str(lib)+ ' ' + str(len(pipeline[lib])) + '\n')
            for l in pipeline[lib]:
                out.write(str(l.id) + ' ')
            out.write('\n')

        out.close()
        '''


if __name__ == '__main__':
    main()











