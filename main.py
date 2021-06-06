def potega(podstawa, wykladnik):
    wynik = podstawa
    for i in range(wykladnik - 1):
        wynik = wynik * podstawa
    return wynik


podstawa = int(input('Podaj podstawe: '))
wykladnik = int(input('Podaj wykladnik: '))

print('Wynik wynosi {}.'.format(potega(podstawa, wykladnik)))
