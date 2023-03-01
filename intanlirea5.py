from itertools import count
from helper import suma
# Obiective Intalnire 5 FUNCTII
'''
-Sa invatam sa lucram cu functii
    -Functii simple
   - Functii cu parametri
    -Functii cu return
   - Functii cu parametri si return
'''

'''Ce este o functie?
O zona de cod cu o mica logica proprie, care poate fi folosita/refolosita (apelata) de oricate ori avem nevoie. 
Asta e si utilitatea ei principala, ajuta sa eliminam copy paste
Write once, use n times 
'''


# def print_hi():
#     print('Hello!')
#
#
# print_hi()  # Apelata cu succes

'''Ce este un parametru?
Datele de intrare (input) intr-o functie.
Uneori functia are nevoie de niste date ca sa poata functiona.
De ex, daca ar fi sa continuam functia print_hi si sa o customizam pentru diferiti
utilizatori vom avea nevoie de un parametru unde sa pastram utilizatorii diferiti
O functie poate sa aiba oricati parametri.
Parametrii sunt optionali.
Daca avem mai multi, se despart cu ","
Practic sunt niste variabile declarate dar neinitializate.
Ele vor fi initializate (adica vor primi valori), la apelarea functiei.
'''

#
# def print_hi_cu_parametru(nume):  # nume reprezinta un parametru
#     print(f'Hello! {nume}')
#
#
# print_hi_cu_parametru('Matei')  # nume reprezinta un argument
#
#
# def print_hi_cu_parametri(nume, prenume):  # cu mai multi parametri
#     print(f'Hello! {nume} {prenume}')
#
#
# print_hi_cu_parametri('Matei', 'Olten')  # parametrii nu sunt obligatorii
#
#
# def print_hi_cu_parametri(nume='___', prenume='___'):
#     print(f'Hello! {nume} {prenume}')
#
#
# print_hi_cu_parametri('Andrei','Sofocle')
# print_hi_cu_parametri()

#  Daca definim parametrii in definitia functiei si nu ii specificam
# in momentul in care apelam functia ca argument, va da eroare.
# Daca declaram valori default la parametri, atunci apelarea functiei fara
# argument nu va da eroare si va afisa valorile default

# def print_hi_cu_parametri():  # Fara parametri in definitie
#     nume = input('Introduceti numele:\n')
#     prenume = input('Introduceti prenumele:\n')
#     print(f'Hello! {nume} {prenume}')
#
#
# print_hi_cu_parametri()


'''Ce este un return?
Se foloseste cand functia ne si expune un raspuns (output).
Acest raspuns se poate salva in variabile.
Return e optional.
Se poate returna orice tip de date cunoscut.
In general, return e ultimul lucru in functie, 
deoarece aici se iese din functie. 
It’s like a lovechild between break + pop :)) 
(iese din functie dar ne ofera si un raspuns)
In general avem un singur return.
Exceptie cand folosim if else, 
atunci putem avea mai multe, 
dar oricum la rulare se va ajunge doar  
intr-un singur caz
'''
# def print_hi_cu_parametri():  # Fara parametri in definitie
#     nume = input('Introduceti numele:\n')
#     prenume = input('Introduceti prenumele:\n')
#     nume_complet = nume + ' ' + prenume
#     return nume_complet


# exemplu = print_hi_cu_parametri()  # cand pui rezultatul intr-o variabila si apoi printezi variabila
# print(exemplu)

# print(print_hi_cu_parametri())  # varianta directa de printat

#
'''Cum apelam functii din alte fisiere
-Se face un nou helper.py in proiect
-in acest nou file se definesc functiile pe care le voi refolosi
-Apoi, in prima linie din fisierul de lucru import functiile din helper.py
- Sunt trei lucruri importante la import
1. Import math  #  syntaxa pentru un modul definit in Python
2. Import suma (pe care nu stie de unde sa o ia)
- from helper import suma = syntaxa pentru tot ce am definit eu in fisierul helper.py
- from helper import * = syntaxa pentru importul tuturor functiilor folosibile din helper.py
- from helper import Matei
'''
# # Asa apar in helper.py
# class Matei():
#     def Matei(self):  # asa initializez clasa, ca in Java

# exemplu2 = suma(2, 3)
# print(exemplu2)