####################Prvi zadatak##################

# s = input('Unesite neki string: ')

# print('Vas string ima:',len(s), 'karaktera')
# print((s + ' ')* 10)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# if len(s) < 7:
#     print('Vas string nema dovoljnu duzinu. Minimum je sedam karaktera')
# else:
#     print(s[6])
# print(s[1 : -1])
# print(s.upper())
# print(s.replace('a', 'e'))
# •	String u kome je svako slovo ( alpha znak ) zamenjeno sa blanko znakom

###############################Drugi zadatak########################################

# a = input('Unesite recenicu: ')
# n = 1
# for i in range(len(a)):
#     if a[i] == ' ':
#         n += 1
#     else:
#         pass
# print('Vasa recenica se sastoji od',n, 'reci')

#############################Treci Zadatak##################################

# formula = input('Unesite formulu: ')
# leve = 0
# desne = 0

# for i in formula:
#     if i in '(':
#         leve += 1
#     elif i in ')':
#         desne += 1
#     else:
#         pass

# if leve != desne and leve == 0 or desne == 0:
#     print('Broj zagrada sa leve i desne strane nije jednak!!!')
# else:
#     print('Formula je ispravna. Broj levih i desnih zagrada je jednak')

######################Zadatak 4##############################################

# print('Unesi string da saznas ima li samoglasnika.') 
# unos = input('>>> ') 
# sam = 0
# for i in unos: 
#     if i in 'aeiouAEIOU': 
#         sam += 1
#     elif sam > 0:
#         print('Ima samoglasnika.')
#         break
#     elif i == ' ': 
#         continue 
#     elif i in '.,;:\'"-*': 
#         print('Karakter', i, 'nije slovo') 
#     else:
#         pass
# if sam == 0:
#     print('Nema samoglasnika.')
# else:
#     pass

    

######################Zadatak 5##############################################

# string = input('Unesite string: ')
# novi_string = string[:1] + '*' + string[2:]
# print(novi_string)


######################Zadatak 6##############################################

# s = input('Unesite string: ')
# s = s.lower()
# tacka_zarez = ',.'
# for i in s:
#     if i in tacka_zarez:
#         s = s.replace(i, '')
# print(s)


######################Zadatak 7##############################################

# s = input('Proveriti da li je palindrom: ')
# a = ''
# b = ''

# for i in range(len(s)):
#     if s[i] != ' ':
#         a += s[i]
#         b = s[i] + b   
# if a == b:
#     print('Jeste palindrom.')
# else:
#     print('Nije palindrom.')


######################Zadatak 8##############################################

# f = eval(input('Koliko email adresa unosite: '))

# b = '@prof.college.edu'
# count = 0

# for i in range (f):
#     a = input('Unesite email adresu: ')
#     if b in str(a):
#         count += 1
#     else:
#         pass
# if count == 0:
#     print('Sve adrese su studentske, nije bilo profesorskih adresa.')
# else:
#     print('Osim studentskih adresa uneto je i', count, 'profesorske adrese.')

######################Zadatak 9##############################################

# broj = eval(input('Unesite neki broj: '))
# for i in range (1, broj + 1):
#     print(' ' * i, i)

######################Zadatak 10##############################################

# s = input('Unesite neku rec: ')

# for i in range(len(s)):
#     print(s[i] * 2)

######################### Zadatak 11###########################################



######################### Zadatak 12###########################################

# a = input('Unesite rec: ')
# b = ''
# i = True

# for char in a:
#     if i:
#         b += char.upper()
#     else:
#         b += char.lower()
#     if char != ' ':
#         i = not i

# print(b)




######################### Zadatak 13###########################################




######################### Zadatak 14###########################################
# ime = input('Unesite vase ime i prezime: ')
# print(ime.capitalize())

######################### Zadatak 15###########################################




######################### Zadatak 16###########################################

# hole_name = input('Enter name: ')

# name = hole_name.split()[0]

# print('\n')
# print('\n')
# print('Dear', hole_name, ',', '\n')


# print('I am plesed to offer you our new Platinum Plus Rewardscard \ncard at special introductory APR of 47,99%.'
# ,name, '\nan offer like this does not come alond evey day, so \nI urge you to call now toll-free at 1-800-314-1592. We \ncannot ofer such low rate for long,', name, 'so call\n'
# 'right away.')





######################### Zadatak 17###########################################
