"""
The action to take upon bad course taken.

USAGE
-------------
dele = CourseCorrectCoR().get_object('base')
dele.course_correct()
"""
from abc import ABC, abstractmethod
import os

class CourseCorrectCoR:
  """ Chain of Responsibility from creating a CourseCorrect Factory"""
  def get_object(self, type_of_factory: str):
    if type_of_factory == "base":
      return DeleteAllCourseCorrect()
    elif type_of_factory == "delete_all":
      return DeleteAllCourseCorrect()
    elif type_of_factory == 'test':
      return TestCourseCorrect()
    else:
      raise Exception(f'Invalid Param for CourseCorrect factory.')

class CourseCorrect(ABC):
  """ Abstract class for dealing with user wasting time on internet"""

  @abstractmethod
  def course_correct(self):
    pass


class DeleteAllCourseCorrect(CourseCorrect):
  """ Deletes all websites on all browsers """

  def course_correct(self):
    for browser in ['firefox', 'chrome']:
      try:
        os.system(f"taskkill /im {browser}.exe /f")
      except e:
        #If the browser is not running, will throw an exception.  
        pass       

class TestCourseCorrect(CourseCorrect):
  def course_correct(self):
    print('Course Correcting!')
