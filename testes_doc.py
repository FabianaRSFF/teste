def soma(x, y):
    """Soma x e y
    >>> soma(10, 20)
    31
    >>> soma(-10, 20)
    10
    """
    assert isinstance(x, (int, float)), 'x precisa ser int ou float.'
    assert isinstance(y, (int, float)), 'y precisa ser int ou float.'
    return x + y 

if __name__== '__main__':
    import doctest
    doctest.testmod()
    doctest.testmod(verbose=True)


# Não colocar o nome do arquivo igual ao nome do teste!!!!!
# Dá conflito e o Python entra em crise de identidade :)))))