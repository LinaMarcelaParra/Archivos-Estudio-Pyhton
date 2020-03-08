while True:
    try:
        a	= input('Introduce	un	número:	')
        b	= 3
        print('{}/{} =	{}'.format(a,	b,	a/b))
    except TypeError :
            print("No se puede dividir una cadena de texto")
