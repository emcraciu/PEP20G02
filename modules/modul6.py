""" Functia map(), functii lambda, functia filter()"""

###############################################################
# map() cu functie de mapare predefinita ca argument
# map() itereaza peste cel de al doilea argument si paseaza
# valuarea curenta functiei date ca prim argument
# Mapeaza fiecare numar din lista la un numar cu 1 mai mare
numbers = [1, 2, 3, 4]


def plus1(number: int):
    return number + 1


new_numbers = map(plus1, numbers)

# obiectul returnat de functia map este un obiect iterabil de tip 'map'
print(type(new_numbers))
print(dir(new_numbers))

for number in new_numbers:
    print(number)

###############################################################
# Creati o lista care sa contina mediile elevilor din dictionar

note = {'Alin': [7, 8, 9],
        'Catalin': [6, 9, 10],
        'Marius': [7, 8, 8]}


# Cand un dictinar este iterat sunt iterate cheile sale deci
# functia de mapare va primi pe rand fiecare cheie din dictionar
def calcul_medie(nume: str):
    note_student = note[nume]
    suma = 0
    for nota in note_student:
        suma += nota
    return nume, suma / len(note_student)


for medie in map(calcul_medie, note):
    print(medie)

###############################################################
# Functii lambda 'lambda *args:<code block>'
# Calculati media valorilor din tuple
note = [(7, 8), (9, 10), (6, 8), (-5, 5)]

medi = map(lambda arg: (arg[0] + arg[1]) / 2, note)

for medie in medi:
    print(medie)

###############################################################
# Recapitulare: Despachetarea unui tuple
a, *b, c = 1, 2, 3, 4

print(a)
print(b)
print(c)

###############################################################
# Functia filter() filtreaza obiectele dintr-un iterabil
# pe baza raspunsului unei functii. Daca obiectul returnat de
# functie este True-ish atunci obiectul este pastrat in obiectul
# returnat de tip filter
obj_filtrate = filter(lambda arg: (arg[0] + arg[1]) / 2, note)

print(type(obj_filtrate))
print(dir(obj_filtrate))

for obj in obj_filtrate:
    print(obj)

###############################################################
# Exercitiu:
animale = ['maimuta', 'leu', 'zebra', 'cangur', 'elefant']

# Din lista de mai sus creati o lista ce contine animalele
# in ordine inversa si nu contine animale ce incep cu 'c'
# Folsiti map, filter, lambda
# incercati sa scrieti to codul intr-o singura linie

# rezultatul este acelas cu:
result1 = [animal for animal in animale if not animal.startswith('c')][::-1]

# Rezolvare
result2 = [animal for animal in filter(lambda animal: not animal.startswith('c'), [animal for animal in map(lambda animal: animale[-animale.index(animal) - 1], animale)])]

print(result1 == result2)
