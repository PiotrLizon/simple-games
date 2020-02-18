# ZGADNIJ JAKA TO LICZBA
# Komputer wybiera losowo liczbę od 1 do 100.
# Gracz próbuje odgadnąć liczbę.
# Komputer informuje gracza czy podaba liczba jest:
# - za duża
# - za mała
# - prawidłowa

import random

print('\tWitaj w grze "ZGADNIJ JAKA TO LICZBA"')
print('\nWylosowałem liczbę z zakresu od 1 do 100.')
print('Spróbuj ją odgadnąć w jak najmniejszej liczbie prób!')

number = random.randint(1, 100)
guess = int(input('Wydaje mi się, że ta liczba to: '))
attempt = 1

while guess != number:
    if guess > number:
        print('Podaba liczba jest ZA DUŻA.')
    elif guess < number:
        print('Podana liczba jest ZA MAŁA.')

    guess = int(input('Wydaje mi się, że ta liczba to: '))
    attempt += 1

print('GRATULACJE! Ta liczba to:', number)
print('Potrzebowałeś tylko:', attempt, 'prób!')
input('\nWciśnij ENTER aby zakończyć')
















