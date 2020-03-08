class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento,autor, genero):
        self.titulo	= titulo
        self.duracion	= duracion
        self.lanzamiento	= lanzamiento
        self.autor	= autor
        self.genero	= genero
        print('Se ha creado la película	{}'.format(self.titulo))

    def __str__(self):
        return '{}({})'.format(self.titulo, self.lanzamiento)
