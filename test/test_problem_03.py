import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('10\n', ['33']),
        ('1\n', ['0']),
        ('2\n', ['0']),
        ('3\n', ['3']),
        ('15\n', ['60']),
        ('100\n', ['2418']),
        ('1000\n', ['234168']),
    ],
)
def test_multiple_sum(run, stdin, expected):
    assert run("problem_03", stdin) == expected
