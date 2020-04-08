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


# ###############################################################
# # Folosirea fisierelor in python

# path absolut /dir1/dir2/fisier.py
# relativ dir2/fisier.py

logfile = 'testfile.log'
data = open(logfile, 'rb')
print(type(data))
print(dir(data))
text = data.read()

text0 = 'alfabet'
# opening file with w+ should not delete existing content (will investigate)
data1 = open('testfile2.log', 'w+t')
text1 = data1.read()
new_text = text0 + text1
data1.write(new_text)
data1.close()

text2 = '\n Add this text'
data2 = open('testfile2.log', 'a')
data2.write(text2)
data2.close()

###############################################################
# obiecte the tip bytearray
# encoding este folosit pentru a determina se bytes corespund la un anumit caracter
# acelas caracter poate avea assignat alt set de bytes pentru un encoding differit

set_de_bytes = '\x03\x00\x00\x33'
byte_array = bytearray(set_de_bytes, encoding='UTF-8')

print(type(byte_array))
print(dir(byte_array))

###############################################################
# Statement-ul with
# metoda __exit__ de pe obiectele de tip stream executa stream.close()

logfile = 'testfile.log'
with open(logfile, 'r') as fisier:
    text = fisier.read()


class TestObject():

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Stop with')

    def print_something(self):
        print('something')


with TestObject() as obj:
    obj.print_something()
    #raise AttributeError('Testing exit')

print('End of Script')

###############################################################
# Explicatii si cauze pentru diverse tipuri de errori

try:
    fisier = open('testfile.log', 'a')
    fisier.write('100')
    fisier = open('somefile.txt', 'r')
except FileNotFoundError:
    pass
except TypeError:
    pass
except PermissionError:
    pass


###############################################################
# Exemplu minimalaist de functie decorator

def decorate_with(func):  # functia decorata este argumentul primit de functia decorator
    def wrapper(*args):  # argumentele functiei decorate ajung ca argumente pentru wrapper
        print('Inainte de functie')
        func(*args)
        print('Dupa functie')

    return wrapper


@decorate_with
def function_to_be_decorate(message):
    print(message)


function_to_be_decorate('Functie decorata')
