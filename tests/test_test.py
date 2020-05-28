from main import check_is_day_off, check_weekday


def test_check_is_day_off(get_date):
    date, expected_result = get_date[0], get_date[1]
    result = check_is_day_off(date)
    print(f"{date} is {result}")
    assert result == expected_result


def test_check_weekday(get_date):
    date, expected_result = get_date[0], get_date[2]
    result = check_weekday(date)
    print(f"{date} is {result}")
    assert result == expected_result
