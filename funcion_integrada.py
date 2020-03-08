while True:
    try:
        a	= float(input('Introduce	un	número:	'))
        b	= 3
        print('{}/{} =	{}'.format(a,	b,	a/b))
        break			#	Si	todo	ha	ido	bien	se	interrumpe	el	bucle.
    except:
        print('Ha	ocurrido	un	error,	introduce	bien	el	número.')
