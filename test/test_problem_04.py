import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('1234\n', ['4321', '10']),
        ('1200\n', ['21', '3']),
        ('0\n', ['0', '0']),
        ('7\n', ['7', '7']),
        ('10\n', ['1', '1']),
        ('999999\n', ['999999', '54']),
        ('1000000007\n', ['7000000001', '8']),
    ],
)
def test_reverse_and_digit_sum(run, stdin, expected):
    assert run("problem_04", stdin) == expected
