import pytest
import datetime


@pytest.fixture(scope = "session",
                params = [
                    (datetime.date(2020, 3, 10), False, 2),
                    (datetime.date(2020, 3, 9), True, 1)
                    ],
                ids = ["working day, tuesday", "day-off, monday"])
def get_date(request):
    return request.param


@pytest.fixture(scope = "session")
def get_person_list():
    test_person_list = {0: ("Василий", "@test_vasya", "male"),
                        1: ("Татьяна", "@test_tatyana", "female"),
                        "manager": ("Олег", "@test_oleg", "male")
                        }
    return test_person_list


@pytest.fixture(scope = "session",
                params = [("male", "ый"), ("female", "ая")],
                ids = ["gender is male", "gender is female"])
def get_gender(request):
    return request.param


@pytest.fixture(scope = "session")
def get_manager_action_list():
    test_manager_action_list = ("двигает таски", "сидит на синках", "ест")
    return test_manager_action_list


@pytest.fixture(scope = "session")
def get_damn_adjective_list():
    test_damn_adjective_list = ["псоват", "незавидн", "дебиловат"]
    return test_damn_adjective_list


@pytest.fixture(scope = "session")
def get_damn_noun_list():
    test_damn_noun_list = [("антихрист", "антихристка"), ("безобразник", "безобразница"), ("баламошка", "баламошка")]
    return test_damn_noun_list
