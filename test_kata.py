import kata

def test_server_score():

    score = kata.Scorer(0, 0)
    score.server_scorer()

    assert score.server_scorer() == '15:0'

def test_receiver_score():

    score = kata.Scorer(0, 0)
    score.receiver_scorer()

    assert score.receiver_scorer() == '0:15'

