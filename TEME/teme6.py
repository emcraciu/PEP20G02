# Tema6 - 30% din nota finala
# Creati o clasa care se intantiaza cu o lista de cai de fisiere
# Clasa va avea o metoda create_ordered_log ce va sorta fiecare linie din fisiere pe baza primului cuvant
# Primul cuvant reprezinta data scrisa in formatul UNIX si este un numar
# Fisierele se gasesc in repo.

import os


class LogSorter():
    def __init__(self, files: list):
        self.files = []
        for file in files:
            path = os.path.join(os.path.dirname(__file__), file)
            self.files.append(path)

    def create_ordered_log(self, output_file: str):
        pass


log_sorter = LogSorter(['log1', 'log2'])
log_sorter.create_ordered_log('sorted.log')

