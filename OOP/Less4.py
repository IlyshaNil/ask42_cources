import random


class Unit:
    def __init__(self, team):
        self.id = id(self)
        self.team = team


class Soldier(Unit):
    def __init__(self, team, hero=None):
        Unit.__init__(self, team)
        self.hero = hero

    def follow_the_hero(self, hero):
        self.hero = hero


class Hero(Unit):
    def __init__(self, team, lvl=1):
        Unit.__init__(self, team)
        self.lvl = lvl

    def levelup(self):
        self.lvl += 1


t1_hero = Hero("t1")
t2_hero = Hero("t2")

t1_list = []
t2_list = []

for elm in "1234567890":
    team = random.choice(("t1", "t2"))
    spawned_soldier = Soldier(team)
    if team == "t1":
        t1_list.append(spawned_soldier)
    else:
        t2_list.append(spawned_soldier)


print(f"t1 soldiers amount: {len(t1_list)}\nt2 soldiers amount: {len(t2_list)}")

t1_hero.levelup() if len(t1_list) > len(t2_list) else t2_hero.levelup()

if t1_list[0]:
    t1_list[0].hero = t1_hero

print(t1_hero.id, t1_list[0].id)
