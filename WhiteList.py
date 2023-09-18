"""
Class for good websites
"""


class WhiteListCoR:
  """ Chain of Responsibility to get correct WhiteList Object"""
  
  def get_object(self, factory_type):
    if factory_type == 'base':
      return WhiteListFromTxt()
    if factory_type == 'test':
      return WhiteListTest()
    else:
      raise Exception(f'{factory_type} not a proper parameter to create WhiteList object.')

class WhiteList:
  """ Creates a list of strings of good websites for browsing"""
  def __init__(self):
    self.whitelist = self.create_whitelist()
  

  def create_whitelist(self, **kwargs) -> list:
    pass

  def website_in_whitelist(self, list_of_current_sites):
    """ checks if all current sites in whitelist """
    for site in list_of_current_sites:
      if sum([sum([white_site.upper().startswith(site.upper()) for white_site in self.whitelist])]) ==0:
        print(f'{site} not found in whitelist')
        return False
    else:
      return True
      
class WhiteListFromTxt(WhiteList):
  """ creates the whitelist of whitelist.txt """

  def create_whitelist(self):
    pass

class WhiteListTest(WhiteList):
  """ Only for testing code.  Not for prod """
  
  def create_whitelist(self, **kwargs):
    return ['cow.cow', 'google.com']
