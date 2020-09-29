from score import Score, next_score
from tennisplayer import TennisPlayer


class Game:
    def __init__(self, server_score: Score, receiver_score: Score):
        self.server = TennisPlayer(server_score)
        self.receiver = TennisPlayer(receiver_score)

    def increment_server_score(self):
        self._increment_player_score(self.server, self.receiver)

    def increment_receiver_score(self):
        self._increment_player_score(self.receiver, self.server)

    def is_over(self):
        return self.winner() is not None

    def winner(self):
        if self.server.score == Score.WIN:
            return "Server"
        if self.receiver.score == Score.WIN:
            return "Receiver"
        return None

    def format_score(self):
        return f"{self.server.score}:{self.receiver.score}"


def _increment_player_score(player, opponent):
    if player.score == Score.FORTY:
        if opponent.score == Score.ADVANTAGE:
            opponent.score = Score.FORTY
        elif opponent.score == Score.FORTY:
            player.score = Score.ADVANTAGE
        else:
            player.score = Score.WIN
    else:
        player.score = next_score(player.score)
