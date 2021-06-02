from random import randint


########################## prvi zadatak #########################

# 1.	Napišite program koji traži od korisnika da unese listu celih brojeva. Program treba da uradi sledeće:
# •	Štampa ukupan broj podataka u listi.
# •	Štampa poslednji podatak u listi.
# •	Štampa listu obrnutim redosledom.
# •	Štampa Da ako lista sadrži 5 na Ne ako ne sadrži.
# •	Štampa broj petica u listi.
# •	Briše prvi i poslednji podatak iz liste, sortira preostale podatke i štampa rezultat.
# •	Štampa koliko celih brojeva u listi je manje od 5.

# lst = []

# lst = [int(item) for item in input("Unesite listu celobrojnih vrednosti, elemente odvojte jednim razmakom : ").split()]

# print('Vasa lista:', lst)
# print('Vasa lista sadrzi', len(lst), 'elemenata.')
# print('Poslednji element liste: ', lst[-1])
# print('Lista unazad', lst[::-1])

# if 5 in lst:
#     print('Vasa lista sadrzi element 5')
# else:
#     print('Vasa lista ne sadrzi element 5')

# brojac = 0

# for i in lst:
#     if i == 5:
#         brojac += 1

# print('U vasoj listi se nalazi', brojac, 'elemenata sa vrednoscu 5')

# del lst[0]
# del lst[-1]
# print(lst)

# brojac_2 = 0
# for i in lst:
#     if i < 5:
#         brojac_2 += 1

# print('U vasoj listi nalazi se', brojac_2, 'elemenata koji su manji od 5')


########################## drugi zadatak #########################

# 2.	Napišite program koji generiše listu od 20 slučajnih brojeva između 1 i 100, pa:
# •	Štampa listu.
# •	Štampa srednju vrednost svih elemenata iz liste.
# •	Štampa najveću i najmanju vrednost iz liste.
# •	Štampa drugu najmanju i drugu najveću vrednost iz liste.
# # •	Štampa koliko ima parnih brojeva u listi.

# L = []
# for i in range(20):
#     L.append(randint(1,101))
# print('Lista slucajnih vrednosti', L)

# sv = sum(L)/len(L)
# print('Srednja vrednost je:', sv)

# L.sort()
# print('Najmanja vrednost:', L[0], 'Najveca vrednost:', L[-1])
# print('Druga najmanja vrednost:', L[1], 'Druga najveca vrednost: ', L[-2])

# brojac_parnih = 0

# for i in range(len(L)):
#     if (L[i]%2 == 0):
#         brojac_parnih += 1
# print('U vasoj listi ima:', brojac_parnih, 'parnih elemenata.')




########################## treci zadatak #########################

# 3.	Počnite sa listom [8,9,10]. Uradite sledeće:
# •	Postavite drugi element (indeks 1) na 17
# •	Dodajte 4, 5, i 6 na kraj liste
# •	Brišite prvi element liste
# •	Sortirajte listu
# •	Duplirajte listu
# •	Ubacite 25 na indeksu 3
# Na kraju treba da dobijete listu [4,5,6,25,10,17,4,5,6,10,17] 




########################## cetvrti zadatak #########################

# 4.	Tražite od korisnika da unese listu koja sadrži brojeve između 1 i 12. Zatim zamenite sve brojeve koji su veći od 10 sa brojem 10.


########################## peti zadatak #########################

# 5.	Tražite od korisnika da unese listu stringova. Kreirajte novu listu koja sadrži iste stringove ali bez prvog slova.


########################## sesti zadatak #########################

# 6.	Kreirajte sledeće liste korišćenjem petlji.
# •	Listu koja se sastoji od brojeva 0 do 49
# •	Listu koja sadrži kvadrate brojeva od 1 do 50.
# •	Listu [‘a’, ‘bb’, ‘ccc’, ‘dddd’, … ] koja se završava sa 26 kopija slova z.

########################## sedmi zadatak #########################

########################## osmi zadatak #########################

########################## deveti zadatak #########################

########################## deseti zadatak #########################

########################## jedanaesti zadatak #########################

########################## dvanaesti zadatak #########################

########################## trinaesti zadatak #########################

########################## cetrnaesti zadatak #########################

########################## petnaesti zadatak #########################