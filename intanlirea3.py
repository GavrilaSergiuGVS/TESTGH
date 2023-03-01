# STRUCTURI DE DATE
# LISTA  # accepta duplicate
'''
● Listele păstrează mai multe valori într-o singura variabilă.
● În Python, putem păstra diferite tipuri de date în aceeași listă.
● Fiecare element din listă are index începând de la 0 (ca și string-ul).
● Lista este ordonată, astfel când adăugăm un element nou, acesta se va pune la final.
● Lista este mutabilă, adică putem adăuga, șterge sau schimba elemente din ea.
● În listă putem pune valori duplicate.
● len() ne va da dimensiunea listei - Câte elemente avem în listă?
'''

# list1 = ['abc', 30, True, 'male1', 'male2']
# print(list1)
# print(list1[0])
# print(len(list1))
# print(list1[-1])
# print(list1[4])

# # Suprascriere
# list1 = ['abc', 30, 'portocala', 'male1', 'male2']
# list1[1] = 'albastru'  # schimbam un item; se incepe de la index 0
# print(list1)
# list1[1:3] = ['test1', 'lamaie']
# print(list1)
# list1[1:3] = [41,'lamaie'] # schimb range de itemi; va inlocui pana la 3, adica 1 si 2
# print(list1)
# #
# list2 = ['mar', 'banana','par']
# print(list2)
# list2[1:2] = ['coacaze', 'pepene'] # pot sa inlocuiesc un element cu doua elemente
# print(list2)

# #  Adaugare  - adauga doar un element la finalul liste
#
# list3 = ['test1', 'test2', 'test3']
# print(list3)
# list3.append('orange')
# print(list3)

# #  Insert - adauga la un anumit index
# list3.insert(0,'cameleon')
# print(list3)

# # Scoatere elemente
# list3.remove('test1')  # scoate elementul dorit, adica 'test1'
# print(list3)
# list3.pop(1)  # scoate elementul cu indexul 1
# print(list3)
# list3.pop()  # scoate ultimul element din lista, cand nu se pune indexul in paranteza
# print(list3)
# del list3[1] # sterge elementul de la indexul specificat
# print(list3)
# del list3  # sterge complet lista
# print(list3)  # NameError: name 'list3' is not defined. Did you mean: 'list'?
# list3.clear()  # goleste lista, ramane fara continut
# print(list3)

#  Sortare
# thislist = ['orange', 'mango', 'kiwi', 'pineapple', 'banana']
# print(thislist)
# thislist.sort()
# print(thislist)  # printeaza in ordine alfabetica
# thislist.sort(reverse=True)
# print(thislist)
#
# thislist = [100, 'krer', 50, 65, 82, 23, True, 'wre']
# thislist.sort()
# print(thislist)  # TypeError: '<' not supported between instances of 'str' and 'int'

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()  # vor fi sortate crescator
# print(thislist)
# thislist.sort(reverse=True)  # sorteaza descrescator
# print(thislist)

# Copierea unei liste
# thislist = ['apple', 'banana', 'cherry']
# mylist = thislist.copy()
# print(mylist)
# mylist = thislist[:2].copy()  # copiaza lista de la inceput pana la indexul specificat
# print(mylist)

# exista si metoda lista de lista
# thislist = ['apple', 'banana', 'cherry']
# mylist = list(thislist)
# print(mylist)

# # concatenare de liste
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# sau
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
# print(list1)
#
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3, 4]
# list1.extend(list2[:4])  # extind list1 cu list2
# list2.extend(list1)  # practic list1 este suprascrisa si la asta se adauda list2
# print(list1)
# print(list2)

# link exemple:  w3schools.com/python/python_lists.asp

'''
Dictionarul - Dict
● Dicționarele păstrează date de tip cheie: valoare.
● Dict-urile sunt ordonate.
● Dict-urile sunt mutabile, deci valorile pot fi schimbate.
● Cheile sunt unice, nu putem avea chei duplicate, ar crea confuzie.
● Cheile sunt ca niște porecle pentru index-uri.
● Putem folosi len() pentru a afla dimensiunea.(cheie-valoare)
'''

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# print(thisdict)
# print(len(thisdict))
# print(thisdict['brand'])  # ca sa printez valoarea de la o anumita cheie
#
# # # Accesare item:
# x = thisdict.get('model') # cu metoda get + cheie
# print(x)
# y = thisdict.keys()  # vrem sa aflam care sunt toate cheile dictionarului
# print(y)

# schimbare valoare

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# thisdict['year'] = 2018 # schimbam anul din 1964 in 2018
# print(thisdict)
#
# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# thisdict.update({'anul': 2020})  # adauga o noua cheie/ valoare->>> anul: 2020
# print(thisdict)

# Adaugare itemi in dictionar
# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# thisdict['color'] = 'red'  # adauga o cheie/valoare la sfarsitul dictionarului
# print(thisdict)

# Scoatere elemente
# thisdict = {
#     'brand de brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# thisdict.pop('model')  # folosim metoda pop cu numele cheii
# print(thisdict)
# thisdict.popitem()  # scoate ultima valoare din dictionar, adica 1964 de la year
# print(thisdict)
# del thisdict['model'] # dam delete la cheia 'model
# print(thisdict)
# del thisdict  # sterge dictionarul cu totul
# print(thisdict)  #NameError: name 'thisdict' is not defined

#  Copiere
# thisdict = {
#     'brand de brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# Cu metoda dict de dict
# thisdict = {
#     'brand1': 'Ford',
#     'model2': 'Mustang',
#     'year3': 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# nested dictionaries  - adica dictionar in dictionar

# myfamily = {
#     'child1': {
#     'name': 'Emil',
#     'year': '2004'
#     },
#     'child2':{
#         'name': 'Tobias',
#         'year': '2007'
#     },
#     'child3': {
#         'name': 'Linus',
#         'year': 2011
#     },
# }
# print(myfamily['child1']['name'])
# print(myfamily['child2']['year'])
# print(myfamily['child3'])

#  SET
'''
● Set-urile păstrează mai multe valori unice într-o variabilă. (gen CNP)
● Nu sunt ordonate sau indexate.
● Datorită acestui fapt sunt și imutabile (nu putem schimba locația elementelor).
● Se pot doar adăuga sau șterge elemente.
● Putem folosi len() pentru a afla dimensiunea.
'''
# thisset = {'apple', 3, 'cherry'}
# print(thisset)
# thisset = {'apple', 'banana', 'cherry', 'apple'}  # returneaza o valoare o singura data
# print(thisset)
#
# #  Accesare itemi din set
# thisset = {'apple', 'banana', 'cerry'}
# for x in thisset:
#     print(thisset)

# # Verificam daca un anumit item este in set
# thisset = {'apple', 'banana', 'cerry'}
# print('banana' in thisset)  # returneaza True
# print('kiwi' in thisset)  # returneaza False
#
# Adaugare elemente in set
# thisset = {'apple', 'banana', 'cerry'}
# thisset.add('orange')
# print(thisset)
#
# # Adaugare item dintr-un alt set
# thisset = {'apple', 'banana', 'cerry'}
# tropical = {'pineapple', 'mango', 'papaya'}
# thisset.update(tropical)
# print(thisset)
#
# # Adaugarea unei liste la un set
# thisset = {'apple', 'banana', 'cerry'}
# mylist = ['kiwi', 'orange']
# thisset.update(mylist)
# print(thisset)
#
# # Scoatere element din set
# thisset = {'apple', 'banana', 'cerry'}
# thisset.remove('banana')
# print(thisset)
#
# # Discard pt anumiti itemi
# thisset = {'apple', 'banana', 'cerry'}
# thisset.discard('banana')
# print(thisset)
#
# #  Scoatem item rendom
#
# thisset = {'apple', 'banana', 'cerry'}
# x = thisset.pop()
# print(x)
# print(thisset)
#
# # Golim setul
# thisset = {'apple', 'banana', 'cerry'}
# thisset.clear()
# print(thisset)
#
# # Stergem un set
# thisset = {'apple', 'banana', 'cerry'}
# del thisset
# print(thisset)  # NameError: name 'thisset' is not defined
#
# # Unim doua seturi - Union creeaza un nou set cu itemii din celel doua
# set1 = {'a', 'b', 'c'}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)
#
# # metoda update - updateaza set1 cu itemii din set2 (returneaza ca si Union)
# set1 = {'a', 'b', 'c'}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# union si update vor exclude orice duplicate

#  TUPLE  - are elemente imutabile
'''
● Păstrează mai multe valori imbutabile într-o singură variabilă.
● Valorile sunt ordonate, încep de la index 0.
● Valorile sunt imutabile, odată definite, așa rămân. Nu se mai pot adăuga/șterge valori.
● Acceptă valori duplicate.
● Putem folosi len() pentru a afla dimensiunea.
'''
#
# thistuple = ('apple', 'banana', 'cerry')
# print(thistuple)
# print(thistuple[2])
#
#  # work around pt a schimba valorile unei tuple
# x = ('apple', 'banana', 'cerry')  # tupla
# y = list(x)  # convertim tupla in lista
# y[1] ='kiwi'  # ii schimbam un elemet -> [1]
# x = tuple(y)  # convertim lista inapoi in tupla
# print(x)
#
# # Adaugare elemente trebuie sa convertim
#
# thistuple = ('apple', 'banana', 'cerry')  # tupla initiala
# y = list(thistuple)  # convertire la lista
# y.append('orange')  #  append pentru a adauga la lista un element la final
# thistuple = tuple(y)  # convertesc inapoi la tupla
# print(thistuple)
#
# # Update tuple
# thistuple = ('apple', 'test', 'cerry')
# y = ('orange',) # atentie are o virgula dupa element
# thistuple += y  # la fel ca thistuple = thistuple + y
# print(thistuple)
#
# # Unpacking
# fruits = ('apple', 'test', 'cerry')
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)
#
# # Numarul variabilelor trebuie sa fie egal cu nr-ul valorilor din tupla (natch)
#
# #  unire a doua tuple
# tuple1 = ('a', 'b', 'c')
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# # Multiplicarea
# fruits = ('apple', 'banana', 'cerry')
# mytuple = fruits * 2
# print(mytuple)
#
# # Lungimea unei Tuple
# fruits = ('apple', 'banana', 'cerry')
# print(len(fruits))

# Metode Tuple
# http://www.w3schools.com/python_tuples_methods.asp
