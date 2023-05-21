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



student_ania = Student("Anna", "Kosinska", 12345)
student_ania.dodaj_ocene(5.0)
print(student_ania.indeks)
print(student_ania.nazwisko)
print(student_ania)