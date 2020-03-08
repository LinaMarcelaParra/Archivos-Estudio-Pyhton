from Catalogo import*
from Peliculas import*

c=catalogo()

c.agregar(Pelicula('Indomable',	100,	2011,'Steven Soderbergh','accion'))
c.agregar(Pelicula('Hanna',	80,	2011,'Joe Wright','accion'))
c.agregar(Pelicula('Historia de un Matrimonio',	80,	2019,'Noah Baumbach','drama'))
c.agregar(Pelicula('Ella',	70,	2013,'Spike Jonze','drama'))
c.agregar(Pelicula('El irlandes',	175,	2019,'Martin Scorsese','drama'))
c.agregar(Pelicula('El	Conjuro',	70,	2013,'James Wan','miedo'))
c.agregar(Pelicula('La monja',	80,	2018,'Corin Hardy','miedo'))
c.agregar(Pelicula('El	exorcista',	80,	1973,'William Friedkin','miedo'))
c.agregar(Pelicula('Dolittle',	90,	2020,'Stephen Gaghan','Comedia'))
c.agregar(Pelicula('The Hangover',	80,	2009,'Todd Phillips','Comedia'))
c.agregar(Pelicula('La Mascara',	90,	1994,'Chuck Russell','Comedia'))
c.agregar(Pelicula('The Great Hack',	60,	2019,'Karim Amer','Documental'))
c.agregar(Pelicula('Leaving Neverland',	80, 2019,'Dan Reed','Documental'))
c.agregar(Pelicula('Amy',	70,	2019,'Asif Kapadia','Documental'))
c.agregar(Pelicula('Origen',	65,	2015,'Christopher Nolan', 'accion'))


print('\n MENU	\n======\n')

while True:
        print('Selecciona una opción:\n')
        print('1: Mostrar todo el catalogo de Peliculas')
        print('2: Mostrar pelicula por genero')
        print('3: Añadir Pelicula Nueva')
        print('4: Eliminar Pelicula')
        print('5: Salir\n')

        user_choice	= input()
        if user_choice	== '1':
            print('\n Lista de Peliculas Disponibles\n-----\n')
            c.mostrar()
        elif user_choice == '2':
            print('Cual es tu genero favorito?, selecciona por genero')
            Genero_choice=input()
            c.mostrar_genero(Genero_choice)

        elif user_choice	== '3':
            titulo=input('Introduzca un titulo: ')
            duracion=input('Introduzca una duración en minutos: ')
            lanzamiento=input('Introduzca el año del lanzamiento: ')
            autor=input('Introduzca el nombre del director de la pelicula: ')
            genero=input('Introduzca genero de la pelicula: ')
            c.agregar(Pelicula(titulo,duracion,lanzamiento,autor, genero))

        elif user_choice	== '4':
                c.eliminar()
        elif user_choice	== '5':
                print('Saliendo	del	programa!...Hasta Luego')
                break
        else:
                print('Opción no valida, vuelve a intentarlo.\n')
