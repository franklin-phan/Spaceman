from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/dice')
def play_dice_game():
    dice_one = randint(1,6)
    dice_two = randint(1,6)
    if dice_one == dice_two:
        print('You won! You rolled '+(str(dice_one))+' and '+ str((dice_two))+'.')
    else:
        print('You lose. You rolled '+(str(dice_one))+' and '+(str(dice_two))+'.')

play_dice_game()

if __name__ == "__main__":
    app.run(debug=True)