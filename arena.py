from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = Team("Team 1")
        self.team_two = Team("Team 2")

    def create_ability(self):
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the weapons name?  ")
        max_damage = input("What is the max damage of the weapon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What is the armors name?  ")
        max_block = input("What is the max health of the armor?  ")

        return Weapon(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
            #TODO add an ability to the hero
            #HINT: First create the ability, then add it to the hero
            elif add_item == "2":
            #TODO add a weapon to the hero
            #HINT: First create the weapon, then add it to the hero
            elif add_item == "3":
                #TODO add an armor to the hero
                #HINT: First create the armor, then add it to the hero
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

