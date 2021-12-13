import random
from random import randint
import time
from termcolor import colored

# print colored('text', 'color of text')
import colorama
from colorama import Fore, Style

score = 0
goldCoins = 0
utlraCoins = 0
waterBottleHp = 100000
jabbariStats = {
	"hp": 100, 
	"atk": 115, 
	"def": 5
}
markStats = {
	"hp": 120, 
	"atk": 10, 
	"def": 5
}
justinStats = {
	"hp": 80, 
	"atk": 20, 
	"def": 5
}

#weapons
WaterGun = {"Name": "Water Gun", "DMG": 15, "ACC": 60}
WoodenStick = {"Name": "Wooden Stick" ,"DMG": 5, "ACC": 70}


#playerweapons
pWeapons = [WaterGun, WoodenStick]


#moves
LightAttack = {"Name": "Light Attck", "DMG": 10, "ACC": 30}
MediumAttack = {"Name": "Medium Atack", "DMG": 15, "ACC": 20}


#playermoves
pMoveSet = [LightAttack, MediumAttack]


#ENEMIES

Zombie = {"atk": 7, "def": 20, "hp": 100, "acc": 85, "name": "Zombie"}
Skeleton = {"atk": 12, "def": 10, "hp": 100, "acc": 80, "name": "Skeleton"}

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
staggeredText(0.003, " ____      ____      __                                       _            ____      ____      _                   ______              ___                               ")
staggeredText(0.003, "|_  _|    |_  _|    [  |                                     / |_         |_  _|    |_  _|    / |_                |_   _ `.          .' ..]                              ")
staggeredText(0.003, "  \ \  /\  / /.---.  | |  .---.   .--.   _ .--..--.  .---.  `| |-' .--.     \ \  /\  / /,--. `| |-'.---.  _ .--.    | | `. \ .---.  _| |_  .---.  _ .--.   .---.  .---.  ")
staggeredText(0.003, "   \ \/  \/ // /__\\ | | / /'`\]/ .'`\ \[ `.-. .-. |/ /__\\  | | / .'`\ \    \ \/  \/ /`'_\ : | | / /__\\[ `/'`\]   | |  | |/ /__\\'-| |-'/ /__\\[ `.-. | / /'`\]/ /__\\ ")
staggeredText(0.003, "    \  /\  / | \__., | | | \__. | \__. | | | | | | || \__.,  | |,| \__. |     \  /\  / // | |,| |,| \__., | |      _| |_.' /| \__.,  | |  | \__., | | | | | \__. | \__., ")
staggeredText(0.003, "     \/  \/   '.__.'[___]'.___.' '.__.' [___||__||__]'.__.'  \__/ '.__.'       \/  \/  \'-;__/\__/ '.__.'[___]    |______.'  '.__.' [___]  '.__.'[___||__]'.___.' '.__.' ")
print ("")

characterPlay = 0
while characterPlay == 0:
	character = input("Who would you like to play as?, 'Jabbari', his friend 'Mark', or his sister 'Justin'\n").lower()
	if character == "jabbari":
		print ("Hello Jabbari!")
		characterPlay == 1
		break
	elif character == "justin":
		print ("Hello Justin!")
		characterPlay == 1
		break
	elif character == "mark":
		print ("Hello Mark!")
		characterPlay == 1
		break
	else:
		print ("Please either type 'Jabbari', 'Justin', or 'Mark'\n")

time.sleep(1)
score = 0
goldCoins = 0
utlraCoins = 0
waterBottleHp = 100000
jabbariStats = {
	"hp": 100, 
	"atk": 20, 
	"def": 5
}
markStats = {
	"hp": 120, 
	"atk": 15, 
	"def": 5
}
justinStats = {
	"hp": 80, 
	"atk": 25, 
	"def": 5
}

if character == "jabbari":
	playerStats = jabbariStats
elif character == "mark":
	playerStats = markStats
elif character == "justin":
	playerStats = justinStats

playerhp = playerStats["hp"]
print ("")
print ("Here are your base starting stats", character)
print ("")
print (playerStats)
time.sleep(2)
print("")
playerhp = playerStats["hp"]


#PlayerWeaponChoose
def playerWeaponChoose():
    global pCurrentWeapon
    print('Your weapons: ', end='')
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
    print("You are now using", colored(pCurrentWeapon['Name'], 'blue'))
    print ("")
    
#PlayerMoveChoose
def playerMoveChoose():
    global pCurrentMove
    print ('Your Moves: ', end='')
    incrementStage = 0
    pCurrentMove = 0
    for i in pMoveSet:
        print (f'{incrementStage + 1}. {i["Name"]}, ', end='')
        incrementStage += 1
    pCurrentMoveInput = input('Type the number of the mvoe you want to use.\n')
    try:
        pCurrentMove = int(pCurrentMoveInput)
    except:
        print (colored('That is not an number. Try again.', 'red'))
        return playerMoveChoose()

    if pCurrentMove > len(pMoveSet):
        print (colored('That is not an option. Try again', 'red'))
        return playerMoveChoose()

    pCurrentMove = pMoveSet[pCurrentMove -1]
    print ("You are now using", colored(pCurrentMove['Name'], 'blue'))
    print ("")

#PlayerDamage
def playerDMG():
    global pCurrentWeapon, pCurrentMove
    dmg = pCurrentWeapon["DMG"] + playerStats["atk"] + pCurrentMove["DMG"] - enemy["def"]
    if dmg < 0:
        dmg = 0
    hitchance = pCurrentMove["ACC"] + pCurrentWeapon["ACC"]
    if randint(1, 100) <= hitchance:
        enemyhp =+ dmg
        print ("You hit", colored(enemy["name"], 'yellow'), "for", colored(dmg, 'red'), "damage!")
        print ("You are now at", colored(playerhp, 'green'), "hp, the", colored(enemy["name"], 'yellow'), "is now at", colored(enemyhp, 'red'), "hp")
        print ("")
    else:
        print (colored('You missed...', 'blue'))
        print ("")

#CPUMove
def cpuMove():
    global playerhp
    dmg = enemy["atk"] - playerStats["def"]
    if dmg < 0:
        dmg = 0
    if randint(1,100) <= enemy["acc"]:
        playerhp -= dmg
        print ("")
        print("The", colored(enemy["name"], 'yellow'), "hit you for", colored(dmg, 'red'), "damage." '''
You are now at''', colored(playerhp, 'green'), "hp, the", colored(enemy["name"], 'yellow'), "is now at", colored(enemyhp, 'red'), "hp")
        print ("")
    else:
        print ("")
        print(colored('The opponent missed...', 'blue'))
        print ("")


#Tutorial       
def tutorial():
    print ("Hello there, this is the tutorial, it will teach you how to play the game")
    print ("")
    print (colored("First you must learn how to defend the pillar from attacking monsters", 'cyan'))




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
    tutorialPlay = input("Would you like to play the tutorial, yes or no?\n")
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







while playerhp > 0:
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

