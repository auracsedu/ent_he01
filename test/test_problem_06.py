import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('1\n', ['*']),
        ('2\n', [' *', '***']),
        ('3\n', ['  *', ' ***', '*****']),
        ('5\n', ['    *', '   ***', '  *****', ' *******', '*********']),
        ('7\n', ['      *', '     ***', '    *****', '   *******', '  *********', ' ***********', '*************']),
    ],
)
def test_pyramid(run, stdin, expected):
    assert run("problem_06", stdin) == expected
