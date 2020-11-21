import random

from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name

        self.abilities = list()
        self.armors = list()

        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage):
        # defend_amt = 0

        for armor in self.armors:
            damage -= armor.defend()
        return damage

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        # return self.current_health

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive() == True:
                print(f"{self.name} wins!")
            elif opponent.is_alive() == True:
                print(f"{opponent.name} wins!")


if __name__ == "__main__":

    # ability = Ability("Great Debugging", 50)
    # ability2 = Ability("Dicreat Hack", 50)
    # hero = Hero("Afar", 200)
    # shield = Armor("Shield", 50)
    # hero.add_ability(ability)
    # hero.add_ability(ability2)
    # print(hero.attack())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
