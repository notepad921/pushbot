import pytest

from src.main import check_is_day_off, check_weekday, choose_person, check_gender, action_generator,\
    damn_generator, generate_text, send_push


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
    gender2 = check_gender(None)
    assert gender0 == "male" and gender1 == "female" and gender2 is None


def test_action_generator(get_manager_action_list):
    action = action_generator(get_manager_action_list)
    assert action in get_manager_action_list


def test_damn_generator(get_gender, get_damn_noun_list, get_damn_adjective_list):
    """Checking the correct end of the adjective. Checking that the noun and adjective were on the source list."""

    damn = damn_generator(get_gender[0], get_damn_noun_list, get_damn_adjective_list)
    noun, adj = damn.split()

    adj_end, expected_adj_end = adj[-2:], get_gender[1]

    damn_noun_list = [item for sublist in get_damn_noun_list for item in sublist]

    assert adj_end == expected_adj_end
    assert adj[:-2] in get_damn_adjective_list
    assert noun in damn_noun_list


def test_generate_text(get_data_for_text):
    """Checking the correct assembly of the message`s text."""

    person, damn, action, manager, manager_damn, link = get_data_for_text

    text = generate_text(person, damn, action, manager, manager_damn, link)
    assert text == """@test_tatyana, безобразница незавидная, ты сегодня дежуришь!
https://www.google.com/

Ну и @test_oleg, как обычно, двигает таски, баламошка дебиловатый."""


def test_send_push(get_data_for_push):
    """Temporary check of success of sending a message via telegram."""
    chat_id, text = get_data_for_push
    success = send_push(chat_id, text)
    assert success is True


@pytest.mark.integration
@pytest.mark.trylast
def test_integration(get_damn_noun_list, get_damn_adjective_list, get_date, get_person_list, get_manager_action_list,
                     get_data_for_text, get_data_for_push):

    damn_noun_list = get_damn_noun_list
    damn_adjective_list = get_damn_adjective_list

    weekday = check_weekday(get_date[0])
    is_day_off = check_is_day_off(get_date[0])

    manager = get_person_list.get("manager")
    person = choose_person(weekday, get_person_list)
    gender = check_gender(person)

    action = action_generator(get_manager_action_list)
    damn = damn_generator(gender, damn_noun_list, damn_adjective_list) if person else None
    manager_damn = damn_generator(manager[2], damn_noun_list, damn_adjective_list)

    text = generate_text(person, damn, action, manager, manager_damn, get_data_for_text[5])

    if person and (is_day_off is False):
        success = send_push(get_data_for_push[0], text)
    else:
        success = True
        print("Сегодня не дежурим")

    assert success is True
