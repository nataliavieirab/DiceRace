import time
from dice import rollDice
from events import applyEvents
from ui import *

finish_line = 30
computer_position = 0
player_position = 0


def run():
    global computer_position
    global player_position

    title()

    while True:
        playerTurn()
        input("Pressione ENTER para rolar o dado...")

        dice = rollDice()
        showDice("Você", dice)

        player_position += dice
        player_position = applyEvents(player_position)

        if dice == 6:
            extraTurn()
            extra = rollDice()
            showDice("Você", extra)

            player_position += extra
            player_position = applyEvents(player_position)

        if player_position >= finish_line:
            winner("Você")
            break

        computerTurn()
        dice = rollDice()
        showDice("Computador", dice)

        computer_position += dice
        computer_position = applyEvents(computer_position)

        if dice == 6:
            extraTurn()
            extra = rollDice()
            showDice("Computador", extra)

            computer_position += extra
            computer_position = applyEvents(computer_position)

        if computer_position >= finish_line:
            winner("Computador")
            break
          
        print("\n\n\n     📊 RESULTADO DA RODADA 📊 ", flush=True)
        time.sleep(1)
        showTrack(player_position, computer_position)
        showPositions(player_position, computer_position)

        print("\n\nPróxima rodada...", flush=True)
        time.sleep(2)
        print("\n-" * 2, flush=True)
        time.sleep(1)