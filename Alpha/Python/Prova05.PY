def maior_numero (a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = 4
b = 2
c = 6

resultado = maior_numero(a,b,c)
print(resultado)