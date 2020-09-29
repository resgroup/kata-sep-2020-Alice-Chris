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
        if opponent.score != Score.ADVANTAGE:
            player.score = next_score(player.score)
        else:
            opponent.score = Score.FORTY

    def format_score(self):
        return f"{self.server.score}:{self.receiver.score}"


