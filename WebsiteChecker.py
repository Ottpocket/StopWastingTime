"""
Checks current websites 

USAGE
-----------
checker = WebsiteCheckerCoR().get_object('test')
checker.get_current_websites()
"""
from abc import ABC, abstractmethod
import os
import sqlite3
import time

class WebsiteChecker(ABC):
  """ Checks current websites """

  @abstractmethod
  def get_current_websites(self) -> list:
    return []


class WebsiteCheckerOnline(WebsiteChecker):
  """ Looks online via something to look at website tabs"""
  def get_current_websites(self):
    pass    

class WebsiteCheckerHistory(WebsiteChecker):
  """ Looks at local History sqlite3 database to check history.
  NOTE: this assumes windows and only looks at Chrome
  """
  self.user = os.getlogin()
  self.chrome_history = f"C:\\Users\\{self.user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
  self.pgm_start = time.time()
  def get_current_websites(self):
    pass

class WebsiteCheckerTest(WebsiteChecker):
  """ Test class for debugging """

  def get_current_websites(self, sites=None):
    if sites is None:
      return ['google', 'stackoverflow', 'co.cccc']
    else:
      return sites


class WebsiteCheckerCoR:
  """Chain of responsibility for WebsiteChecker object creation """

  def get_object(self, type_of_object):
    if type_of_object == 'base':
      return WebsiteCheckerOnline()
    elif type_of_object == 'test':
      return WebsiteCheckerTest()
