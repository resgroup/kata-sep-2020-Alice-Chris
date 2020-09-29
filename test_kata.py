from game import Game
from score import Score


def test_score_format():
    game = Game(Score.ZERO, Score.ZERO)
    assert game.format_score() == '0:0'


def test_server_score():
    game = Game(Score.ZERO, Score.ZERO)
    game.increment_player_score("server")
    assert game.format_score() == '15:0'


def test_receiver_score():
    game = Game(Score.ZERO, Score.ZERO)
    game.increment_player_score("receiver")

    assert game.format_score() == '0:15'


def test_score_fifteen():
    game = Game(Score.FIFTEEN, Score.FIFTEEN)
    game.increment_player_score("receiver")

    assert game.format_score() == '15:30'


def test_score_thirty():
    game = Game(Score.THIRTY, Score.THIRTY)
    game.increment_player_score("server")

    assert game.format_score() == '40:30'


def test_score_server_gets_advantage():
    game = Game(Score.FORTY, Score.FORTY)
    game.increment_player_score("server")

    assert game.format_score() == 'A:40'
