import pytest
from reg import *


@pytest.fixture
def database():
    database = Database()

    database.register(Vehicle("AB01 CDE", 2001, 12345))
    database.register(Vehicle("FG02 HJK", 2001, 12345))
    database.register(Vehicle("L33TH 4X0R", 2022, None))
    return database


def test_register(database):
    vehicle = Vehicle("G839 SGX", 1989, 67654)
    database.register(vehicle)
    assert database.get_vehicles() == [
        Vehicle("AB01 CDE", 2001, 12345),
        Vehicle("FG02 HJK", 2001, 12345),
        Vehicle("L33TH 4X0R", 2022, None),
        Vehicle("G839 SGX", 1989, 67654),
    ]


def test_get_vehicle_id_from_reg(database):
    reg = "AB01 CDE"
    assert database.get_vehicle_id_from_reg(reg) == 12345


def test_total_registration_numbers(database):
    assert database.total_registration_numbers() == 3


def test_get_vehicle(database):
    reg = "AB01 CDE"
    assert database.get_vehicle(reg) == Vehicle("AB01 CDE", 2001, 12345)
