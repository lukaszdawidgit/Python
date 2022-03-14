from lotto import random_numbers


def test_draw_numbers():
    for _ in range(0, 501):
        score = sorted(random_numbers())
        assert len(score) == 6
        assert score[0] >= 1
        assert score[-1] <= 49
