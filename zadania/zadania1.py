slownik = {}

with open('oceny.txt') as oceny:
    for linia in oceny:
        linia = linia.strip()
        podzielone = linia.split()
        nazwisko = podzielone[0]
        ocena = podzielone[1]
        ocena = int(ocena)  # zmiana typu zmiennej ocena ze stringa na liczbe
        slownik[nazwisko] = ocena


najwysza_ocena = 0
najwysza_ocena_nazwisko = None
najnizsza_ocena = 10
najnizsza_ocena_nazwisko = None

suma = 0

for nazwisko in slownik:
    ocena = slownik[nazwisko]
    if ocena > najwysza_ocena:
        najwysza_ocena = ocena
        najwysza_ocena_nazwisko = nazwisko
    if ocena < najnizsza_ocena:
        najnizsza_ocena = ocena
        najnizsza_ocena_nazwisko = nazwisko
    suma += ocena   # to jest dokladnie to samo co: suma = suma + ocena

print("Najwyzsza ocena to:", najwysza_ocena, "uzyskana przez", najwysza_ocena_nazwisko)
print("Najnizsza ocena to:", najnizsza_ocena, "uzyskana przez", najnizsza_ocena_nazwisko)
print("Średnia:", suma/len(slownik))

