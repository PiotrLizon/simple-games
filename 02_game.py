# CO TO ZA ZWIERZĘ?
# Komputer wybiera losowo słowo, a następnie miesza w nim litery.
# Gracz musi odgadnąć co to za zwierzę.

import random


animals = ('żółw', 'żyrafa',
           'słoń', 'kot', 'pies',
           'nosorożec', 'lampard',
           'dzik', 'koń', 'struś',
           'wielbłąd', 'gepard',
           'antylopa', 'sarna',
           'krowa', 'świnia', 'kura'
           'kogut', 'sowa', 'papuga')

animal = random.choice(animals)
correct = animal
mixed = ''
attempts = 0

while animal:
    position = random.randrange(len(animal))
    mixed += animal[position]
    animal = animal[:position] + animal[(position + 1):]

print('''Witaj w grze CO TO ZA ZWIERZĘ?
Uporządkuj litery i odtwórz prawidłową nazwę.''')

print('Zgadnij jakie to zwierzę:', mixed)

guess = input('Wprowadź odpowiedź: ')

while guess != correct and guess != '':
    print('Spróbuj ponownie!')
    guess = input('Wprowadź odpowiedź: ')
    attempts += 1
    
if guess == correct:
    print('Gratulacje! Potrzebowałeś tylko', attempts, 'prób!')

print('Dzięki za udział w grze!')



