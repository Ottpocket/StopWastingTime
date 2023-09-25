"""
Classes for getting current pids
"""
import platform
from abc import ABC, abstractmethod
import subprocess



class GetPids(ABC):
  """ Abstract class to get all running pids from a browser"""

  @abstractmethod
  def get_pids(self, browser) -> list:
    return []

class GetPidsWindows(GetPids):
  """ Gets all pids from a browser in windows os"""

  def get_pids(self, browser):
    #System call
    call = f"powershell get-process {browser} ^| Format-Table Id"
    process = subprocess.Popen(call, stdout=subprocess.PIPE, stderr=None, shell=True)
    outputs = process.communicate()[0].decode('utf-8').split('\n')
    outputs = [output.strip().split() for output in outputs]
    
    #Parsing throught the strings in each line of the output
    pids = []
    for strs in outputs:
      if len(strs) == 1:
        pid = strs[0]
        try:
          pid = int(pid)
          pids.append(pid)
        except ValueError:
          pass
    return pids

class GetPidsFactory:
  """ Factory method """
  def get_object(self):
    if platform.system() == "Windows":
      return GetPidsWindows()
    else:
      msg= """
      ERROR:
      Only works for Windows now.  To add other operating systems,
      subclass GetPids for that os and add it to the GetPidsFactory
      class."""
      raise Exception(msg)

