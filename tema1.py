# '''
# Tema 1 _ Setup, Variabile, Tipuri de date
# Exerciții Recomandate - grad de dificultate: Ușor .
# 1. Revizualizează întâlnirea 1 și ia notițe în caz că ți-a scăpat ceva.
# 2. Vizualizează din videoul ‘Primii pași în Programare’:
# - Variabile și Tipuri;
# - Operatori și Flow Control.
# Astfel, la întâlnirea LIVE deja va fi a 2-a oară când vei auzi conceptele și sigur ți
# se vor întipări mai bine în minte.
# Link: https://www.itfactory.ro/8174437-intro-in-programare/


# '''
# '''
#          TEMA 1  Exerciții obligatorii - grad de dificultate: Ușor spre Mediu:
# '''

# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabila este un tip de date stocata in memoria unui computer

# '''
# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă :
# - string
# - int
# - float
# - bool
# Observație: Valorile vor fi alese de tine după preferințe.
# '''
nume = 'Sergiu'
prenume = 'Gavrila-Ursa'
varsta = 39
inaltime = 1.79
saten = True
# print('Ma numesc ' + nume + ' am varsta de ' + str(varsta) + ' ani ' + ' si inaltimea de ' + str(inaltime) + ' si sunt ' + str('saten'))
# print(f'{nume} \n{varsta} \n{inaltime} \n{saten}')

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
# nume = str('Sergiu')
# print(type(nume))
# varsta = int('39')
# print(type(varsta))
# inaltime = float(1.79)
# print(type(inaltime))
# saten = bool(True)
# print(type(saten))

'''
 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
# print(round(inaltime, 1))
# inaltime = float(1.7)
# print(type(inaltime))

'''
5. Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
# print('Numele meu este ' + nume)
# print('Am varsta de ' + str(varsta) + ' ani.')
# print('Inaltimea mea este de ' + str(inaltime))
# print('Culoarea parului meu este satena ' + str(saten))

# '''
# 6. Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
# '''
# nume = input('Introdu numele\n')
# prenume = input('Introdu prenumele\n')
# lung_nume = len(nume) + len(prenume)
# print(f'Numele complet este {len(nume + prenume)}')
'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
# lungimea = int(input('Introdu lungimea\n'))
# latimea = int(input('Introdu latimea\n'))
# aria = lungimea * latimea
# print('Aria dreptunghiului este', aria)

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
'''
# narativ = 'Coral is either the stupidest animal or the smartest rock'
# print(narativ.count(' the'))
# print(narativ.replace('the', 'THE', 3))
'''
# 10. Același string.
# ● Folosiți un assert ca să verificați dacă acest string conține doar numere.
# '''
# narativ = 'Coral is either the stupidest animal or the smartest rock'
# print(type(narativ))
# assert narativ == str('Coral is either the stupidest animal or the smartest rock')
# print('narativul este un string')
# assert narativ == int('Coral is either the stupidest animal or the smartest rock')
# print('narativul contine doar numere')

''''
       Exerciții Opționale - grad de dificultate: Mediu spre greu
         (s-ar putea să ai nevoie de Google).
'''
'''1. Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
 '''
# cuvant = input('Introdu cuvantul\n')
# lungime_cuvant = len(cuvant)
# print(lungime_cuvant)
# print(cuvant[2])
# print(f'Caracterul din mijloc este ') #-vezi tema rezolvat

# # 2. Folosind assert, verifică dacă un string este palindrom.
# x = input('palindrom\n')
# assert x == x[::-1]
# print('este un palindrom')

'''
3. Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
# glasul_copilariei = input('Introdu\n')
# print(glasul_copilariei)
# glasul = input('Alabala\n')
# copilariei = input('Portocala\n')
# print(glasul)
# print(copilariei)
# print(glasul + ' ' + copilariei)

'''
4. Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
# myStr = input('alabala portocala\n')
# s = myStr[1:16].replace('a', 'A')
# print(f'{myStr[0]}{s}{myStr[16]}')
# # cu ajutorul Alinei
'''
5.Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''
# User= input("User:")
# Parola = input("Parola:")
# Lungime_parola=len(Parola)
# print(f'Parola pentru Userul {User} este {Lungime_parola * "*"}  si are {len(Parola)} caractere')
# # cu ajutorul lui Cosmin