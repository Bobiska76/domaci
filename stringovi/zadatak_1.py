n = input("Ucitaj string ")
 
for i in range (len(n)):        # broj ponavljanja reda
    for j in range (len(n)):    # broj ponavljanja u redu
        print (n, end=' ')      # ispis string, razmak, ostani u istom redu 
    print()                     # novi red



    razmak = ' '                     # razmak
for i in range (1, len(n)+1):    # ponavljaj koliko ima slova
        print (i*(n+razmak))     # ispis i * string i razmak 



c = len(n)*'-'                   # maska od - 
for i in range (1,len(n)+1):     # ponavljaj koliko ima slova
    print ((len(n)-i) * (c+razmak), i*(n+razmak),sep='')   # ispis maska pa string

# novo zbog gita

