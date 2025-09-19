def start_game(players):
    print("\n🎮 Game is Starting!")
    num_rounds = 1

    for round_num in range(1, num_rounds + 1):
        print(f"\n🔁 Round {round_num}")
        for player in players:
            input(f"{player['name']}'s turn. Press Enter to roll the dice...")
            dice = roll_dice()
            total = sum(dice)
            print(f"{player['name']} ({player['piece']}) rolls: {dice[0]} and {dice[1]} — Total: {total}")
    start_game(players)
