from score import Score, next_score


class Game:
    def __init__(self, server_score: Score, receiver_score: Score):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def increment_server_score(self):
        self.server_score = next_score(self.server_score)

    def increment_receiver_score(self):
        self.receiver_score = next_score(self.receiver_score)

    def format_score(self):
        return f"{self.server_score}:{self.receiver_score}"