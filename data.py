class Libreria:
    def __init__(self, libros, sp, p):
        self.libros = libros
        self.sp = sp
        self.p = p

class Libro:
    def __init__(self,id, score):
        self.id = id
        self.score = score

    def __str__(self):
        return "Id : " + str(self.id) + " Score: " + str(self.score) 


