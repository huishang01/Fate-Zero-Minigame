from servants import *
from tools import *
from foreword import *


if __name__ == '__main__':
    while True:
        is_exit = input('╔════════════════════════════════════════════════════╗\n'
                        '║                                                    ║\n'
                        '║                      Fate/Zero                     ║\n'
                        '║                  -按回车开始游戏-                  ║\n'
                        '║                  输入exit退出游戏                  ║\n'
                        '║                                                    ║\n'
                        '╚════════════════════════════════════════════════════╝\n')

        if is_exit.lower() == 'exit':
            break

        choose = foreword()
        if choose is None:
            break
        elif choose == '1':
            saber_()
        elif choose == '2':
            archer_()
        elif choose == '3':
            lancer_()
        elif choose == '4':
            rider_()
        elif choose == '5':
            caster_()
        elif choose == '6':
            assassin_()
        elif choose == '7':
            berserker_()
        input()
