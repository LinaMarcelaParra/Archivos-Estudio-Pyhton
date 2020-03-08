from Peliculas import *

class catalogo:
        Peliculas	= []
        def __init__(self,	peliculas=[]):
            self.peliculas	= peliculas

        def agregar(self, p):
            self.peliculas.append(p)


        def eliminar(self):
            while True:
                try:
                    numero=int(input('introduzca el numero de la pelicula que quieres borrar: '))
                    numero=numero-1
                    if  0 <= numero < len(self.peliculas):
                        p=self.peliculas[numero]
                        print("\tBorrando la pelicula ",numero+1,".",p.titulo,"(",p.lanzamiento,",",p.autor,"-",p.genero,")")
                        del self.peliculas[numero]
                        return
                    else:
                        print("Dato no encontrado")
                        break

                except ValueError:
                    print('El valor debe ser un numero')
                    return

        def mostrar(self):
            for i in range(len(self.peliculas)):
                p=self.peliculas[i]
                print("\t",i+1,".",p.titulo,"(",p.lanzamiento,",",p.autor,"-",p.genero,")")

        def mostrar_genero(self,h):
            print("Peliculas por genero: ",h)
            encontrado=False
            for i in range(len(self.peliculas)):
                p=self.peliculas[i]
                if p.genero.lower() == h.lower():
                    print("\t",i+1,".",p.titulo,"(",p.lanzamiento,",",p.autor,"-",p.genero,")")
                    encontrado=True
            if not encontrado:
                print("Hey no tenemos peliculas del genero:",h," lo siento :( ")
