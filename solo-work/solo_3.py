class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie_studenta = imie
        self.nazwisko = nazwisko
        self.numerindeksu = nr_indeksu
        self.indeks = []

    def __str__(self):
        return self.imie_studenta + ' ' + self.nazwisko + ' ' + str(self.numerindeksu)
    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)

    def oblicz_srednia(self):
        return sum(self.indeks)/len(self.indeks)


student_ania = Student("Anna", "Kosinska", 12345)
student_ania.dodaj_ocene(5.0)
student_ania.dodaj_ocene(4.0)
student_ania.dodaj_ocene(4.5)
student_ania.dodaj_ocene(4.5)
print(student_ania.indeks)
print(student_ania.nazwisko)
print(student_ania.oblicz_srednia())

#zadanie - 8 elementow i 2 def
class Mieszkanie:
    def __init__(self,nr_mieszkania, nr_bloku, ulica,  miasto, powierzchnia, ilosc_pokoi, pietro, cena):
        self.nr_mieszkania = nr_mieszkania
        self.nr_bloku = nr_bloku
        self.ulica = ulica
        self.miasto = miasto
        self.powierzchnia = powierzchnia
        self.ilosc_pokoi = ilosc_pokoi
        self.pietro = pietro
        self.cena = cena

    def __str__(self):
        return 'Zaprezentowane mieszkanie to mieszkanie nr ' + str(self.nr_bloku) + \
            ' w bloku nr ' + str(self.nr_bloku) + ' przy ulicy ' + self.ulica +  \
            ' w mieście ' + self.miasto + '. Mieszkanie znajduje się na piętrze ' + \
            str(self.pietro) + ', ma powierzchnię ' + str(self.powierzchnia) + ' metrów, a jego ilość pokoi to ' \
            + str(self.ilosc_pokoi) + '. Cena mieszkania to ' + str(self.cena)
    
    def czy_za_drogie(self):
        if self.cena/self.ilosc_pokoi > 250000:
            print("Cena mieszkania jest za wysoka w stosunku do ilości pokoi.")
        else:
             print("Cena mieszkania jest adekwatna do ilości pokoi.")
        
    def cena_metra_kwadratowego(self):
        return 'Cena metra kwadratowego wynosi ' + str(round(self.cena/self.powierzchnia))

mieszkanie_1 = Mieszkanie(12,1,'Niepodległości', 'Poznań', 60, 3, 2, 600000)

print(mieszkanie_1)
print(mieszkanie_1.czy_za_drogie())
print(mieszkanie_1.cena_metra_kwadratowego())