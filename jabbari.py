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
pUltraCoins = 0
waterPilarHp = 100000
jabbariStats = {
	"hp": 125, 
    "bhp": 125,
	"atk": 15, 
	"def": 10
}
markStats = {
	"hp": 150, 
    "bhp": 150,
	"atk": 10, 
	"def": 10
}
justinStats = {
	"hp": 100, 
    "bhp": 100,
	"atk": 20, 
	"def": 10
}

#weapons
WaterGun = {"Name": "Water Gun", "DMG": 15, "ACC": 60}
WoodenStick = {"Name": "Wooden Stick" ,"DMG": 10, "ACC": 70}
MetalStick = {"Name": "Metal Stick" ,"DMG": 20, "ACC": 70, "Price": 20}
WaterBlaster = {"Name": "Water Blaster" ,"DMG": 25, "ACC": 65, "Price": 30}
LaserGun = {"Name": "Laser Gun" ,"DMG":30, "ACC": 75, "Price": 50}
Exterminator = {"Name": "Exterminator" ,"DMG":50, "ACC": 65, "Price": 65}
SwordOfMight = {"Name": "Sword of Might" ,"DMG":65, "ACC": 70, "Price": 80}
OceanRipper = {"Name": "Ocean Ripper" ,"DMG":75, "ACC": 75, "Price": 100}
Tsunami = {"Name": "Tsunami" ,"DMG":85, "ACC": 80, "Price": 120}
PrismOfLight = {"Name": "Prism of Light" ,"DMG":100, "ACC": 75, "Price": 150}


weaponSmithItems = [MetalStick, WaterBlaster, LaserGun, Exterminator, SwordOfMight, OceanRipper, Tsunami, PrismOfLight]


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
SteelAssault = {"Name": "Steel Assault", "DMG": 65, "ACC": 35, "Price": 100}
EaglesEye = {"Name": "Eagles Eye", "DMG": 75, "ACC": 40, "Price": 120}
DragonAttack = {"Name": "Dragon Attack", "DMG": 90, "ACC": 45, "Price": 150}


moveShopItems = [Dash, HeavyAttack, UltraAim, RapidFire, UltraAttack, SteelAssault, EaglesEye, DragonAttack]

#playermoves
pMoveSet = [LightAttack, MediumAttack]


#upgrades
hpboost = {"Name": "Hp Boost", "Price": 30}
defboost = {"Name": "Def Boost", "Price": 30}
atkboost = {"Name": "Atk Boost", "Price": 40}

upgradeShopItems = [hpboost, defboost, atkboost]


#ultra things

MegaBlaster = {"Name": "Mega Blaster", "DMG": 75, "ACC": 70, "Price": 30}
JumboRocket = {"Name": "Jumbo Rocket", "DMG": 90, "ACC": 70, "Price": 40}
InfinityGun = {"Name": "Infinity Gun", "DMG": 150, "ACC": 100, "Price": 100}

OmegaAttack = {"Name": "Omega Attack", "DMG": 70, "ACC": 30, "Price": 30}
SuperSpeed = {"Name": "Super Speed", "DMG": 85, "ACC": 40, "Price": 45}
OmniAttack = {"Name": "Omni Attack", "DMG": 135, "ACC": 100, "Price": 100}

UltraBoost = {"Name": "Ultra Boost", "Price": 40}


ultraShopItems = [MegaBlaster, JumboRocket, InfinityGun, OmegaAttack, SuperSpeed, OmniAttack, UltraBoost]

#ENEMIES

Zombie = {"atk": 15, "def": 20, "hp": 100, "acc": 85, "name": "Zombie", "coins": 15}
Skeleton = {"atk": 20, "def": 10, "hp": 100, "acc": 80, "name": "Skeleton", "coins": 20}
WereWolf = {"atk": 25, "def": 5, "hp": 120, "acc": 90, "name": "Were Wolf", "coins": 20}
Ogre = {"atk": 25, "def": 5, "hp": 150, "acc": 80, "name": "Ogre", "coins": 30}
ShadowArcher = {"atk": 35, "def": 5, "hp": 90, "acc": 90, "name": "Shadow Archer", "coins": 25}
Golem = {"atk": 30, "def": 40, "hp": 200, "acc": 75, "name": "Golem", "coins": 30}
Yeti = {"atk": 40, "def": 20, "hp": 150, "acc": 80, "name": "Yeti", "coins": 40}
DarkKnight = {"atk": 55, "def": 30, "hp": 180, "acc": 90, "name": "Dark Knight", "coins": 50}
MagmaElemantal = {"atk": 50, "def": 50, "hp": 250, "acc": 80, "name": "Magma Elemental", "coins": 65}
Necromancer = {"atk": 75, "def": 25, "hp": 150, "acc": 90, "name": "Necromancer", "coins": 85}
PhantomKnight = {"atk": 85, "def": 45, "hp": 250, "acc": 90, "name": "Phantom Knight", "coins": 100}


#Bosses

TheJuggernaut = {"atk": 35, "def": 35, "hp": 150, "acc": 75, "name": "The Juggernaut", "coins": 30}
TheFrostGiant = {"atk": 50, "def": 40, "hp": 250, "acc": 75, "name": "The Frost Giant", "coins": 45}
TheLeviathan = {"atk": 75, "def": 50, "hp": 350, "acc": 75, "name": "The Leviathan", "coins": 60}
TheDragonKing = {"atk": 100, "def": 60, "hp": 450, "acc": 75, "name": "The Dragon King", "coins": 80}
TheOverseer = {"atk": 130, "def": 75, "hp": 600, "acc": 75, "name": "The Overseer", "coins": 100}




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


time.sleep(1)
score = 0
goldCoins = 10000
utlraCoins = 10000
waterPillarHp = 1000


#Tutorial       
def tutorial():
    global waterPillarHp, enemy, enemyhp, pGoldCoins, newGame, playerStats

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
    time.sleep(1)
    print("")
    staggeredText(0.025, colored("hp is the amount of health you have, if is reaches 0 during a battle then you lose, you can increase this with upgrades", 'magenta'))
    staggeredText(0.025, colored("bhp is your base hp, this is what you hp will be set to after each level, you can increase this with upgrades", 'yellow'))
    print ("")
    staggeredText(0.025, colored("atk is the amount of damage your player does, this can be increased with upgrades", 'magenta'))
    staggeredText(0.025, colored("def is the amount of defense you have, this will decrease the damage you take, you can also increase this with upgrades", 'yellow'))
    print ("")
    staggeredText(0.025, colored("The DMG of a move or weapon is the amount of damage it does, better weapons can do more damage", 'magenta'))
    staggeredText(0.025, colored("The ACC of a weapon or move is the accuracy, the chance that you will hit instead of miss the enemy, better weapons can have better accuracy", 'yellow'))


    print ("")
    staggeredText(0.05, colored("Hello there, this is the tutorial, it will teach you how to play the game", 'cyan'))
    print ("")
    staggeredText(0.05, colored("First you must learn how to defend the water pillar from attacking monsters", 'cyan'))
    print ("")
    staggeredText(0.05, colored("Now you must choose a weapon and then choose a move", 'cyan'))
    print ("")
    
    Zombie = {"atk": 15, "def": 20, "hp": 100, "acc": 85, "name": "Zombie", "coins": 15}
    Skeleton = {"atk": 20, "def": 10, "hp": 100, "acc": 80, "name": "Skeleton", "coins": 20}

    enemy = Zombie
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

    enemy = Skeleton
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




    print ("")
    print ("")
    print (colored("You have now defeated your first wave of monsters. Great Job!", 'cyan'))
    print ("")
    print (colored("As the game goes on waves will get harder to beat", 'cyan'))
    print ("")
    print (colored("On levels 3, 6, 9, 12 and 15 there will be a boss, bosses are extra hard to defeat but will give ultra coins when defeated", 'cyan'))
    print ("")
    print (colored("Next lets check out the shop, you can visit here after each level and you can spend gold coins from beating monsters on cool new things", 'magenta'))
    shopFunc()
    print ("")
    print (colored("Now lets check out your inventory, you can also visit here after each level and see your weapons, moves, stats and more", 'yellow'))
    inventory()

    staggeredText(0.05, colored("Great!, now that you have completed the tutorial you are ready to start the real game.", 'green'))
    print ("")
    newGame()


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
    global pCurrentWeapon, pCurrentMove, enemy, enemyhp, playerStats
    dmg = pCurrentWeapon["DMG"] + playerStats["atk"] + pCurrentMove["DMG"] - enemy["def"]
    if dmg < 0:
        dmg = 0
    hitchance = pCurrentMove["ACC"] + pCurrentWeapon["ACC"]
    if randint(1, 100) <= hitchance:
        enemyhp -= dmg
        if enemyhp < 0:
            enemyhp = 0
        time.sleep(1)
        print ("")
        print ("--------------------------------------------------------------------------------------------------------------")
        print ("")
        print ("You hit", colored(enemy["name"], 'yellow'), "for", colored(dmg, 'red'), "damage!")
        
        print ("You are now at", colored(playerStats["hp"], 'green'), "hp, the", colored(enemy["name"], 'yellow'), "is now at", colored(enemyhp, 'red'), "hp")
        print ("")
    else:
        time.sleep(2)
        print ("")
        print ("--------------------------------------------------------------------------------------------------------------")
        print ("")
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
            print ("--------------------------------------------------------------------------------------------------------------")
            print ("")
        else:
            print ("")
            print(colored('The opponent missed...', 'red'))
            print ("")
            print ("--------------------------------------------------------------------------------------------------------------")
            print ("")
    else:
        print

#Endmove
def endMove():
    global enemyhp, pGoldCoins, waterPillarHp
    if playerStats["hp"] <= 0:
        playerStats['hp'] = 0
        waterPillarHp -= enemy["atk"]
        playerStats["hp"] = playerStats["bhp"]
        print ("")
        staggeredText(0.05, colored("The " + enemy["name"] + " defeated you", 'red'))
        print ("")
        print (colored("The Water Pillar took " + str(enemy["atk"]) + " damage!. It is now at " + str(waterPillarHp) + " hp!", 'yellow'))
        print ("")
        print (colored("You are now back at " + str(playerStats['bhp']) + " hp", 'green'))
        print ("")
        print ("--------------------------------------------------------------------------------------------------------------")
        print ("")
        enemyhp = -999

    else:
        print ("")


#WeaponSmithFunc
def weaponSmith():
    global chosenItem, pGoldCoins
    print ("")
    print (colored("Welcome to the Weapon Smith", 'red'))

    table = [["1. Metal Stick", "20 DMG, 70 ACC", 25],["2. Water Blaster", "25 DMG, 65 ACC", 40],["3. Laser Gun","30 DmG, 75 ACC", 65], ["4. Exterminator", "50 DMG, 65 ACC", 100],["5. Sword of Might", "65 DMG, 70 ACC", 80],["6. Ocean Ripper", "75 DMG, 75 ACC", 100],["7. Tsunami", "85 DMG, 80 ACC", 120],["8. Prism of Light", "100 DMG, 75 ACC", 150]]    
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
                remain = pGoldCoins - chosenItem['Price']
                wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(remain) + " gold coins left.\n").lower()
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
                remain = pGoldCoins - chosenItem['Price']
                wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(remain) + " gold coins left.\n").lower()
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
            remain = pGoldCoins - chosenItem['Price']
            wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " coins. You will only have " + str(remain) + " gold coins left.\n").lower()
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

            elif wannaBuy == "exit":
                staggeredText(0.05, colored("Exiting...", 'yellow'))
                didBuy = 1
                return upgradeShop()

            else:
                print ("")
                print (colored("That is not an option", 'red'))
                didBuy = 0


#ultraShopFunc
def ultraShop():
    global chosenItem, pUltraCoins
    print ("")
    print (colored("Welcome to the Ultra Shop", 'magenta'))
    print (colored("Here everything costs ultra coins which can be obtained by killing bosses", 'yellow'))

    table = [["1. Mega Blaster", "75 DMG, 70 ACC", 30],["2. Jumbo Rocket", "90 DMG, 70 ACC", 40],["3. Infinity Gun","150 DmG, 100 ACC", 100],["", "", ""], ["4. Omega Attack", "70 DMG, 30 ACC", 30], ["5. Super Speed", "DMG 85, ACC 45", 45], ["6. Omni Attack", "DMG 135, ACC 100", 100], ["", "", ""], ["7. Ultra Boost", "Increases all stats by 20 ", 40]]
    headers = ["Item", "Stats", "Cost"]
    print(tabulate(table, headers, tablefmt="psql"))
    print ("")

    itemChooseInput = input(colored("Please type the number of the item you want to buy or type 0 to exit:", 'cyan'))
    print ("")
    try:
        chosenItem = int(itemChooseInput)
    except:
        print (colored("That is not a number. Try again.", 'red'))
        print ("")
        return ultraShop()

    if chosenItem == 0:
        return shopFunc()
        
    elif chosenItem > len(ultraShopItems):
        print (colored("That is not an option. Try again.", 'red'))
        print ("")
        return ultraShop()
    
    chosenItem = ultraShopItems[chosenItem - 1]

    if chosenItem in pWeapons or chosenItem in pMoveSet:
        staggeredText(0.05, colored("You already have this item", 'magenta'))
        return ultraShop()
    elif chosenItem not in pWeapons and chosenItem not in pMoveSet:
        print ("")
        if chosenItem['Price'] > pUltraCoins:
            staggeredText(0.05, colored("You do not have enough ultra coins to buy this item. ", 'red'))
            print ("")
            return ultraShop()

        elif chosenItem['Price'] <= pUltraCoins:
            print (colored("To purchase this item, type 'buy', or to exit type exit", 'yellow'))
            didBuy = 0
            while didBuy == 0:
                remain = pUltraCoins - chosenItem['Price']
                wannaBuy = input("Are you sure you want to buy " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins. You will only have " + str(remain) + " ultra coins left.\n").lower()
                if wannaBuy == "buy":
                    if chosenItem['Name'] == "Mega Blaster":
                        pUltraCoins -= chosenItem['Price']
                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'blue'))
                        pWeapons.append(chosenItem)
                        print (chosenItem["Name"], "has now been added to your weapons menu")
                        print ("")
                        print ("")

                    elif chosenItem['Name'] == "Jumbo Rocket":
                        pUltraCoins -= chosenItem['Price']
                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'blue'))
                        pWeapons.append(chosenItem)
                        print (chosenItem["Name"], "has now been added to your weapons menu")
                        print ("")
                        print ("")

                    elif chosenItem['Name'] == "Infinity Gun":
                        pUltraCoins -= chosenItem['Price']
                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'blue'))
                        pWeapons.append(chosenItem)
                        print (chosenItem["Name"], "has now been added to your weapons menu")
                        print ("")
                        print ("")


                    elif chosenItem['Name'] == "Omega Attack":
                        pUltraCoins -= chosenItem['Price']
                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'blue'))
                        pMoveSet.append(chosenItem)
                        print (chosenItem["Name"], "has now been added to your moves menu")
                        print ("")
                        print ("")

                    
                    elif chosenItem['Name'] == "Super Speed":
                        pUltraCoins -= chosenItem['Price']
                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'blue'))
                        pMoveSet.append(chosenItem)
                        print (chosenItem["Name"], "has now been added to your moves menu")
                        print ("")
                        print ("")


                    elif chosenItem['Name'] == "Omni Attack":
                        pUltraCoins -= chosenItem['Price']
                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'blue'))
                        pMoveSet.append(chosenItem)
                        print (chosenItem["Name"], "has now been added to your moves menu")
                        print ("")
                        print ("")

                    elif chosenItem['Name'] == "Ultra Boost":
                        pUltraCoins -= chosenItem['Price']
                        playerStats["hp"] += 20
                        playerStats["bhp"] += 20
                        playerStats["def"] += 20
                        playerStats["atk"] += 20

                        staggeredText(0.05, colored("You have now bought " + chosenItem['Name'] + " for " + str(chosenItem['Price']) + " ultra coins", 'yellow'))
                        staggeredText(0.025, colored("Your def is now at " + str(playerStats['def']), 'green'))
                        staggeredText(0.05, colored("Your hp is now at " + str(playerStats['hp']), 'green'))
                        staggeredText(0.05, colored("Your bhp is now at " + str(playerStats['bhp']), 'green'))
                        staggeredText(0.05, colored("Your atk is now at " + str(playerStats['atk']), 'green'))
                        print ("")

                    didBuy = 1
                    return ultraShop()

            else:
                print ("")
                print (colored("That is not an option", 'red'))
                didBuy = 0


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

pCurrentLevel = 1
levelFact1 = '''Did you know that drinkable freshwater is only 2.5 percent of the total water on Earth
even though 70 percent of the Earth's surface is covered by water!'''
levelFact2 = '''Did you know that more than 70 percent of industrial waste
is dumped into the water!'''
levelFact3 = '''More than 14 billion pounds of garbage
ends up in the oceans every year!'''
levelFact4 = '''Contaminated water is the cause for various diseases
such as cholera and typhus!'''
levelFact5 = '''Over 15 million children under the age of fie years die 
every year from contaminated water!'''
levelFact6 = '''About 250 million people succumb each year from diseases
due to contaminated water!'''
levelFact7 = '''About 2 million tons of human waste are exposed daily to water!'''
levelFact8 = '''In North America, 45 percent of lakes are polluted
and unstable for swimming, fishing or drinking!'''
levelFact9 = '''Each year over 1.5 trillion gallons of untreated sweage and waste 
are dumped into North American waters!'''
levelFact10 = '''In developing countries, 70 percent of industrial waste is 
dumped into the water!'''
levelFact11 = '''More than 80 percent of sweage in developing countries is 
dumped into the water untreated!'''
levelFact12 = '''Every day, more people die from unsafe water than war!'''
levelFact13 = '''Industry dumps an estimated 400 million tons of
polluted waste in waters every year!'''
levelFact14 = '''Agriculture accounts for 70 percent of total
water consumption worldwide!'''
levelFact15 = '''Polluted and waste water contains bacteria, parasites,
and other life threatening diseases!'''

def inventory():
    print ("")
    staggeredText(0.1, "Checking Inventory...")
    print ("")
    staggeredText(0.05, (colored("Here are your stats", 'green')))
    print (playerStats)
    print ("")
    staggeredText(0.05, (colored("Here are your weapons", 'red')))
    print (pWeapons)
    print ("")
    staggeredText(0.05, (colored("Here are your moves", 'blue')))
    print (pMoveSet)
    print ("")
    staggeredText(0.05, (colored("You have " + str(pGoldCoins) + " gold coins", 'yellow')))
    print ("")
    staggeredText(0.05, (colored("You have " + str(pUltraCoins) + " ultra coins", 'magenta')))
    print ("")
    time.sleep(2)



levelEndLoop = 0
def levelEnd1():
    global levelEndLoop
    print ("")
    while levelEndLoop == 0:
        print ("")
        staggeredText(0.05, colored("What would you like to do", 'yellow'))
        afterLevel = input(colored("Press '1' to go to the shop, '2' to check your inventory, or '3' to start the next level\n"))
        
        if afterLevel == "1":

            print ("")
            shopFunc()
        
        elif afterLevel == "2":
            print ("")
            inventory()
            

        elif afterLevel == "3":
            levelEndLoop = 1
            print ("")
            break

        else:
            print (colored("That is not an option please try again.", 'red'))
            print ("")


#levelEnd
def levelEnd():
    global pCurrentLevel, levelEndLoop
    levelEndLoop = 0
    staggeredText(0.05, colored("Congratualations you have beaten level " + str(pCurrentLevel), 'green'))
    print ("")
    staggeredText(0.05, colored("The Water Pillar is at " + str(waterPillarHp) + " hp.", 'blue'))
    print ("")

    if pCurrentLevel == 1:
        print ("")
        print (colored(levelFact1, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 2:
        print ("")
        print (colored(levelFact2, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 3:
        print ("")
        print (colored(levelFact3, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 4:
        print ("")
        print (colored(levelFact4, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 5:
        print ("")
        time.sleep(1)
        print (colored(levelFact5, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 6:
        print ("")
        time.sleep(1)
        print (colored(levelFact6, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 7:
        print ("")
        print (colored(levelFact7, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 8:
        print ("")
        print (colored(levelFact8, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 9:
        print ("")
        print (colored(levelFact9, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 10:
        print ("")
        print (colored(levelFact10, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 11:
        print ("")
        print (colored(levelFact11, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 12:
        print ("")
        print (colored(levelFact12, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 13:
        print ("")
        print (colored(levelFact13, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 14:
        print ("")
        print (colored(levelFact14, 'cyan'))
        print ("")
        time.sleep(1)
    elif pCurrentLevel == 15:
        print ("")
        print (colored(levelFact15, 'cyan'))
        print ("")
        time.sleep(1)

    print ("")
    levelEnd1()
    pCurrentLevel += 1
    print ("")

def levelStart():
    global pCurrentLevel, pGoldCoins, pUltraCoins, enemy, enemyhp
    if pCurrentLevel == 1:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = Zombie
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = Skeleton
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = WereWolf
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

    elif pCurrentLevel == 2:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = Skeleton
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = Ogre
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = WereWolf
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    elif pCurrentLevel == 3:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")
        staggeredText(0.05, colored("The Juggernaut approaches!", 'red'))
        
        enemy = TheJuggernaut
        print ("")
        enemyhp = enemy["hp"]
        while enemyhp > 0:
            playerWeaponChoose()
            playerMoveChoose()
            playerDMG()
            cpuMove()
            endMove()
            if enemyhp <= 0:
                pUltraCoins += enemy["coins"]
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pUltraCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

    elif pCurrentLevel == 4:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))

        enemy = Ogre
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = WereWolf
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = ShadowArcher
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")   

            elif enemyhp == -999:
                print ("")    


    elif pCurrentLevel == 5:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = Ogre
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = Golem
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
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = ShadowArcher
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

    elif pCurrentLevel == 6:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")
        staggeredText(0.05, colored("The Frost Giant approaches!", 'red'))
        enemy = TheFrostGiant
        print ("")
        enemyhp = enemy["hp"]
        while enemyhp > 0:
            playerWeaponChoose()
            playerMoveChoose()
            playerDMG()
            cpuMove()
            endMove()
            if enemyhp <= 0:
                pUltraCoins += enemy["coins"]
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pUltraCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    elif pCurrentLevel == 7:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = ShadowArcher
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = Golem
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = Yeti
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    elif pCurrentLevel == 8:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = Golem
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = ShadowArcher
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = Yeti
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    elif pCurrentLevel == 9:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))

        print ("")
        staggeredText(0.05, colored("The Leviathan approaches!", 'red'))
        enemy = TheLeviathan
        print ("")
        enemyhp = enemy["hp"]
        while enemyhp > 0:
            playerWeaponChoose()
            playerMoveChoose()
            playerDMG()
            cpuMove()
            endMove()
            if enemyhp <= 0:
                pUltraCoins += enemy["coins"]
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pUltraCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

    elif pCurrentLevel == 10:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = Golem
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = Yeti
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = DarkKnight
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

                

    elif pCurrentLevel == 11:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        print ("")

        enemy = Yeti
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = DarkKnight
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = MagmaElemantal
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")




    elif pCurrentLevel == 12:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))

        print ("")
        staggeredText(0.05, colored("The Dragon King approaches!", 'red'))
        enemy = TheDragonKing
        print ("")
        enemyhp = enemy["hp"]
        while enemyhp > 0:
            playerWeaponChoose()
            playerMoveChoose()
            playerDMG()
            cpuMove()
            endMove()
            if enemyhp <= 0:
                pUltraCoins += enemy["coins"]
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pUltraCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    elif pCurrentLevel == 13:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))


        enemy = DarkKnight
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = MagmaElemantal
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = Necromancer
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    elif pCurrentLevel == 14:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))

        enemy = MagmaElemantal
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")

        enemy = Necromancer
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


        enemy = PhantomKnight
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
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pGoldCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")


    

    elif pCurrentLevel == 15:
        staggeredText(0.05, colored("Starting Level " + str(pCurrentLevel), 'blue'))
        
        print ("")
        staggeredText(0.05, colored("The Overseer approaches!", 'red'))
        enemy = TheOverseer
        print ("")
        enemyhp = enemy["hp"]
        while enemyhp > 0:
            playerWeaponChoose()
            playerMoveChoose()
            playerDMG()
            cpuMove()
            endMove()
            if enemyhp <= 0:
                pUltraCoins += enemy["coins"]
                staggeredText(0.025, colored("You defeated the " + enemy["name"] + " and received " + str(enemy["coins"]) + " ultra coins" + " you now have " + str(pUltraCoins) +  " ultra coins!", 'magenta'))
                print ("")
                print ("--------------------------------------------------------------------------------------------------------------")
                print ("")

            elif enemyhp == -999:
                print ("")




#NewGame
def newGame():
    global pGoldCoins, pUltraCoins, pWeapons, pMoveSet, playerStats, pCurrentLevel
    print ("")
    startNewGame = input("Would you like to start a new game " + colored('yes', 'green') + " or no " + colored("no", 'red') + ":")

    if startNewGame.lower() == 'yes':
        pGoldCoins = 0
        pUltraCoins = 0
        pWeapons.clear()
        pWeapons.append(WoodenStick)
        pWeapons.append(WaterGun)
        pMoveSet.clear()
        pMoveSet.append(LightAttack)
        pMoveSet.append(MediumAttack)
        print ("")
        staggeredText(0.05, colored("Welcome to Water Defence", 'blue'))

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

        if character == "jabbari":
            playerStats = jabbariStats
        elif character == "mark":
            playerStats = markStats
        elif character == "justin":
            playerStats = justinStats

        print ("")
        print (colored("Here are your base starting stats " + character, 'blue'))
        print ("")
        print (colored(playerStats, 'green'))
        time.sleep(1)
        print ("")
        print ("")
        
        while pCurrentLevel <= 15 or waterPillarHp > 0:
            if waterPillarHp <= 0:
                print ("")
                staggeredText(0.05, colored("The Water Pillar has been destroyed!", 'red'))
                print ("")
                staggeredText(0.05, colored("You made it to level " + pCurrentLevel, 'green'))
                print ("")
                time.sleep(1)
                print (colored("I hope you use the info you have learned about water pollution to help fix this problem", 'blue'))
                print ("")
                print ("Cya later and I hope to see you come back next time!")
                exit()

            elif pCurrentLevel == 16:
                staggeredText(0.05, colored("Congratulations, you have beat Water Defence!", 'green'))
                print ("")
                print (colored("I hope you use the info you have learned about water pollution to help fix this problem", 'blue'))
                print ("")
                print ("Cya later and I hope to see you come back next time!")
                exit()
                
            else:
                levelStart()
                playerStats['hp'] = playerStats['bhp']
                levelEnd()



            

    elif startNewGame.lower() == 'no':
        print ("Thats too bad, cya next time!")
        exit()
    else:
        print(colored('That is not an option. Try again.', 'red'))
        newGame()



print ("")
staggeredText(0.05, colored("What difficulty would you like to play on", 'yellow'))


table = [["Meant for Beginners", "Challenging Difficulty", "Only if you are Pro", "For the true Gamers", "Infinite Gold and Ultra Coins"], ["Easy and Fun to play", "For the average Joe", "Very Difficult", "No Comment Needed", "Max Stats and Pillar Hp"]] 
headers = [colored("1. Easy", 'green'), colored("2. Medium", 'blue'), colored("3. Hard", 'red'), colored("4. Gamer", 'magenta'), colored("5. Creative", 'cyan')]
print(tabulate(table, headers, tablefmt="psql"))
print ("")

difficultyLoop = 0
while difficultyLoop == 0:
    staggeredText(0.05, "Type '1' for Easy, '2' for Medium, '3' for Hard, '4' for Gamer, or '5' for Creative")
    difficultyDecide = input(colored("What difficulty would you like to play on\n"))
    if difficultyDecide == "1":
        difficultyLoop = 1
        print ("")
        staggeredText(0.05, colored("You are now on easy difficulty", 'green'))
        print ("")

        #ENEMIES

        Zombie = {"atk": 15, "def": 20, "hp": 100, "acc": 85, "name": "Zombie", "coins": 15}
        Skeleton = {"atk": 20, "def": 10, "hp": 100, "acc": 80, "name": "Skeleton", "coins": 20}
        WereWolf = {"atk": 25, "def": 5, "hp": 120, "acc": 90, "name": "Were Wolf", "coins": 20}
        Ogre = {"atk": 25, "def": 5, "hp": 150, "acc": 80, "name": "Ogre", "coins": 30}
        ShadowArcher = {"atk": 35, "def": 5, "hp": 90, "acc": 90, "name": "Shadow Archer", "coins": 25}
        Golem = {"atk": 30, "def": 40, "hp": 200, "acc": 75, "name": "Golem", "coins": 30}
        Yeti = {"atk": 40, "def": 20, "hp": 150, "acc": 80, "name": "Yeti", "coins": 40}
        DarkKnight = {"atk": 55, "def": 30, "hp": 180, "acc": 90, "name": "Dark Knight", "coins": 50}
        MagmaElemantal = {"atk": 50, "def": 50, "hp": 250, "acc": 80, "name": "Magma Elemental", "coins": 65}
        Necromancer = {"atk": 75, "def": 25, "hp": 150, "acc": 90, "name": "Necromancer", "coins": 85}
        PhantomKnight = {"atk": 85, "def": 45, "hp": 250, "acc": 90, "name": "Phantom Knight", "coins": 100}


        #Bosses

        TheJuggernaut = {"atk": 35, "def": 35, "hp": 150, "acc": 75, "name": "The Juggernaut", "coins": 30}
        TheFrostGiant = {"atk": 50, "def": 40, "hp": 250, "acc": 75, "name": "The Frost Giant", "coins": 45}
        TheLeviathan = {"atk": 75, "def": 50, "hp": 350, "acc": 75, "name": "The Leviathan", "coins": 60}
        TheDragonKing = {"atk": 100, "def": 60, "hp": 450, "acc": 75, "name": "The Dragon King", "coins": 80}
        TheOverseer = {"atk": 130, "def": 75, "hp": 600, "acc": 75, "name": "The Overseer", "coins": 100}

        break



    elif difficultyDecide == "2":
        difficultyLoop = 1
        print ("")
        staggeredText(0.05, colored("You are now on medium difficulty", 'blue'))
        print ("")

        #ENEMIES

        Zombie = {"atk": 17, "def": 25, "hp": 110, "acc": 85, "name": "Zombie", "coins": 15}
        Skeleton = {"atk": 23, "def": 13, "hp": 110, "acc": 80, "name": "Skeleton", "coins": 20}
        WereWolf = {"atk": 30, "def": 8, "hp": 135, "acc": 90, "name": "Were Wolf", "coins": 20}
        Ogre = {"atk": 30, "def": 8, "hp": 165, "acc": 80, "name": "Ogre", "coins": 30}
        ShadowArcher = {"atk": 40, "def": 8, "hp": 100, "acc": 90, "name": "Shadow Archer", "coins": 25}
        Golem = {"atk": 38, "def": 50, "hp": 220, "acc": 75, "name": "Golem", "coins": 30}
        Yeti = {"atk": 45, "def": 25, "hp": 170, "acc": 80, "name": "Yeti", "coins": 40}
        DarkKnight = {"atk": 65, "def": 35, "hp": 200, "acc": 90, "name": "Dark Knight", "coins": 50}
        MagmaElemantal = {"atk": 55, "def": 60, "hp": 270, "acc": 80, "name": "Magma Elemental", "coins": 65}
        Necromancer = {"atk": 80, "def": 30, "hp": 160, "acc": 90, "name": "Necromancer", "coins": 85}
        PhantomKnight = {"atk": 95, "def": 55, "hp": 270, "acc": 90, "name": "Phantom Knight", "coins": 100}


        #Bosses

        TheJuggernaut = {"atk": 40, "def": 40, "hp": 160, "acc": 75, "name": "The Juggernaut", "coins": 30}
        TheFrostGiant = {"atk": 60, "def": 50, "hp": 270, "acc": 75, "name": "The Frost Giant", "coins": 45}
        TheLeviathan = {"atk": 85, "def": 60, "hp": 380, "acc": 75, "name": "The Leviathan", "coins": 60}
        TheDragonKing = {"atk": 110, "def": 70, "hp": 490, "acc": 75, "name": "The Dragon King", "coins": 80}
        TheOverseer = {"atk": 140, "def": 85, "hp": 650, "acc": 75, "name": "The Overseer", "coins": 100}

        break

    elif difficultyDecide == "3":
        difficultyLoop = 1
        print ("")
        staggeredText(0.05, colored("You are now on hard difficulty", 'red'))
        print ("")

                #ENEMIES

        Zombie = {"atk": 20, "def": 28, "hp": 120, "acc": 85, "name": "Zombie", "coins": 15}
        Skeleton = {"atk": 25, "def": 15, "hp": 120, "acc": 80, "name": "Skeleton", "coins": 20}
        WereWolf = {"atk": 35, "def": 10, "hp": 140, "acc": 90, "name": "Were Wolf", "coins": 20}
        Ogre = {"atk": 35, "def": 10, "hp": 175, "acc": 80, "name": "Ogre", "coins": 30}
        ShadowArcher = {"atk": 45, "def": 10, "hp": 110, "acc": 90, "name": "Shadow Archer", "coins": 25}
        Golem = {"atk": 42, "def": 57, "hp": 230, "acc": 75, "name": "Golem", "coins": 30}
        Yeti = {"atk": 49, "def": 30, "hp": 180, "acc": 80, "name": "Yeti", "coins": 40}
        DarkKnight = {"atk": 69, "def": 40, "hp": 220, "acc": 90, "name": "Dark Knight", "coins": 50}
        MagmaElemantal = {"atk": 60, "def": 70, "hp": 290, "acc": 80, "name": "Magma Elemental", "coins": 65}
        Necromancer = {"atk": 87, "def": 40, "hp": 180, "acc": 90, "name": "Necromancer", "coins": 85}
        PhantomKnight = {"atk": 100, "def": 65, "hp": 290, "acc": 90, "name": "Phantom Knight", "coins": 100}


        #Bosses

        TheJuggernaut = {"atk": 50, "def": 50, "hp": 170, "acc": 75, "name": "The Juggernaut", "coins": 30}
        TheFrostGiant = {"atk": 70, "def": 60, "hp": 290, "acc": 75, "name": "The Frost Giant", "coins": 45}
        TheLeviathan = {"atk": 95, "def": 70, "hp": 400, "acc": 75, "name": "The Leviathan", "coins": 60}
        TheDragonKing = {"atk": 120, "def": 80, "hp": 520, "acc": 75, "name": "The Dragon King", "coins": 80}
        TheOverseer = {"atk": 150, "def": 90, "hp": 690, "acc": 75, "name": "The Overseer", "coins": 100}

        break

    elif difficultyDecide == "4":
        difficultyLoop = 1
        print ("")
        staggeredText(0.05, colored("You are now on gamer difficulty", 'magenta'))
        print ("")

                #ENEMIES

        Zombie = {"atk": 25, "def": 32, "hp": 130, "acc": 85, "name": "Zombie", "coins": 15}
        Skeleton = {"atk": 27, "def": 19, "hp": 130, "acc": 80, "name": "Skeleton", "coins": 20}
        WereWolf = {"atk": 38, "def": 14, "hp": 150, "acc": 90, "name": "Were Wolf", "coins": 20}
        Ogre = {"atk": 38, "def": 15, "hp": 185, "acc": 80, "name": "Ogre", "coins": 30}
        ShadowArcher = {"atk": 50, "def": 15, "hp": 120, "acc": 90, "name": "Shadow Archer", "coins": 25}
        Golem = {"atk": 48, "def": 64, "hp": 240, "acc": 75, "name": "Golem", "coins": 30}
        Yeti = {"atk": 58, "def": 40, "hp": 200, "acc": 80, "name": "Yeti", "coins": 40}
        DarkKnight = {"atk": 81, "def": 50, "hp": 230, "acc": 90, "name": "Dark Knight", "coins": 50}
        MagmaElemantal = {"atk": 70, "def": 80, "hp": 320, "acc": 80, "name": "Magma Elemental", "coins": 65}
        Necromancer = {"atk": 100, "def": 50, "hp": 220, "acc": 90, "name": "Necromancer", "coins": 85}
        PhantomKnight = {"atk": 120, "def": 70, "hp": 320, "acc": 90, "name": "Phantom Knight", "coins": 100}


        #Bosses

        TheJuggernaut = {"atk": 60, "def": 60, "hp": 180, "acc": 75, "name": "The Juggernaut", "coins": 30}
        TheFrostGiant = {"atk": 80, "def": 70, "hp": 300, "acc": 75, "name": "The Frost Giant", "coins": 45}
        TheLeviathan = {"atk": 105, "def": 80, "hp": 420, "acc": 75, "name": "The Leviathan", "coins": 60}
        TheDragonKing = {"atk": 130, "def": 90, "hp": 580, "acc": 75, "name": "The Dragon King", "coins": 80}
        TheOverseer = {"atk": 160, "def": 100, "hp": 810, "acc": 75, "name": "The Overseer", "coins": 100}

        break

    elif difficultyDecide == "5":
        difficultyLoop = 1
        print ("")
        staggeredText(0.05, colored("You are now in creative mode", 'cyan'))
        print ("")
        pGoldCoins = 1000000000000000000000000000000000000000000000000000000
        pUltraCoins = 1000000000000000000000000000000000000000000000000000000
        waterPilarHp = 10000000000000000000000000000000000000000000000000000
        jabbariStats = {
	        "hp": 500, 
            "bhp": 500,
	        "atk": 500, 
	        "def": 500
        }
        markStats = {
	        "hp": 500, 
            "bhp": 500,
	        "atk": 500, 
	        "def": 500
        }
        justinStats = {
	        "hp": 500, 
            "bhp": 500,
	        "atk": 500, 
	        "def": 500
        }

        break

    else:
        staggeredText(0.05, colored("That is not an option", 'red'))




playTutorial = 0
while playTutorial == 0:
    print ("")
    tutorialPlay = input("Would you like to play the tutorial " + colored('yes', 'green') + " or no " + colored("no", 'red') + ":")
    if tutorialPlay == "yes" or tutorialPlay == "Yes":
        tutorial()
        playTutorial = 1 
        break
    elif tutorialPlay == "no" or tutorialPlay == "No":
        playTutorial = 1
        newGame()
        break
    else:
        print ("That is not a valid option, please type either yes or no")
        playTutorial = 0
