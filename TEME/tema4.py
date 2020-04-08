"""
Tema4 - 40% din nota finala
Creati o functie care poate lua ca argument un obiect iterabil ce poate contine alte obiecte iterabile sau
ne iterabile. Se va itera peste toate obiectele iterabile de la orice nivel si se va crea o lista cu toate obiectele
ce nu pot si iterte sau in cazul string-urilor daca lungimea lor este 1
Nu uitati ca puteti folosi recursivitate

ex:
funtia primeste: [(1, 5), 'abc', {'x': 'y'}, [[[3]]], set()]
funtia returneaza [1, 5, 'a', 'b', 'c', 'x', 'y', 3]

"""
input = [(1, 5), 'abc', {'x': 'y'}, [[[3]]], set()]
output = [1, 5, 'a', 'b', 'c', 'x', 'y', 3]

def flatten(data):
    result = []
    if not hasattr(data, '__iter__'):
        result.append(data)

    elif isinstance(data, dict):
        for key, value in data.items():
            pass  # hint: add code here
    # hint: add additional conditions here
    return result


assert flatten(input) == output
