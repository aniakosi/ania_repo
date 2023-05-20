# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student

print("{} {}".format(hello, student))


# zadanie 1.2
studentname = input("Wpisz swoje imie")

print("Hello Ola")

print("Hello {}".format(studentname))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

# policz liczbe studentow w tablicy studenci 
# oczekiwany rezultat: Liczba studentow wynosi: 4
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: {}".format(liczba_studentow))

# zadanie 1.4
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek
print("Hello Ania")

for i in studenci: 
    print("Hello {}".format(i))

# zadanie 1.5

liczba = 3
potega = 4

wynik = liczba**potega

# oczekiwany rezultat:
# Wynik wynosi: 81
print("Wynik wynosi: {}".format(wynik))

# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))


# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()
# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda s: s.split()[1])
print("Alfabetyczna lista studentow wg nazwiska wynosi: ")
for student in studenci:
    print(student)