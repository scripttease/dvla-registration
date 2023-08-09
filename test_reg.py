import pytest
from reg import *


@pytest.fixture
def registration_data():
    return DATABASE


def test_vehicle_id_from_reg(registration_data):
    reg = "AB01 CDE"
    assert vehicle_id_from_reg(registration_data, reg) == 12345


def test_total_registration_numbers(registration_data):
    assert total_registration_numbers(registration_data) == 3
