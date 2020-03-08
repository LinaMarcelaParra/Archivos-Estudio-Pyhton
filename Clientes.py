clientes	= [
{'nombre':	'Richard',	'apellidos':	'Stallman',	'dni':	'01234567A'},
{'nombre':	'Aaron',	'apellidos':	'Swartz',	'dni':	'98765432Z'}
]
print(clientes)


def mostrar_cliente(clientes,	dni):
    for c	in clientes:
        if dni	== c['dni']:
            print('{} {}'.format(c['nombre'],	c['apellidos']))
            return
        print('Clente	no	encontrado.')

mostrar_cliente(clientes,	'01234567A')
