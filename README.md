# WheelOfFortune
 Wheel Of Fortune. Idk what to tell you. Made for CSE python class

----------------------------------------------------------------------------------------

# Requirements

DESCRIPTION: Wheel of Fortune

This program will mimic the TV show Wheel of Fortune. The object of the game is to guess consonants and/or vowels to try and solve the puzzle (phrase). If you do not know how Wheel of Fortune is played, I would search clips on YouTube to get a better understanding of how this game is played.

A player, on their turn, is able to "spin the wheel" to see how much each consonant guessed will be worth, "buy a vowel" for 200 points, or solve the puzzle. If the letter the player guesses is not in the puzzle, his/her turn is over and it is the next player's turn.

In order to receive a passing grade, you must COMMENT line by line (or section by section, depending on your code).
This activity is worth 50 points in the Projects category (25% of your grade).

The requirements for the password are as follows:
1. Puzzle:
   - There must be at least five (5) puzzles to choose from.
   - One puzzle will be selected at random when the game starts.
   - ALL non-consonant/vowel characters will be revealed at the beginning. For example, if there is an apostrophe ('), then it needs to show up when the inital puzzle is revealed.
   - After each player guesses a letter (consonant or a vowel), the puzzle should be displayed.

2. Players and turns:
   - There needs to be three (3) players.
   - The order of turns will be circular. For example, P1 -> P2 -> P3 -> P1 -> P2 -> etc. The order of turns can be randomized or in the order of input (i.e., P1 always goes first, P2 always goes second, P3 always goes third.)
   - If the player guesses a letter in the puzzle, he/she goes again (chooses to "spin the wheel", "buy a vowel", or "solve the puzzle").
   - If the player incorrectly guesses a letter, his/her turn ends.
   - If the player incorrectly solves the puzzle, his/her turn ends.

3. "Spinning the wheel":
   - If the wheel is spun, only consonants are valid guesses.
   - A point total will be selected at random from a list of point totals.
   - Only one consonant can be guessed at a time; however all the instances of that consonant is revealed in the puzzle.
   - If the guessed consonant is not in the puzzle, the player's turn is over. Points are not deducted from the player's score.

4. "Buying a vowel":
   - "Buying a vowel" costs 200 points. It is 200 points no matter how many of that vowel there are in the puzzle.
   If the guessed vowel is not in the puzzle, the player's turn is over and 200 points are deducted from the player's score.

5. Scoring:
   - For consonants, a player gets the points for each consonant in the puzzle. For example, let's say a player spins the wheel and it lands on 200 points. If the player guesses the letter "R" and there are three (3) R's in the puzzle, the player gets 600 points (200 points for each R).
   - After each turn, the player's turn should be displayed.
   - If the puzzle is solved, 5000 points is awarded to the guessing player and the game is over.
   - Possible points on the wheel ranges from 100 to 2500 points.

6. Game over:
   - When the game is over, user is asked if he/she wants to play again.
     - If yes, the game starts over.
     - If no, the program exits.
   - The player with the most points wins, regardless of who solves the puzzle.
   - All the players' scores should be displayed.

7. Other notes:
   - After each letter is guessed, the game should indicate that:
     1. The letter is not in the puzzle;
     2. There are X number of letter in the puzzle and how many points the player earned
   - Player management:
     - Indicate whose turn it is.

8. MUST USE FUNCTION(S), LOCAL VARIABLES, LOOPS, and LISTS. Not using one of these will lower your score by 20%.

9. The random and colorama modules are the only modules needed. You must ask Mrs. Hong's approval for other modules.
TIME.sleep


1. Extra credit (EC percentage is up to Mrs. Hong):
   - Use classes (see Activity 3.2.4: Course Registrations: Functions).

2. Travis extras
   - Show green highlight on new lets
   - coment if the name has a number or spectial charicter
   - comment if the player charictor is super old or young
   - AI solving
   - Color the errors and numbers and stuff
   - If no more vualse to buy say that.
   - name bias
