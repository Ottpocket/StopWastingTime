"""
Creates an iterator that 
1) lasts a specific duration and
2) sleeps for a specific time between durations
"""
from abc import ABC, abstractmethod
from time import sleep

class TimedIterator(ABC):
  """
  Abstract class to give iterator that waits n seconds each iteration
  """

  def __init__(self, wait_seconds = 1):
    self.wait_seconds = wait_seconds
    self.iteration_counter = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    sleep(self.wait_seconds)
    self.iteration_counter += 1
    self.iteration_logic()
  
  @abstractmethod
  def iteration_logic(self):
    pass

  def update_iterator(

class TimedIteratorInfinite(TimedIterator):
  """
  yields an infinite loop
  """
  def iteration_logic(self):
    return self.iteration_counter


class TimedIteratorSeconds(TimedIterator):
  """
  an iterator that lasts `n` seconds
  """
  def __init__(self, wait_seconds, total_seconds_to_iterate=15):
    super().__init__(wait_seconds)
    self.num_iterations = int(total_seconds_to_iterate / self.wait_seconds)

  def iteration_logic(self):
    if self.iteration_counter <= self.num_iterations:
      return self.iteration_counter
    else:
      raise StopIteration

class TimedIteratorCoR:
  """
  Chain of Responsibility from creating TimedIterator objects
  """
  def get_object(self, num_seconds):
    if num_seconds < 0:
      return TimedIteratorInfinite()
    else:
      return TimedIteratorSeconds(num_seconds)
