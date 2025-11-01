"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload


class Plane(Vehicle):

  def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
    super().__init__(weight=weight, fuel=fuel,
                     fuel_consumption=fuel_consumption)
    self.max_cargo = max_cargo
    self.cargo = 0

  def load_cargo(self, value):
    if self.max_cargo >= self.cargo + value:
      self.cargo = self.cargo + value
    else:
      raise CargoOverload("Ошибка, перегрузка")

  def remove_all_cargo(self):
    cargo_before_remove = self.cargo
    self.cargo = 0
    return cargo_before_remove
