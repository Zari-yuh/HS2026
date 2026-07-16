import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armor = []
        self.weapons = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        for weapon in self.weapons:
            total_damage += weapon.attack()
        return total_damage
    
    def add_armor(self, armor):
        self.armor.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armor:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage):
        blocked = self.defend()
        actual_damage = max(damage - blocked, 0)
        self.current_health -= actual_damage
        if self.current_health < 0:
            self.current_health = 0
        return actual_damage

    def battle(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return

        while self.current_health > 0 and opponent.current_health > 0:
            opponent.take_damage(self.attack())
            if opponent.current_health <= 0:
                print(f"{self.name} won!")
                return
            self.take_damage(opponent.attack())
            if self.current_health <= 0:
                print(f"{opponent.name} won!")
                return

if __name__ == "__main__":
    my_hero = Hero("Spider-Man", 150)

my_hero.add_armor(Armor("Spider Suit", 30))
my_hero.add_armor(Armor("Web Shield", 20))
my_hero.take_damage(30)
print(my_hero.current_health)