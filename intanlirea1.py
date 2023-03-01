# #      Printam in consola un mesaj Hello World + Comentarii
# print('Test')
# print('Hello world')  # cel mai simplu program Python
#
# print('acsta este un comment')
#
# '''
# Comentarii multiple lines
# linia 2
# linia 3
# comentariile nu fac parte din cod
# Python nu le considera parte din program si nu le interpreteaza
# sunt notite pentru tine si colegii tai programatori
# '''
# # Comment pe mai multe linii
# # Comment pe mai multe linii
# # Comment pe mai multe linii
#
# # selectezi liniile si cu CTRL + / = bulk comment
#
# print('MC\'Donalds1\nTest1\nTest2\nTest3')  # escapare
#
# print("Mc'Donalds2")
# print('MC\'Donals3')

# #          Declaram si initializam variabile

# marcaMasina = 'Volvo'  # string
# an_fabricatie = 2005  # integer
# pret = 15000.50  # float
# inmatriculata = False  # boolean

# print(marcaMasina)
# print(an_fabricatie)
# print(pret)
# print(inmatriculata)

# #   suprascriem si schimbam tipul variabilei daca dorim

# marcaMasina = 'Volvo'
# an_fabricatie = 1785
# pret = '15000.50'  # string
# inmatriculata = True

# print(marcaMasina)
# print(an_fabricatie)
# print(pret)
# print(inmatriculata)

# #  mai multe variabilee one line initialization

# x, y, z = 'test1', 'test2', 'test3'
# print(x, y, z)
# print(f'{x}\n{y}\n{z}')
# print(f'numele meu este {x}')

# # sau aceeasi valoare mai multor variabile

# x = y = z = 799
# print(x, y, z)
# print(f'{x}\n{y}\n{z}')

# #    ca sa-i dau cate zecimale vreau unei variabile float
# a = 5.3245897123
# print('{0:.5f}'.format(a))
# aceasta e sintaxa - merge si
# fara 0 si o ia de la inceput mereu {:.5f}
#
# # pentru rotunjire avem round
# #putem rotunji si la zecimale
# print(round(a))
# print(round(a, 2))

# #    Functia Type() si Type casting

# # Pentru Type integer

# x = int(1)
# y = int(2.8)  # ne returneaza typ-ul clasei de care aparine, adica integer(nu 2.8 ci 2)
# z = int('3')

# print(x, y, z)
# print(type(x))
# print(type(y))
# print(type(z))

# # similar pentru Type float

# x = float(1)
# y = float(2.8)
# z = float('3')
# w = float('4.2')

# print(x, y, z, w)
# print(f'{x} \n{y} \n{z} \n{w}')
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(w))

# # similat pentru Type string

# x = str('S1')
# y = str(2.8)
# z = str('3')

# print(x, y, z)
# print(f'{x} \n{y} \n{z}')
# print(type(x))
# print(type(y))
# print(type(z))

# #    Functia print

# nume = 'Minzala '
# prenume = 'Daniela'
# print(nume + prenume)
# varsta = 53.12
# job = 'tester'
# print('Numele meu este ' + nume + prenume + ' si am ' + str(varsta) + ' ani')
# print(f'Numele meu este { nume} { prenume} si am { varsta} ani')  #cea mai buna solutie pt print
# print('Numele meu este {0} {1}, am {2} ani si sunt {3}'.format(nume, prenume, varsta, job))  # nu prea se foloseste

# #    Functia Assert
# a = 1
# # Il intreb pe Python: Hei, a = 1?
# print(a == 1)
#
# assert a == 1  # daca asertul este corect, adica e True, nu exista nici un feedback vizual si ma lasa sa trec mai departe
# print('Trec pe-aici')
# assert a == 2  # daca asertul nu este corect, adica e False, nu executa liniile de cod urmatoare
# print('Am ajuns pana aici')

# # Se poate si cu if/else care echivaleaza assert-ul
# a = 1
# b = 2
# c = 3
# if c == a + b:
#     print('Adevarat ca c este 3')
# else:
#     print('Incorect')
# assert c == a + b
# print('c este corect')   # se afiseaza pt a = 1, b = 2
# # pentru a = 5 returneaza eroarea AssertionError


# #    Functia Input - Ne ajuta sa luam date de la tastatura si sa le salvam intr-o variabila

# # Se poate face type casting pe input; daca nu va lua by default type string

# parola_user = input('Introdu parola\n')
# parola = 'parola1234'
# assert parola_user == parola
# print('Te-ai logat cu succes')

# # ca si exemplu:
# var = 12345
# user_var = int(input('Introdu un nr de la tastatura\n'))
# assert var == user_var
# print('cele doua numere sunt egale')
# print(var + user_var)

# #    String( Index, len(), slicing, metode)
#
# #  String Index
# # Indexarea incepe de la zero!!!
# str = 'Acesta este string-ul meu si fac ce vreau cu el'
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str[4])
# print(str[5])
#
# # String len()
# print(len(str))
# print(str[46])  # daca vreau sa returnez ultime litera din str-ul meu, adica l
# #luand in considerare ca indexarea incepe de la zero, ultimul index va fi len-1
# print(str[47])  # ultimul index va returna :IndexError: string index out of range

# # String slicing
# # cu Slicing taiem din String
# str2 = 'Azi e miercuri'
# print(str2[0])
# print(str2[0:2])  # 0 e locul de unde incepe si 2 locul unde sa se termine; pot sa las si fara 0, [:2]
# print(str2[:5])
# print(str2[3:5])
#
# # pentru parcurgerea inversa
# print(str2[::-1])

# #     Metode - Exemple de slicing
# # # luand in considerare ca indexarea incepe de la zero, ultimul index va fi len-1
# str3 = 'String de test'
# print(len(str3))
# last_index = len(str3)-1
#
# print(str3[13])
# print(str3[0:last_index])
# print(str3[0:13:2])  # 0 e indexul de start, 13 indexul pana la care merge, 2 pasul cu care sare
#
# # Alta sintaxa - care nu prea e uzuala
#
# String = "ASTRING"
#
# s1 = slice(3)
# s2 = slice(1, 5, 2)
# print(String[s1])
# print(String[s2])