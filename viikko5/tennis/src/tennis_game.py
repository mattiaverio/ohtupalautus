class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ''
        if self.is_tie():
            return self.tie_score()

        if self.has_advantage_or_win():
            return self.advantage_or_win_score()
        return self.score()
    
    def is_tie(self):
        if self.player1_score == self.player2_score:
            return True 

    def tie_score(self):
        tie_scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }
        return tie_scores.get(self.player1_score, "Deuce")
    
    def has_advantage_or_win(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            return True 
        
    def advantage_or_win_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"
        
    def score(self):
        point_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{point_names[self.player1_score]}-{point_names[self.player2_score]}"