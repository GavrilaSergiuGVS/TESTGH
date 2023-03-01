#   Intalnirea 4 - CICLURI REPETITIVE

'''   while / while else
● Se execută un bloc de cod atât timp cât o condiție e adevărată.
● Opțional: la final se poate pune else, această zonă se execută o dată, la final.
'''

# i = 0
# while i < 3:
#   print(i)
#   i += 1
# # obtional putem avea si else:
# else:
#     print('Am terminat ciclul')
#
# i = 6
# while i > 0 < 6:
#   print(i)
#   i -= 1

'''  Continue
● Cuvântul cheie ‘continue’ va sări peste iterația actuală.
● E un fel de skip.
● Se va sări peste blocul de cod de după skip, care ține de for/ while.
'''

# i = 0
# while i < 6:
#   i += 1
#   if i == 2:
#     continue
#   print(i)   # sare peste 3 la printare, adica excludem din rezultate

# i = 0
# while i < 89888888:
#   i += 900
#   i += 1232131
#   i += 1
#   if i == 2:  # dau debug si vad la ce rezultat am ajuns
#     continue
#   print(i)

# # Exemplu pt citit de la coada la cap:
#
# n = input('Type a string:\n')
# list = list(n)
# print(list)
# reverse = list[::-1]
# count = ''
# for i in reverse:
#   count += i
#   if len(count) ==len(n):
#     print(count)
#   else:
#     pass  # nu o sa ajunga niciodata la else in acest caz


# # sau def o FUNCTIE() apoi apelez o functie:
# i = 0
# while i < 6:
#     i += 1
#     if i == 2:
#      continue
#     print(i)

# functie()->>> cu zece obiecte cap - la - cap obtii un test case

'''break  - practic opreste iteratia
● Cuvântul cheie ‘break’ va opri iterația.
● Practic se iese automat din loop.
● Nu se mai execută codul de după break, din cadrul unui for/ while.
'''
# folosim de obicei atunci cand cautam dupa un element exact

# i = 1
# while i < 6:  # cand avem elemente pe care nu le stim exact
#   print(i)
#   if i == 3:
#     break
#   i += 1
#
# # Exemplu pt break:
# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
# name = input('Enter name\n')
# for contact in contacts:  # for folosim cand stim exact elementele
#     if name == contact[0]:
#         print(name, "is", contact[1])
#         break
# else:
#     print('Not Found')


'''FOR/ FOR ELSE
● Se execută un bloc de cod pentru fiecare valoare din range.
● Range seamănă cu slicing. Ne spune:
○ De unde începem? Default e 0.
○ Până unde iterăm?
○ Opțional: pasul.
● Opțional: la final se poate pune else.
○ această zonă se execută o dată, la final.
'''
# for i in range(4):
#   print(i)

# sau ...este ca si la slicing cu index de inceput, sfarsit si pas
# for i in range(100, 0, -5):  # parcurgere inversa (descrescatoare) trebuie pus minus la pas
#   print(i)
# else:
#   print('Am ajuns la final') # La fel, else nu este obligatoriu sau esential
# for i in range(0, 101, 5):
#   print(i)

# for i in range(0, 101, 5):  # parcurgere crescatoare
#   print(i)

'''
Folosim si aici CONTINIU
'''

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue  # excludem item din lista
#   print(x)

'''
 Folosim si aici BREAK
'''
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#   if fruit == "cherry":
#     break
#   print(fruit)

''' FOR EACH
● Se parcurge o colecție și se salvează fiecare element într-o variabilă.
● La fiecare iterație, variabila se va suprascrie cu valoarea actuală.
● Rând pe rând, se vor parcurge toate elementele dintr-o colecție.
'''
# masini1 = ['Audi', 'Volvo', 'Mercedes']
# for masina in masini
#     print(f'<asina mea preferata este FOR EACH {masina}')

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#   for y in fruits:
#     print(x, y)

# # daca vrem sa schimbam una dintre valorile din lista de mai sus accesam indexul respectiv
# culori = ['rosu', 'albastru', 'verde', 'galben']
# for culoare in culori:
#     print(f'Culoarea mea preferata este {culoare}')

# fruits = ["apple", "banana", "cherry"]
# print(f'Lista initiala = {fruits}')
# for i in range(len(fruits)):
#   if fruits[i] == 'cherry':
#     fruits[i] = 'kiwi'
# print(fruits)
