"""
Classes of object that cause the checker to pause for certain amounts of time
"""
import time
import datetime
from StopWastingTime.Communication.Communication import CommunicationCoR
from abc import ABC, abstractmethod

class PauseCoR():
  def get_object(self, object_type=None):
    if object_type is None:
      return PauseFromTxt()

class Pause(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def check_for_updates(self):
    pass  
  
  def get_message(self):
    pass

  def pause(self, minutes):
    time.sleep(minutes * 60)

  def reset_pause(self, minutes):
    pass  
  
  def reset_message(self):
    pass


class PauseFromTxt(Pause):
  """ Pauses program N minutes, then becomes unpauseable for N minutes  """
  def __init__(self, communication=None):
    """ """
    self.do_not_start_until = datetime.datetime.now()
    self.communication_method = CommunicationCoR().get_object(communication)
  
  def done_waiting(self):
    """ checks that we can begin checking for messages after stop """
    return datetime.datetime.now() > self.do_not_start_until
    
  def check_for_updates(self):
    return self.communication_method.exists_new_updates()
  
  def get_message(self):
    msg = self.communication_method.get_message()
    if msg == '':
      return 0
    elif len(msg) == 1:
      return int(msg)
    else:
      error = f"""
      ERROR: message must be 1 unit long.  Received:
      {msg}
      """
      raise Exception(error)
  def reset_message(self):
    return self.communication_method.reset_message()
     
  def reset_pause(self, minutes):
    if type(minutes) == str:
      minutes = int(minutes)
    self.do_not_start_until = datetime.datetime.now() + datetime.timedelta(minutes=minutes)