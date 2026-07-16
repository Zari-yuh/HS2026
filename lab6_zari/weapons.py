from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        random_damage = random.randint(self.max_damage // 2, self.max_damage)
        print(random_damage)
        return random_damage