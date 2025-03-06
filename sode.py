from vragiihp import *
from random import *
def draka():
    hp = vragi[0]['hp']
    myhp = gamer['hp']
    vragatt = vragi[0]['hp']
    myatt = gamer['attack']
    if hp > myhp and vragatt > myatt:
        print(vragi('win'))
    else:
        print(vragi('loss')) and gamer['money'+1000]
def magazin():
    what = input('Что вы хотите приобрести?\n1)Лотерейный билет - 1K ъ\n2)Щит - 800 ъ\n3)Напарник - 10K ъ')
    if what == 1:
        lotereya = random.randint(0,3000)