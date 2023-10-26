"""
Implements the communication protocals for checking outside messages
"""
from abc import ABC, abstractmethod
import os

class CommunicationCoR:
  def get_object(self, type_of_object = None):
    if type_of_object is None:
      return CommunicationTxt(file = 'communication.txt')
    elif type_of_object[-4:] == '.txt':
      return CommunicationTxt(file = type_of_object)


class Communication:
  """ abstract protocol for receiving communication outside main.py """
  def __init__(self):
    pass

  @abstractmethod
  def exists_new_updates(self):
     pass
  
  @abstractmethod
  def get_message(self):
    pass

  @abstractmethod
  def reset_message(self):
    pass

class CommunicationTxt(Communication):
  """ Receives outside communication via  `file`

  `file` is a `.txt` files with a single line with a single number.
  If `file` is different, an exception is thrown. 
  """
  def __init__(self, file):
    self.file = file
    self.clean_file()

  def clean_file(self):
    """ deletes the file, then replaces with blank placeholder """
    if os.path.exists(self.file):
      os.remove(self.file)
    with open(self.file, 'w') as fp: 
      pass

  def exists_new_updates(self):
    """ checks if `file.txt` is blank or not """
    return '' != self.get_message()    
 
  def get_message(self):
    line = ""
    with open(self.file, 'r') as f:
      for line in f.readlines():
        pass
    return line
 
  def reset_message(self):
    self.clean_file()

  def write_message(self, msg):
    if type(msg) == int:
      msg = str(msg)
    if (len(msg) > 1) and (msg not in ['i' for i in range(1,11)]):
      error = f"""
      ERROR: Message must be a single integer.  Message received:
      {msg}
      """
      raise Exception(error)

    self.clean_file()
    with open(self.file, 'w') as f: 
      f.write(msg)