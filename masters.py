import random

from tools import *

"""
定义 masters 类，包含名称、生命值、护盾/减伤、攻击、使用攻击
通过传入的宝具名来使用对应的宝具
"""


class master:
    name = None
    HP = 100
    shield = 1.0  # 护盾/减伤，1.0 表示原伤害或无护盾，0.7 表示伤害为原伤害的 70%
    noble_phantasm = None

    def __str__(self):
        return f'══════════════════════════════════════════════════════\n名称：{self.name}\n生命值：{self.HP}\n攻击手段：{np_info(self.noble_phantasm)}'


class kiritsugu(master):
    name = '【魔术师杀手】卫宫切嗣'
    noble_phantasm = {'起源弹': 3, '全自动冲锋枪': 10, 'Time Alter 固有时制御': 3}

    def reset(self):
        self.HP = 100
        self.noble_phantasm = {'起源弹': 3, '全自动冲锋枪': 10, 'Time Alter 固有时制御': 3}

    def origins(self, enemy):
        name = '起源弹'
        enemy.shield = 1.0
        np_effect(self, enemy, name, 70)

    def smg(self, enemy):
        name = '全自动冲锋枪'
        np_effect(self, enemy, name, 30)

    # 随机使用 1-3 级的随机技能，根据使用等级减少 HP
    def time_alter(self, enemy):
        name = 'Time Alter 固有时制御'
        count = random.randint(1, 3)
        if count == 1:
            self.HP *= 0.9
        elif count == 2:
            self.HP *= 0.8
        elif count == 3:
            self.HP *= 0.7
        if random.choice([True, False]):
            np_effect(self, enemy, name, 30)
        np_effect(self, enemy, name, 60)
        slow_print(
            f'{self.name}使用了【{name}】，'
            f'闪避了{enemy.name}{count}次攻击；并使用了全自动冲锋枪，'
            f'对其造成了{30 * count}点伤害。'
        )

    def np_use(self, enemy, name):
        if name == '起源弹':
            self.origins(enemy)
        elif name == 'Time Alter 固有时制御':
            self.time_alter(enemy)
        elif name == '全自动冲锋枪':
            self.smg(enemy)


class tokiomi(master):
    name = '远坂时臣'
    noble_phantasm = {'宝石魔术': 10, '大型宝石魔术': 3}

    def reset(self):
        self.HP = 100
        self.noble_phantasm = {'宝石魔术': 10, '大型宝石魔术': 3}

    def gem_magic(self, enemy):
        name = '宝石魔术'
        np_effect(self, enemy, name, 30)

    def large_gem_magic(self, enemy):
        name = '大型宝石魔术'
        np_effect(self, enemy, name, 60)

    def np_use(self, enemy, name):
        if name == '宝石魔术':
            self.gem_magic(enemy)
        elif name == '大型宝石魔术':
            self.large_gem_magic(enemy)


class kirei(master):
    name = '言峰绮礼'
    noble_phantasm = {'黑键': 10, '八极拳': 3, '法衣': 3}

    def reset(self):
        self.HP = 100
        self.noble_phantasm = {'黑键': 10, '八极拳': 3, '法衣': 3}

    def black_key(self, enemy):
        name = '黑键'
        np_effect(self, enemy, name, 30)

    def eight_pole(self, enemy):
        name = '八极拳'
        np_effect(self, enemy, name, 60)

    def cloak(self, enemy):
        name = '法衣'
        slow_print(
            f'{self.name}使用了【{name}】，防御了{enemy.name}的攻击。')

    def np_use(self, enemy, name):
        if name == '黑键':
            self.black_key(enemy)
        elif name == '八极拳':
            self.eight_pole(enemy)
        elif name == '法衣':
            self.cloak(enemy)


class kenneth(master):
    name = '肯尼斯·艾尔梅洛伊·阿其波卢德'
    noble_phantasm = {'月灵髓液 攻击': 10, '属性魔术': 3, '月灵髓液 防御': 3}

    def reset(self):
        self.HP = 100
        self.noble_phantasm = {'月灵髓液 攻击': 10, '属性魔术': 3, '月灵髓液 防御': 3}

    def moon_attack(self, enemy):
        name = '月灵髓液 攻击'
        np_effect(self, enemy, name, 30)

    def attribute_magic(self, enemy):
        name = '属性魔术'
        np_effect(self, enemy, name, 20)

    def moon_defense(self, enemy):
        name = '月灵髓液 防御'
        if random.random() < 0.5:
            slow_print(
                f'{self.name}使用了【{name}】，防御了{enemy.name}的攻击。')
        else:
            self.HP = 0
            slow_print(f'{self.name}使用了【{name}】，未能防御{enemy.name}的攻击。')

    def np_use(self, enemy, name, enemy_np=None):
        if name == '月灵髓液 攻击':
            self.moon_attack(enemy)
        elif name == '属性魔术':
            self.attribute_magic(enemy)
        elif name == '月灵髓液 防御':
            self.moon_defense(enemy, enemy_np)


class waver(master):
    name = '韦伯·维尔维特'
    noble_phantasm = {'普通攻击': 5}

    def reset(self):
        self.HP = 100
        self.noble_phantasm = {'普通攻击': 5}

    def basic_magic(self, enemy):
        name = '普通攻击'
        np_effect(self, enemy, name, 5)

    def np_use(self, enemy, name):
        if name == '普通攻击':
            self.basic_magic(enemy)


class kariya(waver):
    name = '间桐雁夜'


class ryunosuke(waver):
    name = '雨生龙之介'


