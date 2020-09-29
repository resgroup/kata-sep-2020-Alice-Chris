from score import Score, next_score


class Game:
    def __init__(self, server_score: Score, receiver_score: Score):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def increment_player_score(self, player):
        if player == "server":
            if self.receiver_score != Score.ADVANTAGE:
                self.server_score = next_score(self.server_score)
            else:
                self.receiver_score = Score.FORTY
        elif player == "receiver":
            if self.server_score != Score.ADVANTAGE:
                self.receiver_score = next_score(self.receiver_score)
            else:
                self.server_score = Score.FORTY

    def format_score(self):
        return f"{self.server_score}:{self.receiver_score}"
