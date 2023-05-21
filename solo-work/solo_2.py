#trójkąt
def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = (bok_a * h_a)/2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod


print(f"Pole i obod trojkat wynosza: {trojkat(10,15,12, 8)}")

#koło
def kolo(promien):
    pole = 3.14*promien**2
    obwod = 2*3.14*promien
    return pole, obwod

print(f"Pole i obod kola wynosza: {kolo(4)}")

#romb
def romb(bok, h):
    pole = bok * h
    obwod = 4 * bok
    return pole, obwod

print(f"Pole i obod rombu wynosza: {romb(4, 3)}")