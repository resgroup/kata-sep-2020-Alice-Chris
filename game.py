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

    def _increment_player_score(self, player, opponent):
        if player.score == Score.FORTY:
            if opponent.score == Score.ADVANTAGE:
                opponent.score = Score.FORTY
            elif opponent.score == Score.FORTY:
                player.score = Score.ADVANTAGE
            else:
                player.score = Score.WIN
        else:
            player.score = next_score(player.score)

    def format_score(self):
        if self.server.score == Score.WIN:
            return "Server wins!"
        return f"{self.server.score}:{self.receiver.score}"


