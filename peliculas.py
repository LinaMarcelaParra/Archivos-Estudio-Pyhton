class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo	= titulo
        self.duracion	= duracion
        self.lanzamiento	= lanzamiento
        print('Se	ha	creado	la	película	{}'.	format(self.titulo))

p	= Pelicula('El	padrino',	175,	1972)
