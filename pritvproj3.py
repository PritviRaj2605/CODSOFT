import random
mylist = ['rock', 'paper', 'scissors']
opt = 0

while opt == 0:
    ch = input('Enter rock or paper or scissors to play the game: ')
    low = ch.lower()
    rand = random.choice(mylist)
    print('The bot\'s choice is:', rand)

    if low == rand:
        print('BOTH CHOSE THE SAME, IT IS A DRAW')
    elif low == 'rock' and rand == 'paper':
        print('PAPER BEATS ROCK')
        print('THE BOT WINS')
    elif low == 'paper' and rand == 'scissors':
        print('SCISSORS BEATS PAPER')
        print('THE BOT WINS')
    elif low == 'scissors' and rand == 'rock':
        print('ROCK BEATS SCISSORS')
        print('THE BOT WINS')
    elif low == 'paper' and rand == 'rock':
        print('PAPER BEATS ROCK')
        print('CONGRATS YOU WIN')
    elif low == 'scissors' and rand == 'paper':
        print('SCISSORS BEATS PAPER')
        print('CONGRATS YOU WIN')
    elif low == 'rock' and rand == 'scissors':
        print('ROCK BEATS SCISSORS')
        print('CONGRATS YOU WIN')
    else:
        print('Invalid choice!')

    opt = int(input('Enter 0 to continue or 1 to exit the game: '))

if opt == 1:
    print('Exiting the game.') 