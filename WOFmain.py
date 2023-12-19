#Libs
import random, colorama as c, time as t

c.init()

phrases = ['The best of both worlds', 'Speak of the devil', 'See eye to eye', 'Once in a blue moon', 'When pigs fly', 'To cost an arm and a leg', 'A piece of cake', 'Let the cat out of the bag', 'To feel under the weather', 'To kill two birds with one stone', 'To cut corners', 'To add insult to injury', 'You can\'t judge a book by its cover', 'Break a leg', 'To hit the nail on the head', 'A blessing in disguise', 'Call it a day', 'Let someone off the hook', 'No pain no gain', 'Bite the bullet', 'Getting a taste of your own medicine', 'Giving someone the cold shoulder', 'The last straw', 'The elephant in the room', 'Stealing someones thunder']
players = []
guessed_letters = [" ", ",", "'", ]
current_player = 0

class player:

    def __init__(self, given_dict):
        if given_dict == {}:
            self.character = {
                        'name': random.choice(['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Elijah', 'Characterlotte', 'William', 'Sophia', 'James', 'Amelia', 'Benjamin', 'Isabella', 'Lucas', 'Mia', 'Henry', 'Evelyn', 'Alexander', 'Harper']), #get a random name
                        'age': random.randint(13,72),
                        'score': 0,
                        'ai': True
                        }
        elif given_dict != {}: self.character = given_dict

        if self.character['name'] == 'Frank':
            self.character['score'] = -1000000000
        elif self.character['name'] == 'Travis':
            self.character['score'] = 1000000000000000000000000000000000000000000

    def __str__(self):
        return f"{self.character['name']}, {self.character['age']}: With {self.character['score']} points. Player Controled: {not self.character['ai']}"

    def add_points(self, input):
        print(f"add {input}")
        self.character['score'] += input

def player_setup(players):
    setup = True
    while True:
        user_input = str.lower(input("Do you want to set up a player? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
        if user_input == "y" or user_input == "n":
            break
        else: print("\033[1;31mError, try inputing again\033[1;0m")
            
    while setup and len(players) < 3 and user_input == "y":
        base_dict = {'name': "", 'age': 0, 'score': 0, 'ai': False}
        #Get an clean up name input
        while True:
            name_input = input("What is your name?\n")
            if name_input == "":
                print("\033[1;31mPlease input a name\033[1;0m")
            elif name_input != "":
                base_dict['name'] = name_input
                if not name_input.isalpha():
                    print("Intoresting name!")
                break
        #Get and cleanup age input
        while True:
            age_input = input("How old are you?\n")
            if age_input.isnumeric() and int(age_input) > 0:
                base_dict['age'] = int(age_input)
                if int(age_input) > 90:
                    print("You old fart sure you want to play this game?") 
                elif int(age_input) < 15:
                    print("Ya ankle bitter sure you want to be here?")
                break
            else:
                if age_input == "yo mama":
                    base_dict['age'] = 1000000000000000000000000000000000
                elif not age_input.isnumeric():
                    print("\033[1;31mPlease put their age as a number.\033[1;0m")
                elif age_input.isnumeric() and int(age_input) <= 0:
                    print("\033[1;31mPlease input a number greater than 0\033[1;0m")
                else: 
                    print("\033[1;31mERROR\033[1;0m")
        #init a new player and add it to the end of the list of players
        players.append(player(base_dict))
        print(players[-1])
        while True:
            user_input = str.lower(input("Do you want to set up a player? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
            if user_input == "y" or user_input == "n":
                break
            elif user_input == "n": #if they dont then kick out of the loop
                setup = False
            else: print("\033[1;31mError, try inputing again\033[1;0m")

    #Finish filling out the list of players with AI's
    for i in range(len(players), 3):
        players.append(player({}))

def print_cypher(guessed_letters, cypher, person):
    won = True
    for letter in cypher:
        if letter not in guessed_letters:
            cypher = cypher.replace(letter, "_") #c.Fore.WHITE + c.Back.WHITE + i + c.Fore.RESET + c.Back.RESET
            won = False
            print(letter)
        elif guessed_letters != [] and letter != " " and letter != "'" and letter == guessed_letters[-1]:
            cypher = cypher.replace(letter, c.Back.GREEN + letter + c.Back.RESET)
    if won:
        person.add_points(5000)
    print(cypher)
    return won

def next_player(index):
    if index < 2: return index + 1
    elif index == 2: return 0

#counting how many letters there are in word
def count_letter(cypher, guessed_letter, guessed_letters): 
    cypher2 = list(cypher)
    count = sum(1 for letter in cypher if letter == guessed_letter)
    if guessed_letter == '_':
        for letter in cypher:
            if letter in guessed_letters:
                cypher2.remove(letter)
        return len(cypher2)
    print(f"There is {count} '{guessed_letter}'(s) in the puzzle.")
    return count

def letter_picker(type, guessed_letters, cypher, player):
    letter_list = {'vowel': list('euioa'), 'consonant': list('qwrtypsdfghjklzxcvbnm')}[type]
    while True:
        #print(plist)
        new_player_needed = False
        letter_count = 0
        if not player.character['ai']: 
            letter_input = str.lower(input(f"What {type} do you want?\n"))
        elif player.character['ai']: 
            letter_input = random.choice(letter_list)
        if letter_input in letter_list and letter_input not in guessed_letters:
            guessed_letters.append(letter_input)
            if letter_input in cypher:
                new_player_needed = False
                letter_count = count_letter(cypher, guessed_letters[-1], guessed_letters)
            elif letter_input not in cypher:
                new_player_needed = True
                print(f"There are no '{letter_input}'(s)")
            return guessed_letters, new_player_needed, letter_count
        elif letter_input not in letter_list:
            print(f"Please do a {type}")
        elif letter_input in guessed_letters:
            print("You already guessed that")

def wheel_spin(player, guessed_letters, cypher):
    wheel = ['Lose a Turn', 800, 500, 650, 500, 900, 'Bankrupt', 5000, 500, 600, 700, 600, 650, 500, 700, 500, 600, 550, 500, 600, 'Bankrupt', 650, 700, 'Lose a Turn']
    rest = 0.01
    while rest < 0.7:
        landed_on = random.choice(wheel)
        print(landed_on, "\033[?25l                    ", end = "\r")
        t.sleep(rest)
        rest *= 1.1
    print('\033[?25h')
    if type(landed_on) == int:
        guessed_letters, new_player_needed, count = letter_picker('consonant', guessed_letters, cypher, player)
        print(f"Land_on {landed_on}, count {count}")
        player.add_points(landed_on*count)
    if landed_on == 'Lose a Turn':
        new_player_needed = True
    elif landed_on == 'Bankrupt':
        player.character['score'] = 0
        new_player_needed = False
    return guessed_letters, new_player_needed, player

def buy_vowel(player, guessed_letters, cypher):
    new_player_needed = False
    done = all(letter in guessed_letters for letter in list('euioa'))
    if done:
        print("There are no more vowels to buy")
    else:
        guessed_letters, new_player_needed, count = letter_picker('vowel', guessed_letters, cypher, player)
        player.add_points(-200)
        print(player)
    return guessed_letters, new_player_needed, player

def solve_cypher(player, cypher):
    won = False
    new_player_needed = False
    count = count_letter(cypher, "_", guessed_letters)
    if (not player.character['ai'] and str.lower(input("What do you think the phrase is?\n")) == str.lower(cypher)) or (player.character['ai'] and random.randint(0, count) == count):
        won = True 
        player.add_points(5000)
        print(f"{player}\nGOT IT, the cypher was \"{cypher}\"")
    else:
        print("That is not what the cypher is.")
        new_player_needed = True
    return player, won, new_player_needed

player_setup(players)

cypher = str.lower(random.choice(phrases)) #get the starting cypher
won = False
#won = print_cypher(guessed_letters, cypher, players[0]) #get playing and print the cphyer

while not won:
    if players != []:
        won = print_cypher(guessed_letters, cypher, players[current_player])
    new_player_needed = False

    if players[current_player].character['ai']: 
        choice = random.randint(1,2)
        print(f"{players[current_player]} chose: {choice}")
    while True and not players[current_player].character['ai']:
        choice = str.lower(input(f"Do you (\033[1;33mplayer{current_player+1}\033[1;0m) want to\n(1) Spin the Wheel,\n(2) Buy a Vowel,\n(3) Solve the puzzle,\n(4) See Stats and Stuff\n "))
        if choice.isnumeric():
            choice = int(choice)
            break
        elif choice == "show":
            print(cypher)
        else: 
            print("\033[1;31mError, try inputing again\033[1;0m")

    match choice:
        case 1: #Spin wheel
            guessed_letters, new_player_needed, players[current_player] = wheel_spin(players[current_player], guessed_letters, cypher)
        case 2: #buy vowel
            if players[current_player].character['score'] > 200: 
                guessed_letters, new_player_needed, players[current_player] = buy_vowel(players[current_player], guessed_letters, cypher)
            elif players[current_player].character['score'] < 200: 
                print("You need more the 200 points.")
        case 3: #solve
            players[current_player], won, new_player_needed = solve_cypher(players[current_player], cypher)
        case 4: #print stats
            print(str(guessed_letters))
            for person in players: print(person)
            
    if new_player_needed: 
        current_player = next_player(current_player)

    
    if won:
        top = [0, 'name']
        for current_player in players:
            if current_player.character['score'] > top[0]:
                top[0] = current_player.character['score']
                top[1] = current_player.character['name']
            elif current_player.character['score'] > 0 and current_player.character['score'] == top[0]:
                top[1] = [top[1], current_player['name']]
        if type(top[1]) == list:
            print(f"There was a tie between {", ".join(top[1])} with {top[0]} points")
        else:
            print(f"{top[1]} Won the game with {top[0]} points")

        while True:
            userinp = str.lower(input("Do you want to play again? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
            if userinp == "y":
                players = []
                guessed_letters = []
                current_player = 0
                cypher = random.choice(phrases)
                won = print_cypher(guessed_letters, cypher, current_player)
            elif userinp == "n":
                print("Ok bye have fun, with out me :(")
                break
            else:
                print("Please input y or n")
    t.sleep(0.5)