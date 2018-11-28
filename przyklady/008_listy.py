lista = [1, 2, 3, 4]
lista2 = ["string1", "string2"]
lista3 = [1, 3, "string"]

print(lista)

print(lista[0])  # pierwszy element z listy to jest zawsze 0!

lista2[0] = "inny string"
print(lista2)
# lista2[2] = "trzeci element"  BLAD, nie mozna tak dodawac do listy
lista2.append("dopisane do listy")
print(lista2)

