from enum import Enum


class Score(Enum):
    ZERO = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    ADVANTAGE = 4
    WIN = 5

    def __str__(self):
        return ["0", "15", "30", "40", "A"][self.value]


def next_score(current_score):
    return Score(current_score.value + 1)
