from tools import *

"""
定义 servant 类，包含姓名、生命值、护盾/减伤、宝具、使用宝具
通过传入的宝具名来使用对应的宝具
"""


class servant:
    name = None
    HP = None
    shield = None  # 护盾/减伤，1.0 表示原伤害或无护盾，0.7 表示伤害为原伤害的 70%
    noble_phantasm = None

    def __str__(self):
        return f'══════════════════════════════════════════════════════\n真名：{self.name}\n生命值：{self.HP}\n宝具：{np_info(self.noble_phantasm)}'


class saber(servant):
    name = '【骑士王亚瑟】阿尔托莉雅·潘德拉贡'
    HP = 600
    shield = 0.8
    noble_phantasm = {'Excalibur 契约胜利之剑': 1, 'Invisible Air 风王结界': 5, 'Avalon 遗世独立的理想乡': 0}

    def reset(self):
        self.HP = 600
        self.noble_phantasm = {'Excalibur 契约胜利之剑': 1, 'Invisible Air 风王结界': 5, 'Avalon 遗世独立的理想乡': 0}

    def excalibur(self, enemy):
        name = 'Excalibur 契约胜利之剑'
        np_effect(self, enemy, name, 600)

    def invisible_air(self, enemy):
        name = 'Invisible Air 风王结界'
        np_effect(self, enemy, name, 200)

    # 恢复生命值至上限
    def avalon(self):
        name = 'Avalon 遗世独立的理想乡'
        if self.noble_phantasm[name] > 0:
            self.noble_phantasm[name] -= 1
            self.HP = 600
            cut()
            slow_print(
                f'{self.name}使用了【{name}】，生命值恢复至上限。')
            print(self)
            return True
        else:
            cut()
            slow_print(f'【{name}】使用次数已用光。')
            return False

    def np_use(self, enemy, name):
        if name == 'Excalibur 契约胜利之剑':
            self.excalibur(enemy)
        elif name == 'Invisible Air 风王结界':
            self.invisible_air(enemy)
        elif name == 'Avalon 遗世独立的理想乡':
            self.avalon()


class archer(servant):
    name = '【英雄王】吉尔伽美什'
    HP = 400
    shield = 0.7
    noble_phantasm = {'Gate of Babylon 王之财宝': 10, 'Enumaelish 天地乖离开辟之星': 1}

    def reset(self):
        self.HP = 400
        self.noble_phantasm = {'Gate of Babylon 王之财宝': 10, 'Enumaelish 天地乖离开辟之星': 1}

    def gate_of_babylon(self, enemy):
        name = 'Gate of Babylon 王之财宝'
        np_effect(self, enemy, name, 200)

    def enumaelish(self, enemy):
        name = 'Enumaelish 天地乖离开辟之星'
        np_effect(self, enemy, name, 600)

    def np_use(self, enemy, name):
        if name == 'Gate of Babylon 王之财宝':
            self.gate_of_babylon(enemy)
        elif name == 'Enumaelish 天地乖离开辟之星':
            self.enumaelish(enemy)


class lancer(servant):
    name = '迪尔姆德·奥迪那'
    HP = 600
    shield = 0.7
    noble_phantasm = {'Gae Dearg 破魔的红蔷薇': 3, 'Gae Buidhe 必灭的黄蔷薇': 3}

    def reset(self):
        self.HP = 600
        self.noble_phantasm = {'Gae Dearg 破魔的红蔷薇': 3, 'Gae Buidhe 必灭的黄蔷薇': 3}

    # 无视护盾，对敌方直接造成200点伤害
    def gae_dearg(self, enemy):
        name = 'Gae Dearg 破魔的红蔷薇'
        enemy.shield = 1
        np_effect(self, enemy, name, 200)

    # 减少敌方的生命值至其生命值的70%
    def gae_buidhe(self, enemy):
        name = 'Gae Buidhe 必灭的黄蔷薇'
        enemy.HP *= 0.7
        np_effect(self, enemy, name, 200)

    def np_use(self, enemy, name):
        if name == 'Gae Dearg 破魔的红蔷薇':
            self.gae_dearg(enemy)
        elif name == 'Gae Buidhe 必灭的黄蔷薇':
            self.gae_buidhe(enemy)


class rider(servant):
    name = '【征服王】伊斯坎达尔'
    HP = 800
    shield = 0.6
    noble_phantasm = {'Via Expugunatio 遥远的蹂躏制霸': 5, 'Ionioi Hetairoi 王之军势': 1}

    def reset(self):
        self.HP = 800
        self.noble_phantasm = {'Via Expugunatio 遥远的蹂躏制霸': 5, 'Ionioi Hetairoi 王之军势': 1}

    def via_expugunatio(self, enemy):
        name = 'Via Expugunatio 遥远的蹂躏制霸'
        np_effect(self, enemy, name, 200)

    def ionioi_hetairoi(self, enemy):
        name = 'Ionioi Hetairoi 王之军势'
        np_effect(self, enemy, name, 600)

    def np_use(self, enemy, name):
        if name == 'Via Expugunatio 遥远的蹂躏制霸':
            self.via_expugunatio(enemy)
        elif name == 'Ionioi Hetairoi 王之军势':
            self.ionioi_hetairoi(enemy)


class caster(servant):
    name = '【蓝胡子】吉尔·德·莱斯'
    HP = 300
    shield = 0.9
    noble_phantasm = {'Prelati\'s Spellbook 螺湮城教本': 7}

    def reset(self):
        self.HP = 300
        self.noble_phantasm = {'Prelati\'s Spellbook 螺湮城教本': 7}

    # 随机宝具使用次数：1-3次
    def prelati_spellbook(self, enemy):
        name = 'Prelati\'s Spellbook 螺湮城教本'
        damage = 100 * random.randint(1, 3)
        np_effect(self, enemy, name, 100)

    def np_use(self, enemy, name):
        if name == 'Prelati\'s Spellbook 螺湮城教本':
            self.prelati_spellbook(enemy)


class assassin(servant):
    name = '【山中老人】哈桑·萨巴赫'
    HP = 400
    shield = 0.9
    noble_phantasm = {'Zabaniya 妄想幻象': 7}

    def reset(self):
        self.HP = 400
        self.noble_phantasm = {'Zabaniya 妄想幻象': 7}

    def zabaniya(self, enemy):
        name = 'Zabaniya 妄想幻象'
        damage = 100 * random.randint(1, 3)
        np_effect(self, enemy, name, 100)

    def np_use(self, enemy, name):
        if name == 'Zabaniya 妄想幻象':
            self.zabaniya(enemy)


class berserker(servant):
    name = '兰斯洛特'
    HP = 1000
    shield = 0.6
    noble_phantasm = {'Knight\'s Owner 骑士不死于徒手': 5, 'Arondight 无毁的湖光': 1}

    def reset(self):
        self.HP = 1000
        self.noble_phantasm = {'Knight\'s Owner 骑士不死于徒手': 5, 'Arondight 无毁的湖光': 1}

    def knights_owner(self, enemy):
        name = 'Knight\'s Owner 骑士不死于徒手'
        np_effect(self, enemy, name, 200)

    def arondight(self, enemy):
        name = 'Arondight 无毁的湖光'
        np_effect(self, enemy, name, 600)

    def np_use(self, enemy, name):
        if name == 'Knight\'s Owner 骑士不死于徒手':
            self.knights_owner(enemy)
        elif name == 'Arondight 无毁的湖光':
            self.arondight(enemy)
