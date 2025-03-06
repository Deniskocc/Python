from vragiihp import *
from sode import *
from time import *
from nytime import *
name = input('Введите своё имя : ')
while True:
    dey = int(input('Выберите что хотите сделать - \n1)Пойти воевать\n2)Тренировка\n3)Магазин\n4)Идти работать(не работает тех.работы)\n5)Статистика (В разработке)'))
    if dey == 1:
        pers = input('Выберите врага - \nКрокодил       Hp - 10 Attack - 10\nВ разработке\n')
        if pers == 'Крокодил':
            print(vragi[0]['script'])
            draka()
    if dey == 2:
        trenbolon = int(input('Что вы хотите тренировать : \n1)Атака\n2)В разработке (Тренировка стоит 100ъ)'))
        if trenbolon == 1:
            if gamer['money'] < 100:
                print('У вас не достаточно денег для тренировки\nP.S. Идите работать или победите любого врага')
            trena()
    if dey == 3:
        magazin()
    if dey == 5:
        stat()