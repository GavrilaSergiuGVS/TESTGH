# Operatori
import hint as hint

# De ATRIBUIRE

# x = 3
# print(x)
# x += 3  # la fel cu x = x + 3 = 6 (practic e exemplu de suprascriere)
# print(x)
# x -= 3  # la fel cu x = x - 3 = 3
# print(x)
# x *= 3  # la fel cu x = x * 3 = 9
# print(x)
# x /= 3  # la fel cu x = x / 3 returneaza float 3.0
# print(x)

#
# # ARITMETICI
#
# x = int(input('Introdu x\n'))
# y = int(input('Introdu y\n'))
# z = x + y
# n = x - y
# p = x * y
# l = x / y
# k = x % y  # modulus
# i = x ** y  # Eponexcetion
# print(z)
# print(n)
# print(p)
# print(l)
# print(k)
# print(i)
# # mai putem sa scriem si pe o singura line:
# print(z,n, p, l, k, i)
# # sau scrierea codului pe o singura line:
# print(f'{z}, {n} {p} {l} {k} {i}')

# de COMPARARE

# a = 5
# b = 6

# assert a == b  # comparam a egal cu b
# assert a != b  # comparam a diferit de b
# assert a > b
# assert a < b
# assert a >= b
# assert a <= b

#  OPERATORI LOGICI

# and - returneaza True daca ambele statement-uri sunt adevarate
# or - returneaza True daca cel putin una dintre statement-uri este adevarat
# not - face reverse la rezultat, adica returneaza False daca rezultatul este adevarat
# exemplu: not(x < 5 and x <10)

# x = 5
# y = 6
# z = 11

# assert x == 5 and y == 6 and z == 11  # functioneaza daca toate sunt adevarate
# # print('assert ok')
# assert x== 5 or y == 6 and z == 11  # daca una dintre a si b este adevarat atunci functioneaza
# print('assert ok')
# assert not (x < 9 and y < 9 and z < 12) # paranteze ca sa nu dea not doar la x - NU va functiona
# assert not (x > 9 and y < 9 and z < 12)  # paranteze ca sa nu dea not doar la x - va functiona

# IF (flow control)

# a = 3
# b = 5

# if a == 3: #incep cu afirmatie si verific cand a = 3
#     print('a este 3')
# else:
#     print('a nu este 3')  # daca pun a = 4 afiseaza "a nu este 3"
# assert a == 3   # varianta simpla in loc de if/else

# if not a == 3:  # negatie si verific cazul a nu este  = 3
#     print('a nu este 3')
# else:
#     print('a este 3')
# assert not a == 3   # varianta assert a!=3 in loc de if not/else

# Exemplu negativ - adica am doua numere si verific typr-ul
# if not type(a) == int:
#     print('Tipul lui a nu este int')
# else:
#     print('Tipul lui a este int')
#
# a = 5
# b = 5
# if a == 3:
#     if b == 5:
#         print('Test')
#     else:
#         print('Test2')
# else:
#     print('Test3')

#  IF, ELSE IF, (ELIF), ELSE

# a = 3
#
# if a == 1:
#     print('ati ales limba romana')
# elif a == 2:
#     print('ati ales limba engleza')
# elif a == 3:
#     print('ati ales limba franceza')
# else:
#     print('Nu exista optiunea aleasa')

# str = 'tst'
# if str == 'tst':
#     print('TST is tst')  # un exemplu de IF solitar

# a = 36
#
# if a < 35:
#     if a == 9:
#         print('Test')
#     elif a > 14:
#         print('Test2')
#     elif a == 3:
#         print('Test3')
# else:   # exista un singur else care inchide
#     print('Test 4')

# x = int(input('Introdu valoarea'))
# if x == 5:
#     print('Bravo')
# elif x <10:
#     print('Ok')
# else:
#     print('Nuuu')