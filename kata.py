from enum import Enum


class Score(Enum):
    ZERO = "0"
    FIFTEEN = "15"
    THIRTY = "30"
    FORTY = "40"
    ADVANTAGE = "A"


def next_score(current_score):
    if current_score == Score.ZERO:
        return Score.FIFTEEN
    if current_score == Score.FIFTEEN:
        return Score.THIRTY
    if current_score == Score.THIRTY:
        return Score.FORTY


class Game:
    def __init__(self, server_score: Score, receiver_score: Score):
        self.server_score = server_score
        self.receiver_score = receiver_score

    def increment_server_score(self):
        self.server_score = next_score(self.server_score)

    def increment_receiver_score(self):
        self.receiver_score = next_score(self.receiver_score)

    def format_score(self):
        return f"{self.server_score.value}:{self.receiver_score.value}"

