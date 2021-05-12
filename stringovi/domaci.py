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

#Jedan jednostavan način da se proceni broj reči u stringu
#je da se prebroji broj blanko znakova (space) u stringu. 
# Napišite program koji traži od korisnika da unese tekst, 
# a onda mu vraća procenjeni broj reči u tom stringu.

#############################Treci Zadatak##################################

#Ljudi često zaborave da zatvore zagradu u formulama. 
# Napišite program koji traži od korisnika da unese formulu i štampa poruku 
# da li formula ima isti broj levih i desnih zagrada.

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

