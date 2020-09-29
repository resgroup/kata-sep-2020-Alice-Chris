from kata import Score, Game


def test_score_format():
    game = Game(Score.ZERO, Score.ZERO)
    assert game.format_score() == '0:0'


def test_server_score():
    game = Game(Score.ZERO, Score.ZERO)
    game.increment_server_score()

    assert game.format_score() == '15:0'


def test_receiver_score():
    game = Game(Score.ZERO, Score.ZERO)
    game.increment_receiver_score()

    assert game.format_score() == '0:15'
