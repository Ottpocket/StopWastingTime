"""
Class designed to report 
1) if any bad websites/pids found and 
2) specific bad websites/pids
"""


class Message():
  """
  Message objects created by WhiteList objects to
  state if currentsites not currently in whitelist
  """
  def __init__(self, message):
    """ Message is browser:bad_site dict """
    self._message = message
    self._course_correction_needed = False
    for _, bad_websites in message.items():
      if len(bad_websites) > 0:
        self._course_correction_needed = True 
      
  def set_message(self, message):
    self.message = message
    
  @property 
  def message(self):
    return self._message

  @property
  def course_correction_needed(self):
    return self._course_correction_needed
