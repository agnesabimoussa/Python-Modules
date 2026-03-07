import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print("No scores provided.", end="")
        print(" Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            players: list = []
            for arg in sys.argv[1:]:
                score = int(arg)
                players.append(score)
            print("Scores processed:", players)
            print("Total players:", len(players))
            print("Total score:", sum(players))
            print("Average score:", sum(players) / len(players))
            print("High score:", max(players))
            print("Low score:", min(players))
            print("Score range:", max(players) - min(players))
        except ValueError:
            print(f"Invalid literal for int() with base 10: '{arg}'")
