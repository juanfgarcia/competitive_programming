class Libreria:
    def __init__(self, id, n, libros, sp, p, avg):
        self.id = id
        self.n = n          # Numero de libros que tiene 
        self.libros = libros # Array de objetos libro
        self.sp = sp         # Numero de días de procesado
        self.p = p           # Numero de libros que se pueden procesar a la vez
        self.avg = avg       # Media de los scores de los libros
      
    
    # Se calcula la productividad como el numero de libros que puede procesar dado
    # un dia de inicio 
    def productividad(self, dia, limite):
        n = min ( ( limite - (dia+self.sp) )*self.p, self.n)
        return (n*self.avg)

    # Devuelve los n mejores libros
    def getLibros(self, dia, limite):
        n = min ( ( limite - (dia+self.sp) )*self.p, self.n)
        return self.libros[:n]
 

class Libro:
    def __init__(self,id, score):
        self.id = id
        self.score = score

    def __str__(self):
        return "Id : " + str(self.id) + " Score: " + str(self.score) 


    def __lt__(self, other):
        return self.score<other.score        
    
    def __gt__(self, other):
        return self.score>other.score

    def __eq__(self, other):
        return self.id==other.id and self.score == other.score

    def __ne__(self, other):
        return self.id!=other.id and self.score != other.score
       