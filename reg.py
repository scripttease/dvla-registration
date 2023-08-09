"""This module contains the functions for the registration of vehicles."""

from dataclasses import dataclass


@dataclass
class Vehicle:
    reg: str
    year: int
    id: int | None


DATABASE = {
    "AB01 CDE": Vehicle("AB01 CDE", 2001, 12345),
    "FG02 HJK": Vehicle("FG02 HJK", 2002, 67890),
    "L33T H4X0R": Vehicle("L33T H4X0R", 2022, None),
}


def vehicle_id_from_reg(database: dict[str, Vehicle], reg: str) -> int | None:
    """Return the vehicle ID for the given registration number."""
    return database[reg].id


def total_registration_numbers(database: dict[str, Vehicle]) -> int:
    """Return the total number of registration numbers in the database."""
    return len(database)
