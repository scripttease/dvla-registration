import pytest
from reg import *


@pytest.fixture
def registration_data():
    DATABASE = Database()

    DATABASE.register(Vehicle("AB01 CDE", 2001, 12345))
    DATABASE.register(Vehicle("FG02 HJK", 2001, 12345))
    DATABASE.register(Vehicle("L33TH 4X0R", 2022, None))
    return DATABASE


def test_vehicle_id_from_reg(registration_data):
    reg = "AB01 CDE"
    assert Database.get_vehicle_id_from_reg(registration_data, reg) == 12345


def test_total_registration_numbers(registration_data):
    assert Database.total_registration_numbers(registration_data) == 3
