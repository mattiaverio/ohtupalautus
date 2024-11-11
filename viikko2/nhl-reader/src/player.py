class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get("name")
        self.team = player_dict.get("team")
        self.goals = player_dict.get("goals")
        self.assists = player_dict.get("assists")
        self.nationality = player_dict.get("nationality")

    def total_points(self):
        return self.goals + self.assists

    
    def __str__(self):
        return f"{self.name:20} {self.team:9} {self.goals:2} + {self.assists:2} = {self.total_points()}"