import random
import time

# Variables (ORDER MATTERS!)
hp = 100.0
saturation = 100.0
money = 20.0
sanity = 100.0
gradePoints = 100.0
popularity = 100.0

# Functions
def waitForString(string):
    temp1 = input()
    if temp1.lower() == str(string):
        return
    else:
        waitForString(string)


def sayAndWait(text, length):
    print(text)
    time.sleep(length)


def viewVariables():
    print("\n- Variables -\n")
    print(f"HP: {hp}")
    print(f"Saturation: {saturation}")
    print(f"Money: {money}")
    print(f"Sanity: {sanity}")
    print(f"Grade Points: {gradePoints}")
    print(f"Popularity: {popularity}")


def save():
    variableNames = [hp, saturation, money, sanity, gradePoints, popularity]
    individualCodes = []
    saveCode = ""

    for variable in variableNames:
        saveCode += f"{variable * 361.3};"
    saveCode += "+"
    
    # Print the savecode out
    print("Copy this savecode and paste it somewhere safe.")
    print(saveCode)
    print('\nType "done" when you\'re done.')
    waitForString("done")


def load():
    global hp
    global saturation
    global money
    global santiy
    global gradePoints
    global popularity

    thingToLoad = input("What do you want to load?\n")
    
    chars = []


    i = 0
    iValue = ""
    temp = 0
    
    for ltr in thingToLoad:
        chars.append(ltr)


    while chars[i] != ";":
        iValue += chars[i]

        i += 1

    temp = float(iValue) / 361.3
    hp = temp

    # Next variable

    temp = 0
    i += 1
    iValue = ""

    while chars[i] != ";":
        iValue += chars[i]

        i += 1

    temp = float(iValue) / 361.3
    saturation = temp

    # Next variable

    i += 1
    iValue = ""
    temp = 0
    
    for ltr in thingToLoad:
        chars.append(ltr)


    while chars[i] != ";":
        iValue += chars[i]

        i += 1

    temp = float(iValue) / 361.3
    money = temp

    # Next variable

    temp = 0
    i += 1
    iValue = ""

    while chars[i] != ";":
        iValue += chars[i]

        i += 1

    temp = float(iValue) / 361.3
    santiy = temp

    # Next variable

    temp = 0
    i += 1
    iValue = ""

    while chars[i] != ";":
        iValue += chars[i]

        print(i)
        i += 1

    temp = float(iValue) / 361.3
    gradePoints = temp


    # Next variable

    temp = 0
    i += 1
    iValue = ""

    while chars[i] != ";":
        iValue += chars[i]

        print(i)
        i += 1

    temp = float(iValue) / 361.3
    popularity = temp


    # Done
    print("Done loading!")


def saveOrLoad():
    print("What do you want to do?")
    print('Enter "save", "load", or "continue". (Anything else won\'t work.)')
    temp2 = input()

    while temp2.lower() not in ["save", "load", "continue"]:
        temp2 = input()
    if temp2.lower() == "save":
        save()
    if temp2.lower() == "load":
        load()
    


# Instructions
instructionTexts = ["\n- Asian Life Squared -", "Welcome to Asian Life Squared!", "This is a game similar to Asian Life TBG.", "In fact, it's very similar.", "It's text based, so all you do is type.", "Read the readme file for a little more info.", "(You may need to scroll up.)"]

for i in instructionTexts:
    print(i)
    time.sleep(0)

print()
time.sleep(.125)

print('Type "done" to continue.')
waitForString("done")

# Save or load thing at beginning idk
saveOrLoad()

viewVariables()

print("-")


# REAL GAME STARTING WHOOOOOOOOOOOOOOO

# EVENT 1

print('''
    --------
    EVENT 1
    --------
''')
print("You start of the day buy going to school.")
print("How would you get there? (walk; bus)")

tempInput = input().lower()

while tempInput not in ["walk", "bus"]:
    tempInput = input().lower()

if tempInput == "walk":
    sayAndWait("You walk to school.", 1)
    
    if random.randint(1, 3) == 1:
        sayAndWait("It takes you a long time and you are late.", 1)
        sayAndWait("The teacher yells at you for being late.", 1)
        sayAndWait("-5 Sanity", 1)
        sanity -= 5
        sayAndWait("Your teacher is also mad and lowers your grade by a bit.", 1)
        sayAndWait("-2 Grade Points", 1)
        gradePoints -= 2

        if random.randint(1, 2) == 1:
            sayAndWait("But, you have your homies and get more popular.", 1)
            sayAndWait("+5 Popularity", 1)
            popularity += 5
            sayAndWait("+5 Sanity", 1)
            sanity += 5
        else:
            sayAndWait("You have no friends, and everyone laughs at you.", 1)
            sayAndWait("-3 Sanity", 1)
            sanity -= 3
            sayAndWait("-5 Popularity", 1)
            popularity -= 5

    else:
        sayAndWait("You get to school on time.", 1)
        if random.randint(1, 4) == 1:
            sayAndWait("People laugh at you for being too early for some reason.", 1)
            sayAndWait("-5 Sanity", 1)
            sanity -= 5
            sayAndWait("-3 Popularity", 1)
            popularity -= 3
        else:
            sayAndWait("You feel normal.", 1)
            sayAndWait("Nothing bad is happening.", 1)

else:
    sayAndWait("You take the bus to school.", 0.5)
    if random.randint(1, 3) == 1:
        sayAndWait("However, the bus is late, and you are late for school.", 1)
        sayAndWait("You still get to school, though.", 1)
        sayAndWait("-5 Sanity", 1)
        sanity -= 5
        sayAndWait("Your teacher also lowers your grade by a bit.", 1)
        sayAndWait("-2 Grade Points", 1)
        gradePoints -= 2
    else:
        sayAndWait("You get to school on time, with the bus.", 1)
        sayAndWait("You still have to pay, though.", 1)
        sayAndWait("-2 Money", 1)
        money -= 2

sayAndWait("You are now at school.", 1)


# Between event 1 and 2

sayAndWait("-", 0.25)

print('Do you want to view variables? (Type "yes" if you do; anything else if you don\'t.)')
tempInput = input().lower()

if tempInput == "yes":
    viewVariables()