import time
def line():
    print("=" * 40)
def title():
    line()
    print("   🎲 JOGO DE CORRIDA DE DADOS 🎲")
    line()
    print(" O primeiro a chegar na casa 30 vence!")
    line()

def playerTurn():
    print("\n" + "-" * 40)
    print("       🧑 TURNO DO JOGADOR 🧑")
    print("-" * 40)
    print("\n>> É sua vez de jogar! ",)

def computerTurn():
    print("\n" + "-" * 40)
    print("      💻 TURNO DO COMPUTADOR 💻")
    print("-" * 40, flush=True)
    time.sleep(1)

def showDice(player, value):
    print("\nRolando dado...", flush=True)
    time.sleep(3)
    print(f"🎲 {player} tirou: {value}", flush=True)
    time.sleep(2)

def extraTurn():
    print("🔥 Rodada extra!", flush=True)
    time.sleep(1)

def winner(player):
    print("\n" * 2)
    line()
    print("\n")
    print(f"🏆 {player} venceu!")
    print("\n")
    line()

def showPositions(player_position, computer_position):
    print(f"\n>> Você está na casa {player_position}", flush=True)
    time.sleep(0.5)
    print(f">> Computador está na casa {computer_position}", flush=True)
    time.sleep(0.5)

def showTrack(player_position, computer_position):
    track = ""

    for i in range(31):
        if i == player_position and i == computer_position:
            track += "🤝"
        elif i == player_position:
            track += "🧑"
        elif i == computer_position:
            track += "💻"
        else:
            track += "-"

    print(f"\n  {track}")
    print("  " + "0" + " " * 30 + "30", flush=True)
    time.sleep(1)