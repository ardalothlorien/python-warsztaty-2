import turtle


with open('zolw.txt') as plik:  # wczytujemy plik
    for linia in plik:  # iterujemy po liniach
        linia = linia.strip()  # usuwamy biale znaki z poczatku i konca
        podzielone = linia.split()  # dzielimy po spacjach
        komenda = podzielone[0]  # pierwszy element podzielonego
        liczba = podzielone[1]  # drugi element podzielonego
        liczba = int(liczba)  # zmieniamy typ na liczbe
        print(komenda, liczba)
        if komenda == 'F':
            turtle.forward(liczba)
        elif komenda == 'L':
            turtle.left(liczba)
        elif komenda == 'R':
            turtle.right(liczba)
        elif komenda == 'B':
            turtle.backward(liczba)
        else:
            print("Nie znana komenda!", komenda)


turtle.mainloop()
