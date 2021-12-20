import random
from random import randint
import time
from termcolor import colored
# grey
# red
# green
# yellow
# blue
# magenta
# cyan
# white
from tabulate import tabulate

# print colored('text', 'color of text')
import colorama
from colorama import Fore, Style

score = 0
pGoldCoins = 0
utlraCoins = 0
waterBottleHp = 100000
jabbariStats = {
	"hp": 100, 
    "bhp": 100,
	"atk": 15, 
	"def": 5
}
markStats = {
	"hp": 120, 
    "bhp": 120,
	"atk": 10, 
	"def": 5
}
justinStats = {
	"hp": 80, 
    "bhp": 80,
	"atk": 20, 
	"def": 5
}

#weapons
WaterGun = {"Name": "Water Gun", "DMG": 15, "ACC": 60}
WoodenStick = {"Name": "Wooden Stick" ,"DMG": 10, "ACC": 70}
MetalStick = {"Name": "Metal Stick" ,"DMG": 20, "ACC": 70, "Price": 20}
WaterBlaster = {"Name": "Water Blaster" ,"DMG": 25, "ACC": 65, "Price": 30}
LaserGun = {"Name": "Laser Gun" ,"DMG":30, "ACC": 75, "Price": 50}
Exterminator = {"Name": "Exterminator" ,"DMG":50, "ACC": 65, "Price": 100}

weaponSmithItems = [MetalStick, WaterBlaster, LaserGun, Exterminator]


#playerweapons
pWeapons = [WaterGun, WoodenStick]


#moves
LightAttack = {"Name": "Light Attack", "DMG": 20, "ACC": 30}
MediumAttack = {"Name": "Medium Attack", "DMG": 25, "ACC": 20}
Dash = {"Name": "Dash", "DMG": 25, "ACC": 30, "Price": 20}
HeavyAttack = {"Name": "Heavy Attack", "DMG": 35, "ACC": 15, "Price": 30}
UltraAim = {"Name": "Ultra Aim", "DMG": 25, "ACC": 40, "Price": 45}
RapidFire = {"Name": "Rapid Fire", "DMG": 40, "ACC": 30, "Price": 75}
UltraAttack = {"Name": "Ultra Attack", "DMG": 50, "ACC": 30, "Price": 80}

moveShopItems = [Dash, HeavyAttack, UltraAim, RapidFire, UltraAttack]

#playermoves
pMoveSet = [LightAttack, MediumAttack]


#upgrades
hpboost = {"Name": "Hp Boost", "Price": 30}
defboost = {"Name": "Def Boost", "Price": 30}
atkboost = {"Name": "Atk Boost", "Price": 40}

upgradeShopItems = [hpboost, defboost, atkboost]


#ultra things

MegaBlaster = {"Name": "Mega Blaster", "DMG": 65, "ACC": 70, "Price": }
JumboRocket = {"Name": "Jumbo Rocket", "DMG": 80, "ACC": 30, "Price": 20}
InfintyGun = {"Name": "Dash", "DMG": 25, "ACC": 30, "Price": 20}

OmegaAttack = {"Name": "Dash", "DMG": 25, "ACC": 30, "Price": 20}
SuperSpeed = {"Name": "Dash", "DMG": 25, "ACC": 30, "Price": 20}
OmniAttack = {"Name": "Dash", "DMG": 25, "ACC": 30, "Price": 20}

UltraBoost = {}


table = [["1. Metal Stick", "20 DMG, 70 ACC", 25],["2. Water Blaster", "25 DMG, 65 ACC", 40],["3. Laser Gun","30 DmG, 75 ACC", 65], ["4. Exterminator", "50 DMG, 65 ACC", 100]]


#ENEMIES

Zombie = {"atk": 10, "def": 20, "hp": 100, "acc": 85, "name": "Zombie", "coins": 15}
Skeleton = {"atk": 12, "def": 10, "hp": 100, "acc": 80, "name": "Skeleton", "coins": 20}

GiantSpider ={"atk": 10, "def": 5, "hp": 120, "name": "Giant Spider"}
MutantWolf = {"atk": 10, "def": 5, "hp": 120, "name": "Mutant Wolf"}
StoneGolem = {"atk": 30, "def": 40, "hp": 200, "name": "Stone Golem"}
UndeadCorpse = {"atk": 10, "def": 5, "hp": 150, "name": "Undead Corpse"}

enemyList = [Zombie, Skeleton]


#Staggered Text
def staggeredText(delay, text):
    for i in text:
        print(i, end='', flush=True)
        time.sleep(delay)
    print('')

staggeredText(0.25, '')
staggeredText(0.003, colored(" ____      ____      __                                       _            ____      ____      _                   ______              ___                               ", 'blue'))
staggeredText(0.003, colored("|_  _|    |_  _|    [  |                                     / |_         |_  _|    |_  _|    / |_                |_   _ `.          .' ..]                              ", 'cyan'))
staggeredText(0.003, colored("  \ \  /\  / /.---.  | |  .---.   .--.   _ .--..--.  .---.  `| |-' .--.     \ \  /\  / /,--. `| |-'.---.  _ .--.    | | `. \ .---.  _| |_  .---.  _ .--.   .---.  .---.  ", 'blue'))
staggeredText(0.003, colored("   \ \/  \/ // /__\\ | | / /'`\]/ .'`\ \[ `.-. .-. |/ /__\\  | | / .'`\ \    \ \/  \/ /`'_\ : | | / /__\\[ `/'`\]   | |  | |/ /__\\'-| |-'/ /__\\[ `.-. | / /'`\]/ /__\\ ", 'cyan'))
staggeredText(0.003, colored("    \  /\  / | \__., | | | \__. | \__. | | | | | | || \__.,  | |,| \__. |     \  /\  / // | |,| |,| \__., | |      _| |_.' /| \__.,  | |  | \__., | | | | | \__. | \__., ", 'blue'))
staggeredText(0.003, colored("     \/  \/   '.__.'[___]'.___.' '.__.' [___||__||__]'.__.'  \__/ '.__.'       \/  \/  \'-;__/\__/ '.__.'[___]    |______.'  '.__.' [___]  '.__.'[___||__]'.___.' '.__.' ", 'cyan'))
print ("")

characterPlay = 0
while characterPlay == 0:
	character = input("Who would you like to play as?, 'Jabbari', his friend 'Mark', or his sister 'Justin'\n").lower()
	if character == "jabbari":
		staggeredText(0.1, colored("Hello Jabbari!", 'magenta'))
		characterPlay == 1
		break
	elif character == "justin":
		staggeredText(0.1, colored("Hello Justin!", 'magenta'))
		characterPlay == 1
		break
	elif character == "mark":
		staggeredText(0.1, colored("Hello Mark!", 'magenta'))
		characterPlay == 1
		break
	else:
		print (colored("Please either type 'Jabbari', 'Justin', or 'Mark'\n", 'magenta'))


    
time.sleep(1)
score = 0
goldCoins = 0
utlraCoins = 0
waterBottleHp = 100000


if character == "jabbari":
	playerStats = jabbariStats
elif character == "mark":
	playerStats = markStats
elif character == "justin":
	playerStats = justinStats

print ("")
print (colored("Here are your base starting stats " + character, 'blue'))
print ("")
print (colored(playerStats, 'yellow'))
time.sleep(2)
print("")
staggeredText(0.025, colored("hp is the amount of health you have, if is reaches 0 during a battle then you lose, you can increase this with upgrades", 'magenta'))
staggeredText(0.025, colored("bhp is your base hp, this is what you hp will be set to after each battle, you can increase this with upgrades", 'yellow'))
print ("")
staggeredText(0.025, colored("atk is the amount of damage your player does, this can be increased with upgrades", 'magenta'))
staggeredText(0.025, colored("def is the amount of defense you have, this will decrease the damage you take, you can also increase this with upgrades", 'yellow'))
print ("")
staggeredText(0.025, colored("The DMG of a move or weapon is the amount of damage it does, better weapons can do more damage", 'magenta'))
staggeredText(0.025, colored("The ACC of a weapon or move is the accuracy, the chance that you will hit instead of miss the enemy, better weapons can have better accuracy", 'yellow'))



#PlayerWeaponChoose
def playerWeaponChoose():
    global pCurrentWeapon
    print(colored('Your weapons: ', 'green'), end='')
    incrementStage = 0
    pCurrentWeapon = 0
    for i in pWeapons:
        print(f'{incrementStage + 1}. {i["Name"]}, ', end='')
        incrementStage += 1
    pCurrentWeaponInput = input('Type the number of the weapon you want to use.\n')
    try:
        pCurrentWeapon = int(pCurrentWeaponInput)
    except:
        print (colored('That is not an number. Try again.', 'red'))
        return playerWeaponChoose()

    if pCurrentWeapon > len(pWeapons):
        print (colored('That is not an option. Try again.', 'red'))
        return playerWeaponChoose()

    pCurrentWeapon = pWeapons[pCurrentWeapon - 1]
    staggeredText(0.025, "You are now using " + colored(pCurrentWeapon['Name'], 'blue'))
    print ("")
    
#PlayerMoveChoose
def playerMoveChoose():
    global pCurrentMove
    print (colored('Your Moves: ', 'green'), end='')
    incrementStage = 0
    pCurrentMove = 0
    for i in pMoveSet:
        print (f'{incrementStage + 1}. {i["Name"]}, ', end='')
        incrementStage += 1
    pCurrentMoveInput = input('Type the number of the move you want to use.\n')
    try:
        pCurrentMove = int(pCurrentMoveInput)
    except:
        print (colored('That is not an number. Try again.', 'red'))
        return playerMoveChoose()

    if pCurrentMove > len(pMoveSet):
        print (colored('That is not an option. Try again', 'red'))
        return playerMoveChoose()

    pCurrentMove = pMoveSet[pCurrentMove -1]
    staggeredText(0.025, "You are now using " + colored(pCurrentMove['Name'], 'blue'))
    print ("")

#PlayerDamage
def playerDMG():
    global pCurrentWeapon, pCurrentMove, enemy, enemyhp
    dmg = pCurrentWeapon["DMG"] + playerStats["atk"] + pCurrentMove["DMG"] - enemy["def"]
    if dmg < 0:
        dmg = 0
    hitchance = pCurrentMove["ACC"] + pCurrentWeapon["ACC"]
    if randint(1, 100) <= hitchance:
        enemyhp -= dmg
        time.sleep(1)
        print ("You hit", colored(enemy["name"], 'yellow'), "for", colored(dmg, 'red'), "damage!")
        if enemyhp <= 0:
            print ("You are now at", colored(playerStats["hp"], 'green'), "hp, the", colored(enemy["name"], 'yellow'), "has been defeated")
        else:
            print ("You are now at", colored(playerStats["hp"], 'green'), "hp, the", colored(enemy["name"], 'yellow'), "is now at", colored(enemyhp, 'red'), "hp")
        print ("")
    else:
        time.sleep(2)
        print (colored('You missed...', 'red'))
        print ("")

#CPUMove
def cpuMove():
    global playerhp
    if enemyhp > 0:
        dmg = enemy["atk"] - playerStats["def"]
        if dmg < 0:
            dmg = 0
        if randint(1,100) <= enemy["acc"]:
            playerStats["hp"] -= dmg
            print ("")
            time.sleep(1)
            print("The", colored(enemy["name"], 'yellow'), "hit you for", colored(dmg, 'red'), "damage." '''
    You are now at''', colored(playerStats["hp"], 'green'), "hp, the", colored(enemy["name"], 'yellow'), "is now at", colored(enemyhp, 'red'), "hp")
            print ("")
        else:
            print ("")
            print(colored('The opponent missed...', 'red'))
            print ("")
    else:
        print ("")

#Endmove
def endMove():
    global enemyhp, pGoldCoins, waterBottleHp
    if playerStats["hp"] <= 0:
        waterBottleHp -= enemy["atk"]
        playerStats["hp"] = playerStats["bhp"]
        print ("")
        print (colored("The " + enemy["name"] + " defeated you", 'red'))
        print (colored("The Water Pillar took " + str(enemy["atk"]) + " damage!. It is now at " + str(waterBottleHp) + " hp!", 'magenta'))
    else:
        print ("")

#Tutorial       
def tutorial():
    global waterBottleHp, enemy, enemyhp, pGoldCoins
    print ("")
    staggeredText(0.05, colored("Hello there, this is the tutorial, it will teach you how to play the game", 'cyan'))
    print ("")
    staggeredText(0.05, colored("First you must learn how to defend the water pillar from attacking monsters", 'cyan'))
    print ("")
    staggeredText(0.05, colored("Now you must choose a weapon and then choose a move", 'cyan'))
    for i in range (2):
        enemy = random.choice(enemyList)

        print ("")
        print("A", colored(enemy["name"], 'yellow'), "attacked you!")
        print ("")
        enemyhp = enemy["hp"]
        while enemyhp > 0:
            playerWeaponChoose()
            playerMoveChoose()
            playerDMG()
            cpuMove()
            endMove()
            if enemyhp <= 0:
                pGoldCoins += enemy["coins"]
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " gold coins" + " you now have " + str(pGoldCoins) +  " gold coins!", 'magenta'))
        
    print ("")
    print (colored("You have now defeated your first wave of monsters. Great Job!", 'cyan'))
    print ("")
    print (colored("As the game goes on waves will get harder to beat", 'cyan'))
    print ("")
    print (colored("Next lets check out the shop, here you can spend gold coins from beating monsters on cool new things", 'magenta'))
    shopFunc()


#WeaponSmithFunc
def weaponSmith():
    global chosenItem, pGoldCoins
    print ("")
    print (colored("Welcome to the Weapon Smith", 'red'))

    table = [["1. Metal Stick", "20 DMG, 70 ACC", 25],["2. Water Blaster", "25 DMG, 65 ACC", 40],["3. Laser Gun","30 DmG, 75 ACC", 65], ["4. Exterminator", "50 DMG, 65 ACC", 100]]
    headers = ["Item", "Stats", "Cost"]
    print(tabulate(table, headers, tablefmt="psql"))
    print ("")

    itemChooseInput = input(colored("Please type the number of the weapon you want to buy or type 0 to exit:", 'cyan'))
    print ("")
    try:
        chosenItem = int(itemChooseInput)
    except:
        print (colored("That is not a number. Try again.", 'red'))
        print ("")
        return weaponSmith()

    if chosenItem == 0:
        return shopFunc()
        
    elif chosenItem > len(weaponSmithItems):
        print (colored("That is not an option. Try again.", 'red'))
        print ("")
        return weaponSmith()
    
    chosenItem = weaponSmithItems[chosenItem - 1]

    if chosenItem in pWeapons:
        staggeredText(0.05, colored("You already have this weapon", 'magenta'))
        return weaponSmith()
    elif chosenItem not in pWeapons:
        print ("")
        if chosenItem['Price'] > pGoldCoins:
            staggeredText(0.05, colored("You do not have enough gold coins to buy this weapon. ", 'red'))
            print ("")
            return weaponSmith()

        elif chosenItem['Price'] <= pGoldCoins:
            didBuy = 0

            while didBuy == 0:
                print (colored("To buy this weapon, type 'buy', or to exit type 'exit", 'yellow'))
                print ("")
                wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(pGoldCoins) + " gold coins left.\n").lower()
                if wannaBuy == "buy":
                    pGoldCoins -= chosenItem['Price']
                    staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " gold coins", 'green'))
                    print ("The " + chosenItem['Name'] + " has now been added to your weapons menu")
                    pWeapons.append(chosenItem)
                    didBuy = 1
                    return weaponSmith()

                
                elif wannaBuy == "exit":
                    staggeredText(0.05, colored("Exiting...", 'yellow'))
                    didBuy = 1
                    return weaponSmith()

                else:
                    print ("")
                    print (colored("That is not an option", 'red'))
                    print ("")
                    didBuy = 0



#MoveShopFunc
def MoveShop():
    global chosenItem, pGoldCoins
    print ("")
    print (colored("Welcome to the Move Shop", 'blue'))

    table = [["1. Dash", "25 DMG, 30 ACC", 20],["2. Heavy Attack", "35 DMG, 15 ACC", 30],["3. Ultra Aim","25 DmG, 40 ACC", 45], ["4. RapidFire", "40 DMG, 30 ACC", 75], ["5. Ultra Attack", "50 DMG, 30 ACC", 80]]
    headers = ["Item", "Stats", "Cost"]
    print(tabulate(table, headers, tablefmt="psql"))
    print ("")

    itemChooseInput = input(colored("Please type the number of the move you want to buy or type 0 to exit:", 'cyan'))
    print ("")
    try:
        chosenItem = int(itemChooseInput)
    except:
        print (colored("That is not a number. Try again.", 'red'))
        print ("")
        return MoveShop()

    if chosenItem == 0:
        return shopFunc()
        
    elif chosenItem > len(moveShopItems):
        print (colored("That is not an option. Try again.", 'red'))
        print ("")
        return MoveShop()
    
    chosenItem = moveShopItems[chosenItem - 1]

    if chosenItem in pMoveSet:
        staggeredText(0.05, colored("You already have this move", 'magenta'))
        return MoveShop()
    elif chosenItem not in pMoveSet:
        print ("")
        if chosenItem['Price'] > pGoldCoins:
            staggeredText(0.05, colored("You do not have enough gold coins to buy this item. ", 'red'))
            print ("")
            return MoveShop()

        elif chosenItem['Price'] <= pGoldCoins:
            didBuy = 0

            while didBuy == 0:
                print (colored("To buy this move, type 'buy', or to exit type 'exit", 'yellow'))
                print ("")
                wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(pGoldCoins) + " gold coins left.\n").lower()
                if wannaBuy == "buy":
                    pGoldCoins -= chosenItem['Price']
                    staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " gold coins", 'green'))
                    print ("The " + chosenItem['Name'] + " has now been added to your moves menu")
                    pMoveSet.append(chosenItem)
                    didBuy = 1
                    return MoveShop()

                
                elif wannaBuy == "exit":
                    staggeredText(0.05, colored("Exiting...", 'yellow'))
                    didBuy = 1
                    return MoveShop()

                else:
                    print ("")
                    print (colored("That is not an option", 'red'))
                    print ("")
                    didBuy = 0

#UpgradeShopFunc
def upgradeShop():
    global chosenItem, pGoldCoins
    print ("")
    print (colored("Welcome to the Upgrade Shop", 'blue'))

    table = [["1. Hp Boost", "Incrases your hp and bhp by 15", 30],["2. Def Boost", "Increase your defence by 10", 30],["3. Atk Boost","Increase your attack by 15", 40]]
    headers = ["Item", "Stats", "Cost"]
    print(tabulate(table, headers, tablefmt="psql"))
    print ("")

    itemChooseInput = input(colored("Please type the number of the upgrade you want to buy or type 0 to exit:", 'cyan'))
    print ("")
    try:
        chosenItem = int(itemChooseInput)
    except:
        print (colored("That is not a number. Try again.", 'red'))
        print ("")
        return upgradeShop()

    if chosenItem == 0:
        return upgradeShop()
        
    elif chosenItem > len(upgradeShopItems):
        print (colored("That is not an option. Try again.", 'red'))
        print ("")
        return upgradeShop()
    
    chosenItem = upgradeShopItems[chosenItem - 1]

    if chosenItem['Price'] > pGoldCoins:
        staggeredText(0.05, colored("You do not have enough gold coins to buy this upgrade. ", 'red'))
        print ("")
        return upgradeShop()

    elif chosenItem['Price'] <= pGoldCoins:
        print (colored("To buy this upgrade, type 'buy', or to exit type 'exit", 'yellow'))
        print ("")
        didBuy = 0
        while didBuy == 0:

            wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(pGoldCoins) + " gold coins left.\n").lower()
            if wannaBuy == "buy":
                if chosenItem['Name'] == "Hp Boost":
                    pGoldCoins -= chosenItem['Price']
                    playerStats["hp"] += 15
                    playerStats['bhp'] += 15
                    staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " gold coins", 'yellow'))
                    staggeredText(0.05, colored("Your hp is now at " + str(playerStats['hp']), 'green'))
                    print ("")

                elif chosenItem['Name'] == "Def Boost":
                    pGoldCoins -= chosenItem['Price']
                    playerStats["def"] += 10
                    staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " gold coins", 'yellow'))
                    staggeredText(0.05, colored("Your def is now at " + str(playerStats['def']), 'green'))
                    print ("")

                elif chosenItem['Name'] == "Atk Boost":
                    pGoldCoins -= chosenItem['Price']
                    playerStats['atk'] += 15
                    staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " gold coins", 'green'))
                    staggeredText(0.05, colored("Your atk is now at " + str(playerStats['atk']), 'green'))
                    print ("")

                didBuy = 1
                return upgradeShop

            else:
                print ("")
                print (colored("That is not an option", 'red'))
                didBuy = 0


#ultraShopFunc
def ultraShop():
    global chosenItem, pGoldCoins
    print ("")
    print (colored("Welcome to the Ultra Shop", 'magenta'))
    print ("Here everything costs ultra coins which can be obtained by killing bosses")

    table = [["1. Metal Stick", "20 DMG, 70 ACC", 25],["2. Water Blaster", "25 DMG, 65 ACC", 40],["3. Laser Gun","30 DmG, 75 ACC", 65], ["4. Exterminator", "50 DMG, 65 ACC", 100]]
    headers = ["Item", "Stats", "Cost"]
    print(tabulate(table, headers, tablefmt="psql"))
    print ("")

    itemChooseInput = input(colored("Please type the number of the weapon you want to buy or type 0 to exit:", 'cyan'))
    print ("")
    try:
        chosenItem = int(itemChooseInput)
    except:
        print (colored("That is not a number. Try again.", 'red'))
        print ("")
        return weaponSmith()

    if chosenItem == 0:
        return shopFunc()
        
    elif chosenItem > len(weaponSmithItems):
        print (colored("That is not an option. Try again.", 'red'))
        print ("")
        return weaponSmith()
    
    chosenItem = weaponSmithItems[chosenItem - 1]

    if chosenItem in pWeapons:
        staggeredText(0.05, colored("You already have this weapon", 'magenta'))
        return weaponSmith()
    elif chosenItem not in pWeapons:
        print ("")
        if chosenItem['Price'] > pGoldCoins:
            staggeredText(0.05, colored("You do not have enough gold coins to buy this weapon. ", 'red'))
            print ("")
            return weaponSmith()

        elif chosenItem['Price'] <= pGoldCoins:
            pGoldCoins -= chosenItem['Price']
            print (colored("To buy this weapon, type 'buy', or to exit type anything else", 'yellow'))
            print ("")
            wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(pGoldCoins) + " gold coins left.\n").lower()
            if wannaBuy == "buy":
                staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " gold coins", 'green'))
                print ("The " + chosenItem['Name'] + " has now been added to your weapons menu")
                pWeapons.append(chosenItem)
                return weaponSmith()
            else:
                pGoldCoins += chosenItem['Price']
                print ("")
                print ("You have not bough this weapon")
                print ("")
                return weaponSmith()




shopWhereLoop = 0
#ShopFunc
def shopFunc():
    global shopWhereLoop
    print ("")
    staggeredText(0.1, colored("Welcome to the shop", 'yellow'))
    print ("")
    while shopWhereLoop == 0:
        shopWhere = input("Where you like to go. 1. Weapon Smith, 2. Move Shop, 3. Upgrade Shop, 4. Ultra Shop or 0. Exit")
        print ("")
        

        if shopWhere == '0':
            staggeredText(0.1, colored("Exiting ...", 'red'))
            shopWhereLoop = 1
            break

        elif shopWhere == '1':
            weaponSmith()
            shopWhereLoop = 1
            break

        elif shopWhere == '2':
            MoveShop()
            shopWhereLoop = 1
            break

        elif shopWhere == '3':
            upgradeShop()
            shopWhereLoop = 1
            break

        elif shopWhere == '4':
            ultraShop()
            shopWhereLoop = 1
            break

        else:
            print (colored("That is not an option please try again.", 'red'))
            print ("")







#NewGame
def newGame():
    print ("Would you like to start a new game?")
    startNewGame = input('Type yes or no: ')

    if startNewGame.lower() == 'yes':
        print('Hi')
    elif startNewGame.lower() == 'no':
        exit()
    else:
        print(colored('That is not an option. Try again.', 'red'))
        newGame()



playTutorial = 0
while playTutorial == 0:
    print ("")
    tutorialPlay = input("Would you like to play the tutorial " + colored('yes', 'green') + " or no " + colored("no", 'red') + ":")
    if tutorialPlay == "yes" or tutorialPlay == "Yes":
        tutorial()
        playTutorial += 1 
        break
    elif tutorialPlay == "no" or tutorialPlay == "No":
        playTutorial += 1
        newGame()
        break
    else:
        print ("That is not a valid option, please type either yes or no")
        playTutorial = 0


print ("hi")




# while playerStats["hp"] > 0:
#     enemy = random.choice(enemyList)

#     print ("")
#     print("A", colored(enemy["name"], 'yellow'), "attacked you!")
#     print ("")
#     enemyhp = enemy["hp"]
#     while enemyhp > 0:
#         playerWeaponChoose()
#         playerMoveChoose()
#         playerDMG()
#         cpuMove()
