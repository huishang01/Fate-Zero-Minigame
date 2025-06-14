import random
import time
import re
from servants import *


def cut():
    print('══════════════════════════════════════════════════════')


def np_info(np):
    np = "\n" + "\n".join([f"【{i+1}】{k}: {v}" for i, (k, v) in enumerate(np.items())])
    return np


def is_dead(servant):
    if servant.HP <= 0:
        cut()
        slow_print(f'{servant.name}已死亡。')
        return True
    else:
        return False


def slow_print(text, line_feed=True, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if line_feed:
        print()


def print_text(text):
    text = re.sub(r'\s', '', text)
    split_result = re.split('([。？！…])', text)
    final_result = [''.join([split_result[i], split_result[i + 1]])
                    for i in range(0, len(split_result) - 1, 2)]
    if len(split_result) % 2 != 0:
        final_result.append(split_result[-1])
    for i in final_result:
        is_exit = input()
        if is_exit.lower() == 'exit':
            return True
        slow_print(i, False)


def np_effect(myself, enemy, name, damage):
    damage = damage * enemy.shield
    if myself.noble_phantasm[name] > 0:
        myself.noble_phantasm[name] -= 1
        enemy.HP -= damage
        cut()
        slow_print(
            f'{myself.name}使用了【{name}】，对{enemy.name}造成了{damage}点伤害。')
        # print(myself)
        return True
    else:
        cut()
        slow_print(f'【{name}】使用次数已用光。')
        return False


def use_np(myself, enemy, choose):
    try:
        name = list(myself.noble_phantasm.keys())[int(choose)-1]
        myself.np_use(enemy, name)
    except Exception:
        cut()
        slow_print('Master，请您做出正确的选择。')


def attack(myself, enemy):
    while (myself.HP >= 0) and (enemy.HP >= 0):
        choose = input(f'{myself}\n\nMaster，请做出您的选择：')

        try:
            use_np(myself, enemy, choose)
        except Exception:
            cut()
            slow_print('Master，请您做出正确的选择。')

        enemy_np = random.choice(list(enemy.noble_phantasm.keys()))
        enemy.np_use(myself, enemy_np)

    if myself.HP <= 0:
        cut()
        slow_print(f'{myself.name}已回归英灵殿。')
        return True
    else:
        cut()
        slow_print(f'{enemy.name}已被击败。')
        return False


