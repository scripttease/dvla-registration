"""This module contains the functions for the registration of vehicles."""

from dataclasses import dataclass


@dataclass
class Vehicle:
    reg: str
    year: int
    id: int | None


class Database:
    vehicles: dict[str, Vehicle]

    def __init__(self):
        self._vehicles = {}

    def register(self, vehicle: Vehicle) -> None:
        self._vehicles[vehicle.reg] = vehicle

    def get_vehicle(self, reg: str) -> Vehicle:
        return self._vehicles[reg]

    def get_vehicle_id_from_reg(self, reg: str) -> int | None:
        return self._vehicles[reg].id

    def total_registration_numbers(self) -> int:
        return len(self._vehicles)
