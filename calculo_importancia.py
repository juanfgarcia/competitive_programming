#librerias es una array de librerias
# una libreria tiene []libros, sp y p
# un libro tiene id y score

def calculoImportancia(librerias):
    
    sign_up = []
    for lib in librerias:
        result=0
        for book in lib.libros:
            result+=book.score
        sign_up.append(lib.sp)
        lib.importancia=result

    return sign_up, puntuacion

def procesarLibrerias(sign_up, puntuacion):
    
    