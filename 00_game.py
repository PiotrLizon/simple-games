# ZGADNIJ CO TO ZA KRAJ EUROPEJSKI
'''
Program zadaje 14 pytań dotyczących
krajów Starego Kontynentu.
Sprawdź swoją wiedzę. POWODZENIA!
'''

qa = {
      'Rosja' : 'Największe powierzchniowo państwo w Europie',
      'Watykan' : 'Najmniejsze powierzchniowo państwo w Europie',
      'Polska' : 'Ojczyzna Kopernika',
      'Niemcy' : 'Graniczą z największa ilością krajów w Europie',
      'Holandia' : 'Kraj który słynie z produkcji serów',
      'Francja' : 'Kraj w którym znada się najwięcej na świecie żab',
      'Włochy' : 'Ojczyzna Benito Mussoliniego',
      'Cypr' : 'Położone w całości na teretorium Azji państwo należące do UE',
      'Macedonia Północna' : 'Stolicą tego państwa jest Skopje',
      'Monako' : 'Państwo z największą gęstością zaludnienia',
      'Islandia' : 'Państwo z najmniejszą gęstością zaludnienia',
      'Albania' : 'Stolicą tego państwa jest Tirana',
      'Wielka Brytania' : 'Ojczyzna Williama Shakespearea',
      'Norwegia' : 'Kraj w którym nie ma ani jednego lokalu KFC'
      }


input('''Witaj w grze \'ZGADNIJ CO TO ZA KRAJ EUROPEJSKI\' \n
wciśnij ENTER aby rozpocząć rozgrywkę. POWODZENIA! ''')

points = 0
message = ''

for key in qa:
    answer = key.upper()
    user = (input(qa[key] + '? ')).upper()
    if answer == user:
        points += 1
    if not(points > len(qa) / 2):
        message = 'Musisz jeszcze poćwiczyć...'
    elif points > len(qa) / 2:
        message = 'Świetny wynik!'

input('Udało Ci się odpowiedzieć na ' + str(points)
      + ' pytań! '+ message)

        

