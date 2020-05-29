from main import check_is_day_off, check_weekday, choose_person, check_gender, action_generator, damn_generator


def test_check_is_day_off(get_date):
    date, expected_result = get_date[0], get_date[1]
    result = check_is_day_off(date)
    assert result == expected_result


def test_check_weekday(get_date):
    date, expected_result = get_date[0], get_date[2]
    result = check_weekday(date)
    assert result == expected_result


def test_choose_person(get_person_list):
    person = choose_person(1, get_person_list)
    assert person == get_person_list[0]


def test_check_gender(get_person_list):
    gender0 = check_gender(get_person_list[0])
    gender1 = check_gender(get_person_list[1])
    assert gender0 == "male" and gender1 == "female"


def test_action_generator(get_manager_action_list):
    action = action_generator(get_manager_action_list)
    assert action in get_manager_action_list


def test_damn_generator(get_gender, get_damn_noun_list, get_damn_adjective_list):
    """Checking the correct end of the adjective. Checking the deletion of the used word from lists after generating."""

    damn = damn_generator(get_gender[0], get_damn_noun_list, get_damn_adjective_list)
    noun, adj = damn.split()

    adj_end, expected_adj_end = adj[-2:], get_gender[1]

    assert adj_end == expected_adj_end
    assert noun not in get_damn_noun_list
    assert adj not in get_damn_adjective_list
