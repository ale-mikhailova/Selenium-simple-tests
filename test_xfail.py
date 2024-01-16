import pytest

#@pytest.mark.xfail(strict=True) #второй вариант решения
def test_succeed():
    if test_not_succeed():
        pytest.xfail
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False