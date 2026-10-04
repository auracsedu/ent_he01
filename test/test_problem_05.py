import pytest


@pytest.mark.parametrize(
    "stdin, expected",
    [
        ('3\n7\n2\n0\n', ['3', '7']),
        ('0\n', ['0', '없음']),
        ('5\n0\n', ['1', '5']),
        ('1\n2\n3\n4\n5\n0\n', ['5', '5']),
        ('9\n9\n9\n0\n', ['3', '9']),
        ('100\n1\n50\n0\n', ['3', '100']),
        ('4\n3\n2\n0\n99\n', ['3', '4']),
    ],
)
def test_max_until_zero(run, stdin, expected):
    assert run("problem_05", stdin) == expected
