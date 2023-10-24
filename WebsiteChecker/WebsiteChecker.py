"""
Checks current websites 

USAGE
-----------
checker = WebsiteCheckerCoR().get_object('test')
checker.get_current_websites()
"""
from abc import ABC, abstractmethod
import os
import time
from StopWastingTime.GetPids.GetPids import GetPidsFactory

class WebsiteChecker(ABC):
  """ Checks current websites """

  @abstractmethod
  def get_current_websites(self) -> list:
    return []


class WebsiteCheckerOnline(WebsiteChecker):
  """ Looks online via something to look at website tabs"""
  def get_current_websites(self):
    pass    

'''
WILL NOT WORK FOR OPEN TABS. DEFUNCT
import sqlite3
class WebsiteCheckerHistory(WebsiteChecker):
  """ Looks at local History sqlite3 database to check history.
  NOTE: this assumes windows and only looks at Chrome
  """
  self.user = os.getlogin()
  self.chrome_history_database = f"C:\\Users\\{self.user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
  self.pgm_start = time.time()
  def get_current_websites(self):
    #https://www.geeksforgeeks.org/python-sqlite-select-data-from-table/
    #https://www.sans.org/blog/google-chrome-forensics/
    conn = sqlite3.connect(self.chrome_history_database)
    cursor = conn.cursor()
    query = "SELECT title, last_visit_time FROM urls LIMIT 4"
    cursor.execute(query)
    output = cursor.fetchall()
    for row in output:
      print(row)
    conn.close()
'''    

class WebsiteCheckerTest(WebsiteChecker):
  """ Test class for debugging """

  def get_current_websites(self, sites=None):
    if sites is None:
      return ['google', 'stackoverflow', 'co.cccc']
    else:
      return sites

class WebsiteCheckerPids(WebsiteChecker):
  """ Outputs current pids  """
  def __init__(self):
    self.pids_getter = GetPidsFactory().get_object()

  def get_current_websites(self):
    website_pid_dict = {}
    for browser in ['firefox', 'chrome', 'msedge']:
      website_pid_dict[browser] = self.pids_getter.get_pids(browser=browser)
    return website_pid_dict 

class WebsiteCheckerCoR:
  """Chain of responsibility for WebsiteChecker object creation """

  def get_object(self, type_of_object):
    if type_of_object == 'base':
      return WebsiteCheckerOnline()
    elif type_of_object == 'test':
      return WebsiteCheckerTest()
    elif type_of_object == "pids":
      return WebsiteCheckerPids()