# Fate/Zero Minigame 说明文档

## 项目概述

这是一个基于《Fate/Zero》动漫/小说设定的文字冒险游戏，玩家可以选择不同的英灵阵营进行游戏体验。

## 项目结构

```python
Fate Zero Minigame/
├── .idea/                # IDE配置文件
├── part/                 # 游戏文本资源
│   ├── archer.txt        # 弓兵剧情文本
│   ├── assassin.txt      # 暗杀者剧情文本
│   ├── berserker.txt     # 狂战士剧情文本
│   ├── caster.txt        # 魔术师剧情文本
│   ├── end.txt           # 游戏结束文本
│   ├── foreword.txt      # 开场文本
│   ├── lancer.txt        # 枪兵剧情文本
│   ├── rider.txt         # 骑兵剧情文本
│   └── saber.txt         # 剑兵剧情文本
├── foreword.py           # 游戏前导和角色选择逻辑
├── main.py               # 主程序入口
├── masters.py            # 御主(Master)角色定义
├── servants.py           # 从者(Servant)角色定义
├── test.py               # 测试脚本
└── tools.py              # 工具函数
```

## 游戏功能

### 1.  主菜单

-   显示精美的ASCII艺术标题
-   按回车开始游戏
-   输入"exit"退出游戏

### 2. 阵营选择

-   玩家可以选择以下7个英灵阵营：
    1.   剑兵 Saber
    2.   弓兵 Archer
    3.   枪兵 Lancer
    4.   骑兵 Rider
    5.   魔术师 Caster
    6.   暗杀者 Assassin
    7.   狂战士 Berserker

### 3. 游戏机制

-   战斗系统：回合制战斗，玩家可以选择使用不同的宝具(Noble Phantasm)攻击敌人
-   文本显示：逐字打印效果，增强沉浸感
-   生命值系统：从者和御主都有HP属性
-   宝具系统：每个从者有独特的宝具和有限的使用次数

## 核心代码说明

### 主要函数

`Fate Zero Minigame\main.py`

```python
# 主循环
while True:
    # 显示主菜单
    is_exit = input('╔════════════════════════════════════════════════════╗\n'
                    '║                                                    ║\n'
                    '║                      Fate/Zero                     ║\n'
                    '║                  -按回车开始游戏-                  ║\n'
                    '║                  输入exit退出游戏                  ║\n'
                    '║                                                    ║\n'
                    '╚════════════════════════════════════════════════════╝\n')
    
    if is_exit.lower() == 'exit':
        break
    
    # 处理玩家选择
    choose = foreword()
    if choose == '1':
        saber_()  # 唯一实现的完整剧情
    elif choose in ['2','3','4','5','6','7']:
        # 其他阵营暂未实现
        slow_print('敬请期待，按回车回到主菜单')
```
### 工具函数

`Fate Zero Minigame\tools.py`

```python
# 逐字打印效果
def slow_print(text, line_feed=True, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if line_feed:
        print()

# 战斗系统核心
def attack(myself, enemy):
    while (myself.HP >= 0) and (enemy.HP >= 0):
        print(myself)  # 显示状态
        print(enemy)
        cut()  # 分割线
        
        # 玩家选择宝具
        choose = input(f'Master，请做出您的选择：')
        try:
            use_np(myself, enemy, choose)  # 使用宝具
        except Exception:
            slow_print('Master，请您做出正确的选择。')
        
        # 敌人行动
        enemy_np = random.choice(list(enemy.noble_phantasm.keys()))
        enemy.np_use(myself, enemy_np)
```

## 如何运行

1.   确保已安装 Python 3.x
2.   运行主程序：`main.py`