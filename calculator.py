from unittest import result


class Calculator:
  
  def __init__(self, save_result_on_memory = True):
    self._result = 0
    self._save_result_on_memory = save_result_on_memory

  def add(self, number):
    self._result += number

  def subtract(self, number):
    self._result -= number

  def get_result(self):
    result = self._result
    if not self._save_result_on_memory:
      self._result = 0
    return result
  
