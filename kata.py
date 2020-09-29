from enum import Enum


class Score(Enum):
    ZERO = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    ADVANTAGE = 4

    def __str__(self):
        return ["0", "15", "30", "40", "A"][self.value]


def next_score(current_score):
    return Score(current_score.value + 1)


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
