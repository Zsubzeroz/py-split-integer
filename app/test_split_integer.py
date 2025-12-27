from app.split_integer import split_integer


def test_split_integer_returns_single_element_list_when_parts_is_one():
    assert split_integer(8, 1) == [8]


def test_split_integer_returns_equal_parts_when_perfectly_divisible():
    assert split_integer(6, 2) == [3, 3]


def test_split_integer_result_sum_equals_value():
    # Testa se a soma dos elementos é igual ao valor original
    value, parts = 17, 4
    assert sum(split_integer(value, parts)) == value


def test_split_integer_result_length_equals_number_of_parts():
    # Testa se o tamanho da lista é exatamente o solicitado
    assert len(split_integer(32, 6)) == 6


def test_split_integer_result_is_sorted_ascending():
    # Verifica se a lista está em ordem crescente
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_split_integer_difference_between_max_and_min_is_at_most_one():
    # Verifica a regra fundamental de distribuição (max - min <= 1)
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1


def test_split_integer_handles_value_less_than_parts():
    # Quando o valor é menor que as partes, deve resultar em 0s e 1s ordenados
    value, parts = 2, 5
    result = split_integer(value, parts)
    assert result == [0, 0, 0, 1, 1]
    assert sum(result) == value
