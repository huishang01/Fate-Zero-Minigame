from tools import *
from servants import *


def foreword():
    with open('part/foreword.txt', 'r', encoding='utf-8') as f:
        if print_text(f.read()):
            return None

    while True:
        cut()
        choose = input(
            '【1】剑兵 Saber\n'
            '【2】弓兵 Archer\n'
            '【3】枪兵 Lancer\n'
            '【4】骑兵 Rider\n'
            '【5】魔术师 Caster\n'
            '【6】暗杀者 Assassin\n'
            '【7】狂战士 Berserker\n'
            '\nMaster，请选择您的阵营：'
        )

        if choose in ['1', '2', '3', '4', '5', '6', '7']:
            return choose
        cut()
        slow_print('Master，请您做出正确的选择。',)


def saber_():
    attack(saber(), archer())


def archer_():
    cut()
    slow_print('敬请期待，按回车回到主菜单')


def lancer_():
    cut()
    slow_print('敬请期待，按回车回到主菜单')


def rider_():
    cut()
    slow_print('敬请期待，按回车回到主菜单')


def caster_():
    cut()
    slow_print('敬请期待，按回车回到主菜单')


def assassin_():
    cut()
    slow_print('敬请期待，按回车回到主菜单')


def berserker_():
    cut()
    slow_print('敬请期待，按回车回到主菜单')
