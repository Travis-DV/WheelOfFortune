#Libs
import random as r, colorama as c, time as t

c.init()

#all posible phrases
phrases = ['The best of both worlds', 'Speak of the devil', 'See eye to eye', 'Once in a blue moon', 'When pigs fly', 'To cost an arm and a leg', 'A piece of cake', 'Let the cat out of the bag', 'To feel under the weather', 'To kill two birds with one stone', 'To cut corners', 'To add insult to injury', 'You can\'t judge a book by its cover', 'Break a leg', 'To hit the nail on the head', 'A blessing in disguise', 'Call it a day', 'Let someone off the hook', 'No pain no gain', 'Bite the bullet', 'Getting a taste of your own medicine', 'Giving someone the cold shoulder', 'The last straw', 'The elephant in the room', 'Stealing someones thunder']
players = [] #Where the players made in the class will be stored
guessedlet = [" ", ",", "'", ] #Where all guessed letters will be stored
cplayer = 0

class player: #Where the players are made

    def __init__(self, dict):
        #All pos names
        self.names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Elijah', 'characterlotte', 'William', 'Sophia', 'James', 'Amelia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn', 'Alexander', 'Harper', 'Travis', 'Frank']
        #if the player did not add any name or age
        if dict == {}:
            #make one
            self.character = {
                        'name': r.choice(self.names), #get a random name
                        'age': r.randint(13,72), #random age
                        'score': 0, #Set the score to 0
                        'pc': False #and that it is an AI
                        }
        elif dict != {}: #If they did have something
            self.character = {
                        'name': dict['name'], #Set the name to what they inputed
                        'age': dict['age'], #Set the age to their input
                        'score': 0, #Set score to 0
                        'pc': True #and set that it is a player controled characterictor
                        }
        if self.character['name'] == 'Frank': #If the dumb dumb named themself Frank he diserves no points
            self.character['score'] = -1000000000
        elif self.character['name'] == 'Travis': #If the god is named Travis
            self.character['score'] = 1000000000000000000000000000000000000000000 #Then all the points

    def printstuff(self):
        #print the name their score and if they are player controled
        print(f"{self.character['name']}, {self.character['age']}: With {self.character['score']} points. Player Controled: {self.character['pc']}")

    def pointchange(self, input): #A point changing deff
        self.character['score'] += input #Changing it whatever is needed

def playersetup(players, player): #Fuction to set up players
    setup = True
    while setup and len(players) < 3:
        dict = {'name': "", 'age': 0} #set the dictionary to start
        #Ask if they want to set up a player
        userinp = str.lower(input("Do you want to set up a player? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
        if userinp == "y": #If they do
            while True:
                inp = input("What is their name?\n") #Get the name they want
                if inp == "": #if there name is empty
                    print("Please put a name") #make them add a name
                elif inp != "":
                    dict['name'] = inp #Setting there name
                    if not inp.isalpha(): #If there is anything that is not a number
                        print("Intoresting name!") #coment on the intoresting name
                    break
            while True:
                inp = input("How old are they?\n") #get the age they want
                if not inp.isalpha(): #Make sure it is a number
                    if int(inp) > 0:
                        dict['age'] = int(inp)#Seting the age part of the dict to an int
                        if int(inp) > 90: #If they are old
                            print("You old fart sure you want to play this game?") #Tell them
                        elif int(inp) < 15: #If young
                            print("Ya ankle biter sure you want to be here?") #Tell them
                    else: print("\033[1;31mMake that age over 0\033[1;0m") #If no age make them input one
                    players.append(player(dict)) #Getting a player
                    players[-1].printstuff()
                    break
                elif inp.isalpha(): #If it is not a number
                    if inp == "yo mama": #If they make there age yo mama
                        dict['age'] = 1000000000000000000000000000000000 #Make them soooooooooooooo old
                    else: print("\033[1;31mPlease put their age as a number.\033[1;0m") #Through an error
        elif userinp == "n": #if they dont then kick out of the loop
            setup = False
        else: print("\033[1;31mError, try inputing again\033[1;0m") #If they didn't do a y or n then print an error
    for i in range(len(players),3): #if they kicked out before making 3 moves then
        players.append(player({})) #make as meny as needed
playersetup(players, player)

def prcph(guessed, cphr, person): #print the cypher
    playing = False
    for i in cphr:
        if i not in guessed: #If it is not guessed
            cphr = cphr.replace(i, "_") #c.Fore.WHITE + c.Back.WHITE + i + c.Fore.RESET + c.Back.RESET
            playing = True
        elif guessed != [] and i != " " and i != "'" and i == guessed[-1]: #If it is the newest guessed
            cphr = cphr.replace(i, c.Back.GREEN + i + c.Back.RESET) #Make it green so the player knows
    if not playing:
        person.pointchange(5000) #if it is done add points
    print(cphr) #Print it
    return playing

def newplayer(index): #The player index loop
    if index == 2: return 0 #If it is on the last player set index to 0
    elif index < 2: return index + 1 #else return the index +1

def countlet(cphr, guessed): #counting how many letters there are in word
    count = 0
    for i in cphr: #For everything in the word
        if i == guessed: count += 1 #if it is the guessed then incroment guessed
    print(f"There is {count} '{guessed}'(s) in the puzzle.") #print how many there are
    return count

def pickalet(type, guessedlet, cphr, player): #Picking let function for both vowels and constanents
    lettertypes = [list('euioa'), list('qwrtypsdfghjklzxcvbnm')] #all the constanents
    if type == 'vowel': #if it is the vowel
        plist = lettertypes[0] #Set the list to the first set 0f lets
    elif type == 'consonant': #if you need a consonant
        plist = lettertypes[1] #set the list to the second one
    else: print("\033[1;31mIncompatable letter type\033[1;0m") #Else print error
    while True:
        #print(plist)
        newp = False; count = 0
        if player.character['pc']: inp = str.lower(input(f"What {type} do you want?\n")) #If it is a player get their input
        elif not player.character['pc']: inp = r.choice(plist) #If ai get random
        if inp in plist and inp not in guessedlet: #If it is not in guessed and is in the possible letters
            guessedlet.append(inp) #add it to guessed
            if inp in cphr: #if it is in the cphr
                newp = False
                count = countlet(cphr, guessedlet[-1]) #then count
            elif inp not in cphr: #if not
                newp = True #You need a new player
                print(f"There are no '{inp}'(s)") #tell the player
            return guessedlet, newp, count
        elif inp not in plist: #If it is not a possible let
            print(f"Please do a {type}") #Tell them to get a correct let
        elif inp in guessedlet: #if guessed
            print("You already guessed that") #Tell player

def wheelspin(player, guessedlet, cphr): #The wheel spin stuff
    wheel = ['Lose a Turn', 800, 500, 650, 500, 900, 'Bankrupt', 5000, 500, 600, 700, 600, 650, 500, 700, 500, 600, 550, 500, 600, 'Bankrupt', 650, 700, 'Lose a Turn']
    rest = 0.01; newp = False
    while rest < 0.7:
        landon = r.choice(wheel) #Get a random choice
        print(landon, "\033[?25l                    ", end = "\r") #Print landed on remove curser and remove preveus line
        t.sleep(rest) #rest for how ever long
        rest *= 1.1 #make rest longer
    print('\033[?25h') #add curser
    if type(landon) == int:
        guessedlet, newp, count = pickalet('consonant', guessedlet, cphr, player) #Pick a let
        player.pointchange(int(landon)*int(count)) #How ever many of that let*there points
    if landon == 'Lose a Turn': #If they lost a turn then get a new player
        newp = True
    elif landon == 'Bankrupt': #if they went bankrupt
        player.character['score'] = 0 #Set there score to 0
    return guessedlet, newp, player

def bavowel (player, guessedlet, cphr): #Buying a vowel
    newp = False
    for i in list('euioa'): #for every vowel
        if i in guessedlet: #if it is in guessed
            done = True #Done still equals true
        else:
            done = False #if there is one let that isnt then done equals false and break
            break
    if done:
        print("There are no more vowels to buy") #if done then tell player
    else:
        guessedlet, newp, count = pickalet('vowel', guessedlet, cphr, player) #Get a let
        player.pointchange(-200) #Remove 200 points
        player.printstuff() #print the players stuff
    return guessedlet, newp, player

def solving(player, cphr): #Solving the puzzle
    playing = True; newp = False
    if player.character['pc']: #If it is a player
        inp = str.lower(input("What do you think the phrase is?\n")) #Get what they think the cphyer is
        if inp == str.lower(cphr): #if there input is the cphyer
            playing = False #they are no longer playing
            player.pointchange(5000) #Add 5k points
        else:
            print("That is not what the cypher is.") #if it isnt tell them
            newp = True #get new player
    elif not player.character['pc']: #If it is ai
        count = countlet(cphr, "_") #Get how many unknown lets there are
        if count < 3: #if it is less then 3
            playing = False #no longer playign
            player.printstuff() #print the cpther
            print(f"Guessed the prase, they guessed {cphr}") #Tell player
    return player, playing, newp

cphr = str.lower(r.choice(phrases)) #get the starting cphr
playing = prcph(guessedlet, cphr, players[0]) #get playing and print the cphyer
while playing:
    newp = False
    #If it is a player get what they want to do
    if players[cplayer].character['pc']: choice = str.lower(input(f"Does {players[cplayer].character['name']} want to\n(1) Spin the Wheel,\n(2) Buy a Vowel,\n(3) Solve the puzzle,\n(4) See Stats and Stuff\n "))
    #If AI do random thing
    elif not players[cplayer].character['pc']: choice = str(r.randint(1,3))
    #If it is a 1 then do wheel spin
    if choice == "1": guessedlet, newp, players[cplayer] = wheelspin(players[cplayer], guessedlet, cphr)
    #if buy vowel
    elif choice == "2":
        #Buy the vowel as long as they have more then 200 points
        if players[cplayer].character['score'] > 200: guessedlet, newp, players[cplayer] = bavowel (players[cplayer], guessedlet, cphr)
        #If they dont tell player
        elif players[cplayer].character['score'] < 200: print("You need more the 200 points.")
    #If solve do that
    elif choice == "3": players[cplayer], playing, newp = solving(players[cplayer], cphr)
    #If want stats
    elif choice == "4":
        print(str(guessedlet)) #print guessed lets
        for i in players: i.printstuff() #print the player sats for everyone
    elif choice == "show": #If haxs
        print(cphr) #Print the cphyer
    else: print("\033[1;31mError, try inputing again\033[1;0m") #if not any of thoughs then error
    if newp: cplayer = newplayer(cplayer) #If new player needed then get that
    if playing: playing = prcph(guessedlet, cphr, players[cplayer]) #if they are playing print cphyer
    elif not playing: #if not playing
        top = [0, 'name']
        for i in players: #For everyone
            if i.character['score'] > top[0]: #Find highest score
                top[0] = i.character['score'] #do set it
                top[1] = i #set there name
            elif i.character['score'] > 0 and i.character['score'] == top[0]: #If tie
                top[1] = [top[1], i]
        if type(top[1]) == list: #if there is a tie
            people = []
            for i in top[1]: #Get the people
                people.append(i.character['name']) #add the name
            print(f"There was a tie between {str(people)} with {top[0]} points") #print who had a tie
        else:
            print(f"{top[1].character['name']} Won the game with {top[0]} points") #If no tie print winner
        #ask if play again
        userinp = str.lower(input("Do you want to play again? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
        if userinp == "y": #if they do
            players = [] #Where the players made in the class will be stored
            guessedlet = [] #Where all guessed letters will be stored
            cplayer = 0
            cphr = r.choice(phrases) #get new phrase
            playing = prcph(guessedlet, cphr, cplayer) #print it
        elif userinp == "n": #if not
            print("Ok bye have fun, with out me :(") #be sad
    t.sleep(0.5) #make slower