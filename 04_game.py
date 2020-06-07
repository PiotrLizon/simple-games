# GRA

import random

def square_field(a):
    return a ** 2

def rectangle_field(a, b):
    return a * b

def triangle_field(a, h):
    return (a * h) / 2

while (True):
    figures = {
                'KWADRAT' : 'P = a ** 2',
                'PROSTOKĄT' : 'P = a * b',
                'TRÓJKĄT' : 'P = (a * h) / 2'
            }
    print('POLA FIGUR PŁASKICH')
    choice = int(input('''
Wybierz formę nauki:
1 - Teoria
2 - Quiz
3 - Zadania
4 - Zakończ
'''))
    
    if choice == 1:
        choice = int(input('''
TEORIA
Wybierz figurę:
1 - Kwadrat
2 - Prostokąt
3 - Trójkąt
4 - Wróć do menu
'''))
        while (True):
            if choice == 1:
                print('''
-------------------------------------------------------------------
Kwadrat - wielokąt foremny o czterech równej wielkości bokach.
Wzór na pole: P = a ** 2
a - długość boku
-------------------------------------------------------------------
''')
                break
            elif choice == 2:
                print('''
-------------------------------------------------------------------
Prostokąt -  czworokąt, który ma wszystkie wewnętrzne kąty proste.
Boki przeciwległe są tej samej długości.
Wzór na pole: P = a * b
a - długość boku
b - długość boku
-------------------------------------------------------------------
''')
                break
            elif choice == 3:
                print('''
-------------------------------------------------------------------
Trójkąt - wielokąt o trzech bokach.
Wzór na pole: P = (a * h) / 2
a - podstawa trójkąta
h = wysokość opuszczona na podstawę
-------------------------------------------------------------------
''')
                break
            elif choice == 4:
                break
    elif choice == 2:
        points = 0
        for key in figures:
            print('Podaj wzór na pole:', key)
            answer = input('Wzór: ')
            if answer == figures[key]:
                points += 1
        print('Twój wynik to:', points, 'punkty.')
        if points == 3:
            print('''
GRATULACJE. UMIESZ JUŻ WZORY NA POLE KWADRATU, PROSTOKĄTA I TRÓJKĄTA.
''')
        else:
            print('''
Niestety musisz jeszcze poćwiczyć.
Zapoznaj się z TEORIĄ.
''')
    elif choice == 3:
        points = 0
        a = random.randint(1, 10)
        b = random.randint(11, 20)
        h = random.randint(1,10)
        for figure in figures:
            print('Oblicz pole:', figure)
            if figure == 'KWADRAT':
                print('o boku a =', a)
                answer = int(input('Pole wynosi: '))
                correct_answer = square_field(a)
                print(correct_answer)
                if answer == correct_answer:
                    points += 1
            elif figure == 'PROSTOKĄT':
                print('o boku a =', a, 'i boku b = ', b)
                answer = int(input('Pole wynosi: '))
                correct_answer = rectangle_field(a, b)
                print(correct_answer)
                if answer == correct_answer:
                    points += 1
            elif figure == 'TRÓJKĄT':
                print('o boku a =', a, 'i boku h = ', h)
                answer = float(input('Pole wynosi: '))
                correct_answer = triangle_field(a, h)
                print(correct_answer)
                if answer == correct_answer:
                    points += 1
        print('Twój wynik to:', points, 'punkty.')
        if points == 3:
            print('Umiesz już obliczać pola. GRATULACJE!')
        else:
            print('Musisz jeszcze poćwiczyć.')
    elif choice == 4:
        break
