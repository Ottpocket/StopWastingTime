"""
Checks current websites 

USAGE
-----------
checker = WebsiteCheckerCoR().get_object('test')
checker.get_current_websites()
"""
from abc import ABC, abstractmethod

class WebsiteChecker(ABC):
  """ Checks current websites """

  @abstractmethod
  def get_current_websites(self) -> list:
    return []


class WebsiteCheckerOnline(WebsiteChecker):
  def get_current_websites(self):
    

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
