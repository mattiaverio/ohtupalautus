from player_stats import PlayerStats
from player_reader import PlayerReader

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Top scorers from FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
