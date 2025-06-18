import random
import time
import re

"""
工具类
"""


# 分割线
def cut():
    string = '══════════════════════════════════════════════════════'
    print(string)


# 遍历宝具字典，并格式化输出：在每个键值对前面加上序号
def np_info(np):
    np = "\n" + "\n".join([f"【{i + 1}】{k}: {v}" for i, (k, v) in enumerate(np.items())])
    return np


# 缓慢输出，当 line_feed 为 True 时，会在输出完文本后换行
def slow_print(text, line_feed=True, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if line_feed:
        print()


# 从初始文本中提取文本并格式化输出：分割成多个句子，并按一下回车输出一个句子
# 如果想强制换行，就可以用 | 符号
def print_text(text):
    cut()
    text = re.sub(r'\s', '', text)
    # 修正正则表达式，正确转义管道符号
    split_result = re.split(r'([。？！]”*|\|)', text)
    final_result = []
    for i in range(0, len(split_result) - 1, 2):
        segment = split_result[i] + (split_result[i + 1] if split_result[i + 1] != '|' else '')
        final_result.append(segment)
    if len(split_result) % 2 != 0:
        final_result.append(split_result[-1])
    for i in final_result:
        slow_print(i, False)
        is_exit = input()
        if is_exit.lower() == 'exit':  # 在输出文本时，输入可 exit 退出游戏
            return True


# 宝具的攻击效果：当宝具只有减 HP 的效果时，直接调用这个函数
def np_effect(myself, enemy, name, damage):
    damage = int(damage * enemy.shield)
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


# 通过选择的序号来获取当前宝具并使用
def use_np(myself, enemy, choose):
    try:
        name = list(myself.noble_phantasm.keys())[int(choose) - 1]
        myself.np_use(enemy, name)
    except Exception:
        cut()
        slow_print('Master，请您做出正确的选择。')


# 战斗系统：我方是自己选则宝具，敌方是随机选择宝具
def attack(myself, enemy):
    while (myself.HP >= 0) and (enemy.HP >= 0):
        print(myself)
        print(enemy)
        cut()
        choose = input(f'Master，请做出您的选择：')

        try:
            use_np(myself, enemy, choose)
        except Exception:
            cut()
            slow_print('Master，请您做出正确的选择。')

        if enemy.HP <= 0:
            cut()
            slow_print(f'{enemy.name}已被击败。')
            break

        enemy_np = random.choice(list(enemy.noble_phantasm.keys()))
        enemy.np_use(myself, enemy_np)

        # 当我方生命值耗尽时，则输出 END 文本
        if myself.HP <= 0:
            cut()
            slow_print(f'{myself.name}已被击败。')
            with open('part/end.txt', 'r', encoding='utf-8') as f:
                if print_text(f.read()):
                    return None
            break

