koszyk_items = ['telewizor', 'radio', 'lodowka', 'glosniki']
koszyk_ilosc = [1, 2, 3, 5]
koszyk_cena = [1000, 400, 1200, 500]

sum = 0
for idx in range(len(koszyk_items)):
    item = koszyk_items[idx]
    ile = koszyk_ilosc[idx]
    cena = koszyk_cena[idx]
    print("{0} {1} {2} {3}".format(item, ile, cena))
    suma = suma + sum #do poprawy i skonczenia 
