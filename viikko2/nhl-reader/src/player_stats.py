class PlayerStats:
    def __init__(self, player_reader):
        self._players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = [player for player in self._players if player.nationality == nationality]
        players.sort(key=lambda player: player.total_points(), reverse=True)
        return players