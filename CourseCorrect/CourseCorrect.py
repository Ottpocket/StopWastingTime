"""
The action to take upon bad course taken.

USAGE
-------------
dele = CourseCorrectCoR().get_object('base')
dele.course_correct()
"""
from abc import ABC, abstractmethod
import os
import ctypes  # An included library with Python install.


class CourseCorrectCoR:
  """ Chain of Responsibility from creating a CourseCorrect Factory"""
  def get_object(self, type_of_factory: str):
    if type_of_factory == "base":
      return DeleteAllCourseCorrect()
    elif type_of_factory == "delete_all":
      return DeleteAllCourseCorrect()
    elif type_of_factory == 'test':
      return TestCourseCorrect()
    elif type_of_factory == 'pids':
      return CourseCorrectPids()
    elif type_of_factory == 'popup':
      return CourseCorrectPopUp()
    else:
      raise Exception(f'Invalid Param for CourseCorrect factory.')

class CourseCorrect(ABC):
  """ Abstract class for dealing with user wasting time on internet"""

  @abstractmethod
  def course_correct(self, message):
    """ Accepts object of Message class"""
    pass


class DeleteAllCourseCorrect(CourseCorrect):
  """ Deletes all websites on all browsers """

  def course_correct(self, message):
    for browser in ['firefox', 'chrome']:
      try:
        os.system(f"taskkill /im {browser}.exe /f")
      except e:
        #If the browser is not running, will throw an exception.  
        pass       

class CourseCorrectPids(CourseCorrect):
  """ deletes all pids from message """
  
  def course_correct(self, message):
    for browser, pid_list in message.message.items():
      if len(pid_list) > 0:
        print(f'{browser} browser: deleting pids {pid_list}')
        for pid in pid_list:
          os.system(f"taskkill /F /PID {pid}")

class CourseCorrectPopUp(CourseCorrect):
  """ Opens a popup box """

  def course_correct(self, message):
    """ Takes pids from message as a popup """
    msg = ''
    for browser, pids in message.message.items():
      msg += f'{browser}: {pids}\n'

    self.Mbox(title= 'Warning!', text=msg)  
  def Mbox(self, title, text, style= 0x40000):
    return ctypes.windll.user32.MessageBoxW(None, text, title, style)
  

        
class TestCourseCorrect(CourseCorrect):
  def course_correct(self):
    print('Course Correcting!')
