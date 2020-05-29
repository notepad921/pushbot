import pytest
import datetime


@pytest.fixture(params = [
    (datetime.date(2020, 3, 10), False, 2),
    (datetime.date(2020, 3, 9), True, 1)
    ],
    ids=["working day, tuesday", "day-off, monday"])
def get_date(request):
    return request.param
