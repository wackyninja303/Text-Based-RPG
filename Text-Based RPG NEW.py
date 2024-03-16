import random
import os
import sys
import time

#--------------------------------------------------------------------------------------------------------------
# Ansi Shit

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[96m"
COLOR_BLACK = "\033[30m"
COLOR_WHITE = "\033[97m"
COLOR_GRAY = "\033[90m"

COLOR_ORANGE = "\033[38;5;208m"

COLOR_WARM_YELLOW = "\033[38;5;214m"
COLOR_DARK_CYAN = "\033[38;5;30m"
COLOR_YELLOW_GREEN = "\033[93;5;32m"

COLOR_RESET = "\033[0m"


HEALTH_SYMBOL = "\u2588"
MANA_SYMBOL = "\u25A0"
STAMINA_SYMBOL = "\u25CF"
XP_SYMBOL = "\u25CF"
os.system("color")

#--------------------------------------------------------------------------------------------------------------
# setup classes

archetypes = {
    "1": {"name":"Archer", "meDamage":80, "rDamage":120, "maDamage":0,  "health":0, "mana":0, "dodge":10, "2turnChance":0, "critC":0, "critD":0},
    "2": {"name":"Warrior", "meDamage":120, "rDamage":0, "maDamage":0,  "health":80, "mana":0, "dodge":0, "2turnChance":0, "critC":80, "critD":120},
    "3": {"name":"Assassin", "meDamage":80, "rDamage":80, "maDamage":80,  "health":0, "mana":0, "dodge":25, "2turnChance":10, "critC":150, "critD":0},
    "4": {"name":"Mage", "meDamage":0, "rDamage":0, "maDamage":180,  "health":0, "mana":150, "dodge":0, "2turnChance":0, "critC":0, "critD":0},
    "5": {"name":"Knight", "meDamage":80, "rDamage":0, "maDamage":0,  "health":120, "mana":0, "dodge":0, "2turnChance":0, "critC":0, "critD":0}
}

types = {
    "1": {"name":"Goblin", "damage":5, "health":50, "critC":5, "critD":150, "speed":100, "xp":10, "gold":5, "boss":False},
    "2": {"name":"Ghost", "damage":5, "health":50, "critC":5, "critD":150, "speed":100, "xp":10, "gold":5, "boss":False},
    "3": {"name":"Werewolf", "damage":5, "health":50, "critC":5, "critD":150, "speed":100, "xp":10, "gold":5, "boss":False},
    "4": {"name":"Goblin King", "damage":15, "health":150, "critC":50, "critD":200, "speed":150, "xp":100, "gold":50, "boss":True},
}

# set up weapons

swords = {
    "1": {"name":"Wooden Sword", "desc":"Made from a stick!", "dmg":"1", "type":"weapon"},
    "2": {"name":"Rusted Sword", "desc":"A well used sword.", "dmg":"2", "type":"weapon"},
    "3": {"name":"", "desc":"", "dmg":"", "type":"weapon"},
    "4": {"name":"", "desc":"", "dmg":"", "type":"weapon"},
    "5": {"name":"", "desc":"", "dmg":"", "type":"weapon"},
}

bows = {}

armour = {
    "1": {"name":"Tattered Clothes", "desc":"A set of ripped clothes.", "hp":"5", "type":"armour"},
    "2": {"name":"", "desc":"", "hp":"", "type":"armour"},
    "3": {"name":"", "desc":"", "hp":"", "type":"armour"},
    "4": {"name":"", "desc":"", "hp":"", "type":"armour"},
    "5": {"name":"", "desc":"", "hp":"", "type":"armour"},
}

magic = {}

other = {}

# attack types

attacks = {
    "1": {"name":"Basic", "extraDamage":"0", "cooldown":"0"},
    "2": {"name":"Strong", "extraDamage":"50", "cooldown":"2"}
}
#"": {"name":"", "extraDamage":"", "cooldown":""}

#locations

locations = {
    "1": {"name":"Fairhaven", "minLevel":"0"},
    "2": {"name":"Ravenwood", "minLevel":"5"},
    "3": {"name":"Stoneroot", "minLevel":"10"},
    "4": {"name":"Duneshire", "minLevel":"15"},
}
#"": {"name":"", "minLevel":""},

villages = {
    "1": {"name":"Windmere", "location":"Fairhaven"},
    "2": {"name":"Raven's Perch", "location":"Ravenwood"},
    "3": {"name":"Bedrock Hollow", "location":"Stoneroot"},
    "4": {"name":"Shire's Edge", "location":"Duneshire"},
}
#"": {"name":"", "location":""},

#--------------------------------------------------------------------------------------------------------------
# Classes

class Player:
    def __init__(self, name):
        # name and class
        self.name = name
        self.player_class = {}
        
        # damage and combat
        self.melee_damage = 5
        self.ranged_damage = 5
        self.magic_damage = 5

        self.crit_chance = 10
        self.crit_damage = 150

        self.dodge_chance = 0
        self.turn2Chance = 0
        self.speed = 100

        self.health = 100
        self.max_health = 100

        self.stamina = 50
        self.max_stamina = 50
        
        self.mana = 50
        self.max_mana = 50

        # misc stats
        self.level = 1
        self.levelXp = 50
        self.xp = 0
        self.gold = 0
        self.scrap = 0
        self.location = "Fairhaven"
        
        # dictionary stuff
        self.inventory = {}

        for i in range(30):
            self.inventory[str(i+1)] = ""

        self.equipped_weapon = {}

#-----------------------------------------------------------------------------------------------------------

    # choose the player's class
    def choose_class(self):
        chosen = False
        archetype = "0"
        while not chosen:
            try:
                self.player_class = archetypes[archetype]
                chosen = True
            except:
                os.system("cls")
                print(f"{COLOR_CYAN}What class do you want to play?{COLOR_RESET}")
                print(f"{COLOR_MAGENTA}1. {COLOR_YELLOW}Archer{COLOR_MAGENTA}   (Higher Ranged Damage, Lower Melee Damage)\n2. {COLOR_YELLOW}Warrior{COLOR_MAGENTA}  (Higher Damage, Lower Health)\n3. {COLOR_YELLOW}Assassin{COLOR_MAGENTA} (Lower Damage, Higher Speed)\n4. {COLOR_YELLOW}Mage{COLOR_MAGENTA}     (Higher Mana and Magic Damage)\n5. {COLOR_YELLOW}Knight{COLOR_MAGENTA}   (Higher Health, Lower Damage){COLOR_RESET}")
                if archetype != "0":
                    print(f"{COLOR_RED}Please input a valid option!{COLOR_RESET}")
                archetype = input(f"{COLOR_GREEN}> {COLOR_RESET}")


        if self.player_class['health'] != 0:
            self.max_health = round(self.max_health * (int(self.player_class['health'])/100))
        
        self.health = self.max_health

        if self.player_class['meDamage'] != 0:
            self.melee_damage = round(self.melee_damage * (self.player_class['meDamage']/100))

        if self.player_class['rDamage'] != 0:
            self.ranged_damage = round(self.ranged_damage * (self.player_class['rDamage']/100))

        
        if self.player_class['maDamage'] != 0:
            self.magic_damage = round(self.magic_damage * (self.player_class['maDamage']/100))

        print(f"{COLOR_CYAN}You have chosen the {COLOR_YELLOW}{self.player_class['name']}{COLOR_CYAN} class!{COLOR_RESET}")

#-----------------------------------------------------------------------------------------------------------

    def levelUp(self):
        if self.player_class['health'] != 0:
            self.max_health += round(10 * (self.player_class['health']/100))
        else:
            self.max_health += 10
        
        self.health = self.max_health


        if self.player_class['meDamage'] != 0:
            self.melee_damage += round(5 * (self.player_class['meDamage']/100))
        else:
            self.melee_damage += 5


        if self.player_class['rDamage'] != 0:
            self.ranged_damage += round(5 * (int(self.player_class['rDamage'])/100))
        else:
            self.ranged_damage += 5

        
        if self.player_class['maDamage'] != 0:
            self.magic_damage += round(5 * (int(self.player_class['maDamage'])/100))
        else:
            self.magic_damage += 5
        
        self.level += 1
        self.levelxp += 50 * (1.1**self.level)

#--------------------------------------------------------------------------------------------------------------
        
    #combat!!!
    def attack(self, enemy):
        print("ATTACK!")
#--------------------------------------------------------------------------------------------------------------

class Enemy:
    def __init__(self, type):
        #random.choice(types['boss'] == True)
        self.name = type['name']
        self.max_health = type['health']
        self.damage = type['damage']
        self.health = self.max_health
        self.crit_chance = type['critC']
        self.crit_damage = type['critD']
        self.speed = type['speed']
        self.xp = type['xp']
        self.gold = type['gold']
        
#--------------------------------------------------------------------------------------------------------------

# other functions
def getVillage(player):
    for village in villages:
        place = villages[village]
        if place["location"] == player.location:
            return place["name"]

#printing things

def printStats(player):
    statsPrint = f"{COLOR_MAGENTA}{player.name}'s Stats: \nHealth: {COLOR_GREEN}{COLOR_ORANGE if player.health < (player.max_health/2) else ''}{COLOR_RED if player.health < (player.max_health/4) else ''}{player.health}/{player.max_health} {HEALTH_SYMBOL*round((player.health/player.max_health)*10)}{COLOR_GRAY}{HEALTH_SYMBOL*(10 - (round((player.health/player.max_health)*10)))} \n{COLOR_MAGENTA}Stamina:  {COLOR_WARM_YELLOW}{COLOR_ORANGE if player.stamina < (player.max_stamina/2) else ''}{COLOR_RED if player.stamina < (player.max_stamina/4) else ''}{player.stamina}/{player.max_stamina} {STAMINA_SYMBOL*round((player.stamina/player.max_stamina)*10)}{COLOR_GRAY}{STAMINA_SYMBOL*(10 - (round((player.stamina/player.max_stamina)*10)))} \n{COLOR_MAGENTA}Mana:     {COLOR_CYAN}{COLOR_ORANGE if player.mana < (player.max_mana/2) else ''}{COLOR_RED if player.mana < (player.max_mana/4) else ''}{player.mana}/{player.max_mana} {MANA_SYMBOL*round((player.mana/player.max_mana)*10)}{COLOR_GRAY}{MANA_SYMBOL*(10 - (round((player.mana/player.max_mana)*10)))} \n{COLOR_MAGENTA}Level: {COLOR_YELLOW_GREEN}{player.level}:  {COLOR_YELLOW_GREEN}{player.xp}/{player.levelXp} {XP_SYMBOL*round((player.xp/player.levelXp)*10)}{COLOR_GRAY}{XP_SYMBOL*(10 - (round((player.xp/player.levelXp)*10)))} \n{COLOR_MAGENTA}Gold:  {COLOR_YELLOW}{player.gold} \n{COLOR_MAGENTA}Scrap: {COLOR_GRAY}{player.scrap}"
    #{COLOR_ORANGE if player.stat < (player.max_stat/2) else COLOR_RED if player.stat < (player.max_stat/4) else ''}
    print(statsPrint)

def printOptions(player):
    print(f"{COLOR_GRAY}1. {COLOR_YELLOW}Fight \n{COLOR_GRAY}2. {COLOR_YELLOW}Explore \n{COLOR_GRAY}3. {COLOR_YELLOW}Go to {getVillage(player)} \n{COLOR_GRAY}4. {COLOR_YELLOW}Inventory")

def printInventory(player):
    print(player.inventory)
    for slot in player.inventory:
        item = player.inventory[slot]


#--------------------------------------------------------------------------------------------------------------

#shop buying and selling
def generalBuy():
    print(f"{COLOR_MAGENTA}What would you like to buy?")
    print(f"{COLOR_GRAY}1. {COLOR_YELLOW}Potion Of Healing \n{COLOR_GRAY}2. {COLOR_YELLOW}Potion Of Rage")

def generalSell():
    print(f"sold")
    

#--------------------------------------------------------------------------------------------------------------

# shops
def general(player):
    os.system('cls')
    print(f"{COLOR_MAGENTA}You went to the {COLOR_YELLOW}General Store{COLOR_MAGENTA}!")
    print(f"{COLOR_GRAY}1. {COLOR_YELLOW}Buy \n{COLOR_GRAY}2. {COLOR_YELLOW}Sell")
    input(f"{COLOR_GREEN}> {COLOR_RESET}")
    goToVillage(player)

def armoursmith(player):
    os.system('cls')
    print("armoursmith")
    input()
    goToVillage(player)

def weaponsmith(player):
    os.system('cls')
    print("weaponsmith")
    input()
    goToVillage(player)

def jewelery(player):
    os.system('cls')
    print("jewelery")
    input()
    goToVillage(player)

def accessory(player):
    os.system('cls')
    print("accessory")
    input()
    goToVillage(player)

#--------------------------------------------------------------------------------------------------------------

# main options
def fight(player):
    os.system('cls')
    print("fight")
    input()

def explore(player):
    travelled = False
    travelTo = "0"
    travelLocations = {}
    while not travelled:
        try:
            travel = travelLocations[travelTo]
            if int(travelTo) < travelLocations[-1]:
                if player.level >= location[travelTo]['minLevel']:
                    player.location = travel
                    travelled = True
        except:
            os.system('cls')
            print(f"{COLOR_MAGENTA}You are currently at {COLOR_YELLOW}{player.location}{COLOR_MAGENTA}! \n{COLOR_BLUE}Where would you like to go?")
            num = 0
            for l in locations:
                location = locations[l]
                if location['name'] != player.location:
                    num += 1
                    #print(f"{COLOR_GRAY}{l}. {COLOR_YELLOW}{location['name']} {COLOR_GRAY}(You are here!)")
                    print(f"{COLOR_GRAY}{num}. {COLOR_YELLOW}{location['name']} [Minimum Level: {location['minLevel']}]")
                    travelLocations.update({f"{num}": location['name']})
            print(f"{COLOR_GRAY}{num+1}. {COLOR_YELLOW}Exit")
            travelLocations.update({f"{num+1}": 'exit'})
            if travelTo != "0":
                try:
                    if player.level < int(location[travelTo]['minLevel']):
                        print(f"{COLOR_RED}You are too low level!{COLOR_RESET}")
                    else:
                        print(f"{COLOR_RED}Please input a valid option!{COLOR_RESET}")
                except:
                    print(f"{COLOR_RED}Please input a valid option!{COLOR_RESET}")
            travelTo = input(f"{COLOR_GREEN}> {COLOR_RESET}")



def goToVillage(player):
    shops = {
        "1": {"name":"General Store", "run": general},
        "2": {"name":"Armoursmith", "run": armoursmith},
        "3": {"name":"Weaponsmith", "run": weaponsmith},
        "4": {"name":"Jewelery Store", "run": jewelery},
        "5": {"name":"Accessory Store", "run": accessory},
        "6": {"name":"Exit", "run": ""}
    }
    gotoShop = "0"
    shopping = False
    while not shopping:
        try:
            shop = shops[gotoShop]
            if gotoShop != "6":
                shop['run'](player)
            shopping = True
        except:
            os.system('cls')
            print(f"{COLOR_MAGENTA}You are in {COLOR_YELLOW}{getVillage(player)}{COLOR_MAGENTA}! \n{COLOR_BLUE}What shop would you like to go to?")
            for shop in shops:
                goto = shops[shop]
                print(f"{COLOR_GRAY}{shop}. {COLOR_YELLOW}{goto['name']}")
            if gotoShop != "0":
                print(f"{COLOR_RED}Please input a valid option!{COLOR_RESET}")
            gotoShop = input(f"{COLOR_GREEN}> {COLOR_RESET}")

def inventory(player):
    os.system('cls')
    print(f"{COLOR_MAGENTA}{player.name}'s Inventory:")
    printInventory(player)
    input()

# game

def game():
    shopType = ""

    os.system("cls")
    player = Player(input(f"{COLOR_MAGENTA}What is your name? {COLOR_RESET}"))
    player.choose_class()

    mainOptions = {
        "1": fight,
        "2": explore,
        "3": goToVillage,
        "4": inventory
    }

    choice = "0"
    while True:
        try:
            mainOptions[choice](player)
            choice = "0"
        except:
            os.system("cls")
            printStats(player)
            printOptions(player)
            if choice != "0":
                print(f"{COLOR_RED}Please input a valid option!{COLOR_RESET}")
            choice = input(f"{COLOR_GREEN}> {COLOR_RESET}")


game()