"""
Доработайте класс `Vehicle`
"""

from homework_05.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC


class Vehicle(ABC):

  def __init__(self, weight=0, fuel=0, fuel_consumption=0):
    self.weight = weight
    self.started = False
    self.fuel = fuel
    self.fuel_consumption = fuel_consumption

  def start(self):
    if not self.started and self.fuel > 0:
      self.started = True
    else:
      raise LowFuelError("Недостаточно топлива для запуска двигателя.")

  def move(self, distance):
    fuel_needed_for_move = distance * self.fuel_consumption

    if self.fuel >= fuel_needed_for_move:
      self.fuel = self.fuel - fuel_needed_for_move
    else:
      raise NotEnoughFuel("Недостаточно топлива для преодоления расстояния.")
