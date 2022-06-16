import random


class Warrior:
    name = "default_name"
    health = 100
    damage = 20

    def attack(self, aim):
        print(f"{self.name} attack!")
        aim.getDamage(self.damage)

    def getDamage(self, damage):
        self.health -= damage
        print(f"{self.health} HP left with {self.name}\n")

        if self.health <= 0:
            print(f"{self.name} lose :(")


saitama = Warrior()
saitama.name = "saitama"

default_warrior = Warrior()
default_warrior.name = "default_warrior"

while saitama.health > 0 and default_warrior.health > 0:
    initiator = random.choice((saitama, default_warrior))
    if initiator is saitama:
        saitama.attack(default_warrior)
    else:
        default_warrior.attack(saitama)

print(f"saitama win!") if default_warrior.health <= 0 else print(
    f"default_warrior win!"
)
