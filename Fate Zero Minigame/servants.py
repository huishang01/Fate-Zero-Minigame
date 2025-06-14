from tools import *


class servant:
    name = None
    HP = None
    shield = None
    noble_phantasm = None

    def __str__(self):
        return f'══════════════════════════════════════════════════════\n真名：{self.name}\n生名值：{self.HP}\n宝具：{np_info(self.noble_phantasm)}'

    # def __init__(self):
    #     print(f'\n真名：{self.name}\n生名值：{self.HP}\n宝具：{np_info(self.noble_phantasm)}')


class saber(servant):
    name = '【骑士王亚瑟】阿尔托莉雅·潘德拉贡'
    HP = 600
    shield = 0.6
    noble_phantasm = {'Excalibur 契约胜利之剑': 1, 'Invisible Air 风王结界': 10, 'Avalon 遗世独立的理想乡': 1}

    def excalibur(self, enemy):
        name = 'Excalibur 契约胜利之剑'
        np_effect(self, enemy, name, 500)

    def invisible_air(self, enemy):
        name = 'Invisible Air 风王结界'
        np_effect(self, enemy, name, 100)

    def avalon(self):
        name = 'Avalon 遗世独立的理想乡'
        if self.noble_phantasm[name] > 0:
            self.noble_phantasm[name] -= 1
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
    shield = 0.5
    noble_phantasm = {'Gate of Babylon 王之财宝': 10, 'Enumaelish 天地乖离开辟之星': 1}

    def gate_of_babylon(self, enemy):
        name = 'Gate of Babylon 王之财宝'
        np_effect(self, enemy, name, 100)

    def enumaelish(self, enemy):
        name = 'Enumaelish 天地乖离开辟之星'
        np_effect(self, enemy, name, 500)

    def np_use(self, enemy, name):
        if name == 'Gate of Babylon 王之财宝':
            self.gate_of_babylon(enemy)
        elif name == 'Enumaelish 天地乖离开辟之星':
            self.enumaelish(enemy)


class lancer(servant):
    name = '迪尔姆德·奥迪那'
    HP = 600
    shield = 0.5
    noble_phantasm = {'【1】Gae Dearg 破魔的红蔷薇': 3, '【2】Gae Buidhe 必灭的黄蔷薇': 3}


class rider(servant):
    name = '【征服王】伊斯坎达尔'
    HP = 800
    shield = 0.4
    noble_phantasm = {'【1】Via Expugunatio 遥远的蹂躏制霸': 5, '【2】Ionioi Hetairoi 王之军势': 1}


class caster(servant):
    name = '【蓝胡子】吉尔·德·莱斯'
    HP = 300
    shield = 0.8
    noble_phantasm = {'【1】Prelati\'s Spellbook 螺湮城教本': 10}


class assassin(servant):
    name = '【山中老人】哈桑·萨巴赫'
    HP = 400
    shield = 0.8
    noble_phantasm = {'【1】Zabaniya 妄想幻象': 20}


class berserker(servant):
    name = '兰斯洛特'
    HP = 1000
    shield = 0.4
    noble_phantasm = {'【1】Knight\'s Owner 骑士不死于徒手': 20, '【2】Arondight 无毁的湖光': 1}
