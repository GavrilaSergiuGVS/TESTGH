
#   Tema 3 _ Structuri de date
'''
I.
Exerciții Recomandate - grad de dificultate: Ușor
1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare' (Daca nu ai
facut-o deja)
3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'. Astfel, la
intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele si sigur ti se vor intipari in
minte mai bine. Link video: https://www.itfactory.ro/8174437-intro-in-programare/
'''
'''
II.
Exerciții obligatorii - grad de dificultate: Ușor spre
Mediu:

1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.
'''
# # 1a
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
# print(note_muzicale)
# # 1b
# note_muzicale[0:8] = ['si', 'la', 'sol', 'fa', 'mi', 're', 'do']
# print(note_muzicale)
# note_muzicale.reverse()
# print(note_muzicale)

# # 2. De cate ori apare do?
# note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# note_muzicale.count('do')
# print(note_muzicale.count('do'))
#
# # 3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# # Gasiti 2 variante sa le uniti intr-o singura lista.
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list3 = list1 + list2
# print(list3)
# for x in list2:
#     list1.append(x)
# print(list1)
#
# # 4. Sortati si afisati lista generata la ex anterior
# # Stergeti numarul 0 folosind o functie
# # Afisati iar lista
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# lista3.sort()
# print(lista3)
# lista3.remove(0)
# print(lista3)

# 5. Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala (IF)
# Lista nu este goala (ELSE)
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# if lista3 == [3, 1, 0, 2, 6, 5, 4]:
#     print('Lista nu este goala')
# # else:
# #     print('Lista este goala')
# lista3.clear()
# print('Lista este goala')
#
# # 6. Foloseste o functie care sa goleasca lista de la exercitiul 3
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# lista3.clear()
# print(lista3)

# # 7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
# afiseze ca lista e goala
# lista3 = [3, 1, 0, 2, 6, 5, 4]
# if lista3 == [3, 1, 0, 2, 6, 5, 4]:
#     print('Lista nu este goala')
# lista3.clear()
# print('lista este goala')

# # 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5},
# # foloseste o functie ca sa afisezi Elevii (cheile)
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# x = dict1.keys()
# print(x)
#
# # 9. Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
# # Ex: ‘Ana a luat nota {x}’.
# # Doar nota o vei lua folosindu-te de cheie
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# print('Ana a luat nota:', dict1['Ana'])
# print('Gigel a luat nota:', dict1['Gigel'])
# print('Dorel a luat nota:', dict1['Dorel'])

# varianta Lidia + Petre
9# dict1 = {#     'Ana': 8,#     'Gigel': 10,#     'Dorel': 5# }# x = dict1.get('Ana')# y = dict1.get('Gigel')# z = dict1.get('Dorel')# # x = dict1['Ana']# # y = dict1['Gigel']# # z = dict1['Dorel']# print(f'Ana a luat nota {x}.')# print(f'Gigel a luat nota {y}.')# print(f'Dorel a luat nota {z}.')

# # 10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# # - Modifica nota lui Dorel in 6
# # - Printeaza nota lui dupa modificare
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1['Dorel'] = 6
# print('Dorel a luat nota:', dict1['Dorel'])
#
# # 11. Imagineaza-ti ca Gigel se transfera din clasa.
# # - Cauta o functie care sa il stearga
# # Vine un coleg nou.
# # - Adaugati-l in lista pe Ionica, cu nota 9
# # - Printati dictionarul cu noii elevi
# dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# dict1.pop('Dorel')
# print(dict1)
# dict1['Ionica'] = 9
# print(dict1)

# 12. Ai urmatoarele seturi:
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# - Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
# - Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(zile_sapt)  # returneaza 'luni' o singura data

# 13. Foloseste un if si verifica daca:
# - Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
# regasesc intre elementele din setul zile_sapt)
# - Weekend nu este un subset al zilelor din sapt
# Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
# punct de mai sus va fi un boolean
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# !!!!!!
# if weekend != zile_sapt:
#     print(weekend in zile_sapt)  # returneaza False
# if weekend < zile_sapt:
#     print('Weekend este un subset al zile_sapt')
# if weekend > zile_sapt:
#     print('weekend nu este un subset al zile_sapt')

# Varianta Matei
# zile_sapt = {'sambata', 'duminica', 'luni'}
# weekend = {'sambata', 'duminica'}
# if weekend.issubset(zile_sapt):
#     print('Este subset')
# else:
#     print('Nu este subset')
#
# if zile_sapt.issuperset(weekend):
#     print('Este supraset')
# else:
#     print('Nu este supraset')

# Varianta Lidia + Petre
# 13# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# if weekend < zile_sapt:
# __________<<< de ce operatorul asta?#     print(True)# else:#     print(False)# if weekend.issubset(zile_sapt):
#     print(True)
# else:
#     print(False)


# # 14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# # sunt in weekend si invers)
# print(zile_sapt - weekend)
# print(weekend - zile_sapt)
#
# # 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
# # ambele seturi). Hint: Va puteti folosi de o functie
#
# y = zile_sapt - weekend
# print(weekend - y)

'''
Exerciții Opționale - grad de dificultate: Mediu spre
greu (s-ar putea să ai nevoie de Google).

1. Ne imaginam o echipa de fotbal in timpul meciului. Sunt permise maxim 3 schimbari.
- Declara o lista cu 5 jucatori: lista_jucatori_teren
- Declara o lista cu 5 jucatori de rezerva: lista_jucatori_rezerva
- Declara o lista goala cu jucatori scosi din teren: lista_jucatori_scosi
- Schimbari_efectuate = joaca-te cu valori diferite ca sa vezi cum trec datele prin cod
- SCHIMBARI_MAX va fi o constanta cu valoarea 3
Daca Jucatorul x e in teren si mai avem schimbari la dispozitie atunci:
- Efectuam schimbarea daca jucatorul e in lista de rezerve si nu exista in jucatorii de pe
teren
- Stergem jucatorul scos din lista de teren si il adaugam in lista de jucatori scosi
- Adaugam jucatorul intrat in lista de jucatori de pe teren si il scoatem din lista de jucatori
de rezerva
- Afisam pe ecran: a intrat x, a iesit y. Mai aveti z schimbari (inlocuiti x, y si z cu numele
variabilelor voastre)
Daca jucatorul pe care vrem sa il schimbam nu e in teren:
- Afisati ‘nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Altfel, afisati ecran: ‘mai aveti z schimbari’
Google search hint: “how to check if item is in list python”
'''

# lista_jucatori_teren = ['portar', 'fundas', 'libero', 'atacant', 'varf']
# lista_jucatori_rezerva = ['r_portar', 'r_fundas', 'r_libero', 'r_atacant', 'r_varf']
# lista_jucatori_scosi = []
# schimbari_max = 3
#
# x = 'fundas'
# if x in lista_jucatori_teren:
#     print('fundas este in teren')
# lista_jucatori_teren[1] = 'r_fundas'
# lista_jucatori_scosi.append('fundas')
# print(lista_jucatori_teren)
# print(lista_jucatori_scosi)
# if x not in lista_jucatori_teren:
#     print('Nu se poate efectua schimbarea, fundas nu este in teren')
# schimbari_max = int(schimbari_max -1)
# print('A intrat', lista_jucatori_teren[1], ',' 'a iesit:', lista_jucatori_scosi[0], 'si mai aveti:', int(schimbari_max), 'schimbari')

# Exercitii Petre

# 1 (optional)
# #
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 1
# SCHIMBARI_MAX = 3
# x = str(input('Iese de pe teren: \n'))
# y = str(input('Intra pe teren: \n'))
# z = SCHIMBARI_MAX - schimbari_efectuate
#
# if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#     lista_jucatori_teren.remove(x)
#     lista_jucatori_rezerva.remove(y)
#     lista_jucatori_scosi.append(x)
#     lista_jucatori_teren.append(y)
#     print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#     print(f'Jucatori pe teren: {lista_jucatori_teren}')
#     print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#     print(f'Jucatori scosi: {lista_jucatori_scosi}')
# elif x not in lista_jucatori_teren:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
# elif y not in lista_jucatori_rezerva:
#     print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
# else:
#     print(f'Limita schimbari depasite! {z} schimbari ramase')

#_______________________________________________________________________________________________________

# Tentativa de For loop
#
# lista_jucatori_teren = ['Marius', 'Adi', 'Dan', 'Alex', 'Bubu']
# lista_jucatori_rezerva = ['Vlad', 'Gigi', 'Mihai', 'Dorin', 'Alin']
# lista_jucatori_scosi = []
# schimbari_efectuate = 0
# SCHIMBARI_MAX = 3
#
# for i in range(0, 3):
#     x = str(input('Iese de pe teren: \n'))
#     y = str(input('Intra pe teren: \n'))
#     schimbari_efectuate +=1
#     z = SCHIMBARI_MAX - schimbari_efectuate
#     if x in lista_jucatori_teren and y in lista_jucatori_rezerva and schimbari_efectuate <= SCHIMBARI_MAX:
#         lista_jucatori_teren.remove(x)
#         lista_jucatori_rezerva.remove(y)
#         lista_jucatori_scosi.append(x)
#         lista_jucatori_teren.append(y)
#         print(f'A intrat {y}, a iesit {x}, mai aveti {z} schimari.')
#         print(f'Jucatori pe teren: {lista_jucatori_teren}')
#         print(f'Jucatori in rezerva: {lista_jucatori_rezerva}')
#         print(f'Jucatori scosi: {lista_jucatori_scosi}')
#     elif x not in lista_jucatori_teren:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {x} nu este pe teren.')
#     elif y not in lista_jucatori_rezerva:
#         print(f'Nu se poate efectua schimbarea deoarece jucatorul {y} nu este rezerva.')
#     else:
#         print(f'Limita de {z} a fost atinsa')

##---------------------------
 # Your program needs to take the key as input and output the corresponding value.
# # Sample Input
# # year
# # Sample Output
# # 2018

# car = {
#     'brand': 'BMW',
#     'year': 2018,
#     'color': 'red',
#     'mileage': 15000
# }

# # 9 line answer
# x = input()
# if x == 'brand':
#     print(car['brand'])
# elif x == 'year':
#     print(car['year'])
# elif x == 'color':
#     print(car['color'])
# elif x == 'mileage':
#     print(car['mileage'])

# 2 line answer
# x = input()
# print(car[x])

# # 1 line answer
# print(car[input()])

# # 1 line answer
# print(car.get(input()))

#__________________________________________________________________

# # You are working on data that represents the economic freedom rank by country.
# # Each country name and rank are stored in a dictionary, with the key being the country name.
#
# # Complete the program to take the country name as input and output its corresponding economic freedom rank.
# # In case the provided country name is not present in the data, output "Not found".
# # Recall the get() method of a dictionary, that allows you to specify a default value.

# data = {
#     'Singapore': 1,
#     'Ireland': 6,
#     'United Kingdom': 7,
#     'Germany': 27,
#     'Armenia': 34,
#     'United States': 17,
#     'Canada': 9,
#     'Italy': 74
# }

# # 5 line answer
# x = input()
# if x in data:
# 	print(data[x])
# else:
# 	print('Not found')

# # 1 line answer
# print(data.get(input(), 'Not found'))

#_______________________________________________________________________________________

# # You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact.
# # Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below:
#
# # Sample Input
# # John
#
# # Sample Output
# # John is 31
# # If the contact is not found, the program should output "Not Found".
#
# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]

# # 13 line answer
# x = input()
# if x == 'James':
#     print('James is 42')
# elif x == 'Amy':
#     print('Amy is 24')
# elif x == 'John':
#     print('John is 31')
# elif x == 'Amanda':
#     print('Amanda is 64')
# elif x == 'Bob':
#     print('Bob is 18')
# else:
#     print('Not found')
#