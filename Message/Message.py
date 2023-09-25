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
  def __init__(self, course_correction_needed, message):
    self.course_correction_needed = course_correction_needed
    self.message = message
    
  @property 
  def message(self):
    return self.message

  @property
  def course_correction_needed(self):
    return self.course_correction_needed
