import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('2024\n', ['윤년']),
        ('2023\n', ['평년']),
        ('1900\n', ['평년']),
        ('2000\n', ['윤년']),
        ('2100\n', ['평년']),
        ('4\n', ['윤년']),
        ('1\n', ['평년']),
    ],
)
def test_leap_year(run, stdin, expected):
    assert run("problem_02", stdin) == expected
