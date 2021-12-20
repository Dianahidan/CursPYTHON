from functions import sum_from_args

def test_sum_from_args():
    result = sum_from_args(1, 2, 3, 4, 5)
    assert result == 45