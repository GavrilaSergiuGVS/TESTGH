from datetime import date

from helper import Scoala, TableIt
from helper import Cerc
from helper import Dreptunghi
from helper import Angajat
from helper import ContBancar

# Functie care sa returneze daca un nume este nume de fata sau de baiat
# def gen_nume():
#     nume = input('Scrie numele:\n')
#     if nume[-1] == 'a' and nume != 'Mircea' and nume != 'Luca':
#         print('Acesta este un nume de fata')
#     elif nume == 'Mircea' or nume == 'Luca':
#         print('Acesta este un nume de baiat')
#     elif nume == 'Carmen' or nume == 'Beatrice':
#         print('Acesta este un nume de fata')
#     else:
#         print('Acesta este un nume de baiat')
#
#
# gen_nume()

# Sau dupa Matei
# def gen_nume():
#     lista_exceptii_fete = ['Carmen', 'Beatrice']
#     lista_exceptii_baieti = ['Mircea', 'Luca']
#     nume = input('Scrie numele:\n')
#     if nume in lista_exceptii_fete:
#         print("Nume de fata")
#     elif nume in lista_exceptii_baieti:
#         print("Nume de baiat")
#     elif nume[-1] == 'a' and nume not in lista_exceptii_fete:
#         print("Nume de fata")
#     else:
#         print("Nume de baiat")
#
#
# gen_nume()


''' CLASA, OBIECT, CONSTRUCTOR, CLASA IMPORTATA DIN ALT FISIER
Intalnirea 6 -Ce este o CLASA?
● O clasă este o rețetă (blueprint) pentru crearea obiectelor
● Ea conține elemente descriptive: atribute/fields
(practic niste variabile)
● Conține acțiuni posibile: metode (practic niște funcții)
● Self - este instanță clasei, ajută funcția să aibă acces
la atributele clasei
● Deci o clasă este doar un concept, cum ar fi o rețetă pentru
paste carbonara. Faptul că există rețetă nu înseamnă că
există și pastele.
● Dar aceeași rețetă o putem folosi ca să facem 1, 2, 100
de porții carbonara.
'''

# class Car:
#     # fields / attributes ( caracteristicile pe care poate sa le aiba clasa Car)
#     make = 'Dacia'
#     model = None
#     year = 2023
#     color = 'alb'

# contructorul se defineste dupa atribute si inainte de metode
# def __init__(self, model, color):
#     self.model = model
#     self.color = color

# METODE (methods) - actiunile pe care poate sa le faca sau sa le suporte clasa noastra
# def accelerate(self):  # def startup(self): functia de deschidere
#     print('Masina accelereaza: Vrrrum, vrum')
'''  Pe scurt un test case apare asa:
#   def startup(self): functia de deschidere
#      se executa pasii test case-urile
#      pas 1
#      pas 2
#      pas 3
#    def teardown(self): functia de inchidere care sterge tot
'''
#      def rezervor(self):
#        print(f'Rezervorul are capacitatea de {}, litri')
#
#
# def change_color(self, color):  # color este unparametru care devine argument
#     self.color = color
# exemplu pt change color:
# car1 = Car()
# car1.color = 'red'
# print(car1.color)

#
# def model_masina(self, model):
#     self.model = model
#
#
# def stop(self):  # teardown(self): functia de inchidere care sterge tot
#      print('Masina s-a oprit')

'''  Ce este un OBIECT?
● Obiect = instanță a clasei
● Toate obiectele de tip Car vor avea același comportament

○ Aceleași atribute
○ Aceleași metode
○ Atributele pot suferi modificări după inițializarea obiectului
○ Ex: o mașină se poate vopsi într-o culoare nouă

● Putem crea oricâte obiecte de tip Car dorim
● Acesta e și avantajul OOP: write once, use n times
'''
# obiecte de tipul Car() -ne creem masinile pe care vrem sa le vedem /folosim/testam
# fiecare dintre obiecte are acces la toate atributele si metodele clasei

# car1 = Car()  # car1 = obiect de tip Car()
# car2 = Car()
# print(car1.make)
# print(car2.make)
# car1.color = 'albastru'
# car1.model = 'Duster'
# car2.color = 'galben'
# car2.model = 'Logan'
# print(car1.color)
# print(car1.model)
# print(car1.accelerate())
# print(car1.stop())
# print(car2.color)
# print(car2.model)
# print(car2.accelerate())
# print(car2.stop())


'''Ce este un constructor?
● Constructor se asigură că la crearea obiectelor setăm
niște date fără de care obiectul nu are sens să existe

● Practic atribuie valori atributelor
● Dacă ne gândim la un formular, ar fi acele field-uri cu *

care sunt OBLIGATORII / sau permanetizam

● Dacă prin constructor suntem obligați să dăm model și
color, nu am putea să instanțiem obiecte de tip
Car fără să dăm aceste valori obligatorii
'''

# vezi contructorul care se defineste dupa atribute si inainte de metode

# class Car:
#     make = 'Dacia'
#     model = None
#     year = 2023
#     color = 'alb'
#
# # contructorul se defineste dupa atribute si inainte de metode
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
#     def accelerate(self):  # def startup(self): functia de deschidere
#         print('Masina accelerate: Vrrrum, vrum')
#
#     def change_color(self, color):  # color este unparametru care devine argument
#         self.color = color
#
#     def model_masina(self, model):
#         self.model = model
#
#     def stop(self):  # teardown(self): functia de inchidere care sterge tot
#         print('Masina s-a oprit')
#
#
# car1 = Car('Duster', 'albastru')  # car1 va trebui sa aiba argumentele'model' si 'culoare' din cauza constructorului
# car2 = Car('Logan', 'galben')  # similar car1 va avea acceasi obligativitate de argumente: 'model' si 'culoare'
# print(car1.make)
# print(car2.make)
# car1.color = 'albastru'
# car1.model = 'Duster'
# car2.color = 'galben'
# car2.model = 'Logan'
# print(car1.color)
# print(car1.model)
# print(car1.accelerate())
# print(car1.stop())
# print(car2.color)
# print(car2.model)
# print(car2.accelerate())
# print(car2.stop())

'''
Cum importăm clase din alte fișiere?
● from folder.folder.fișier import nume_clasă
'''
# Am definit in helper -> class Scoala:
# scoala1 = Scoala('tip_seral', 'profil_mate-info')
# print(scoala1.profil_real)
# print(scoala1.tip)
# print(scoala1.nr_elevi)
#
# scoala2 = Scoala('tip_liceu_teoretic', 'profil_uman')
# print(scoala2.profil_real)
# print(scoala2.tip)
# print(scoala2.nr_elevi)