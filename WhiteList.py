"""
Class for good websites
"""
from abc import ABC, abstractmethod
import sys
sys.path.append('GetPids')
from GetPids import GetPidsFactory




class WhiteListCoR:
  """ Chain of Responsibility to get correct WhiteList Object"""
  
  def get_object(self, factory_type):
    if factory_type == 'base':
      return WhiteListFromTxt()
    elif factory_type == 'test':
      return WhiteListTest()
    elif factory_type == 'pids':
      return WhiteListPids()
    else:
      raise Exception(f'{factory_type} not a proper parameter to create WhiteList object.')

class WhiteList(ABC):
  """ Creates a list of strings of good websites for browsing"""
  def __init__(self):
    self.whitelist = self.create_whitelist()
  
  @abstractmethod
  def create_whitelist(self):
    pass

  def website_in_whitelist(self, list_of_current_sites, whitelist_sites):
    """ checks if all current sites in whitelist """
    bad_sites = []
    for site in list_of_current_sites:
      if sum([sum([white_site.upper().startswith(site.upper()) for white_site in whitelist_sites])]) ==0:
        print(f'{site} not found in whitelist')
        bad_sites.append(site)
    return bad_sites

class WhiteListFromPids(WhiteList):
  """ creates a whitelist from pids currently running

  This whitelist has the form of the following dict:
  { 
    'chrome': [pid1, pid2, ...]
    'firefox': [pid1, pid2, ...]
    'msedge':[pid1, pid2, ...]
  }
  """
  def create_whitelist(self):
    whitelist = {}
    for browser in ['firefox', 'chrome', 'msedge']:
      whitelist[browser] = GetPidsFactory().get_object().get_pids(browser=browser)

class WhiteListFromTxt(WhiteList):
  """ creates the whitelist of whitelist.txt """

  def create_whitelist(self):
    with open("whitelist.txt", "r") as filestream:
      for line in filestream:
        good_lines = []
        for line in lines:
          line = line.strip()
    
          if len(line) == 0:
            pass
          elif line[0] == '#':
            pass
          elif line == '':
            pass
          else:
            good_lines.append(line)
    return good_lines

class WhiteListTest(WhiteList):
  """ Only for testing code.  Not for prod """
  
  def create_whitelist(self, **kwargs):
    return ['cow.cow', 'google.com']
