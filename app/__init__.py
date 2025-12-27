from app.split_integer import split_integer


def test_return_list_with_one_element_when_number_of_parts_is_one():
    assert split_integer(8, 1) == [8]


def test_return_equal_parts_when_value_is_divisible_by_number_of_parts():
    assert split_integer(6, 2) == [3, 3]


def test_return_exactly_number_of_parts_elements():
    result = split_integer(17, 4)
    assert len(result) == 4


def test_parts_sum_to_value():
    result = split_integer(32, 6)
    assert sum(result) == 32


def test_parts_differ_by_at_most_one():
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_parts_are_sorted_ascending():
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_handle_case_where_value_is_less_than_number_of_parts():
    result = split_integer(2, 5)
    assert result == [0, 0, 0, 1, 1]
