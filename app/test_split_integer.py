from app.split_integer import split_integer


def test_sum_or_single_part():
    assert split_integer(8, 1) == [8], (
        "Should return a list with the value itself if number_of_parts is 1"
    )


def test_split_into_equal_parts():
    assert split_integer(6, 2) == [3, 3], (
        "Should return equal parts when value is perfectly divisible"
    )


def test_split_into_parts_with_remainder():
    assert split_integer(17, 4) == [4, 4, 4, 5], (
        "The difference between elements should be no more than 1 "
        "and the list should be sorted"
    )


def test_split_into_parts_with_large_remainder():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6], (
        "Should handle cases where the remainder results in multiple higher values"
    )


def test_parts_should_be_sorted_ascending():
    result = split_integer(17, 4)
    assert result == sorted(result), (
        "The resulting list must be sorted in ascending order"
    )


def test_value_smaller_than_number_of_parts():
    assert split_integer(2, 5) == [0, 0, 0, 1, 1], (
        "Should work even if value is smaller than number_of_parts "
        "(elements should be 0 and 1)"
    )
