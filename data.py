class Libreria:
    def __init__(self, libros, sp, p):
        self.libros = libros
        self.sp = sp
        self.p = p
        self.importancia = 0
        
    #para poder ordenar llista de librerias por importancia
    def __lt__(self, other):
        return self.importancia<other.importancia        
    
    def __gt__(self, other):
        return self.importancia>other.importancia

    def __eq__(self, other):
        return self.importancia==other.importancia and self.p == other.p and self.libros==other.libros and self.sp==other.sp

    def __ne__(self, other):
        return self.importancia!=other.importancia and self.p != other.p and self.libros!=other.libros and self.sp!=other.sp

class Libro:
    def __init__(self,id, score):
        self.id = id
        self.score = score

    def __str__(self):
        return "Id : " + str(self.id) + " Score: " + str(self.score) 


