from time import sleep
from vragiihp import *
def trena():
    timepop = 0
    while timepop == 100:
        sleep(1)
        timepop+=10
        print('Вы выполнили трену на ',timepop)
    print(f'Вы выполнили тренировку. Теперь у вас урон',{gamer['attack']+10})
    gamer['attack']+=10
def job():
    print('Ответьте на лёгкие вопросы и получите 100ъ')
    sleep(2)
    asd = 0
    asd == input('Введите ник автора данной программы. Варианты ответа:\n1)Deniskocc 2)Korablik\n3)Denryoker4)DenisGodzilla')
    if asd == 1:
        print('И ЭТО ПРАВИЛЬНЫЙ ОТВЕТ!!!! ВЫ ПОЛУЧИЛИ +100ъ')
        gamer['money']+100
    else:
        print('И это не правильный ответ((((')