import subprocess
import sys
import time

sys.path.append('..')
from StopWastingTime.Communication.Communication import CommunicationCoR

#Kicking off program as background process
with open('dump.txt', 'w') as f:
  subprocess.Popen(['powershell', 'py', 'main.py'], 
                    stdout=f, stderr=subprocess.STDOUT)

while True:
  comm = CommunicationCoR().get_object()
  time_to_rest = int(input("Enter minutes to use new internet: "))
  print(f'Resting for {time_to_rest} minutes')
  comm.clean_file()
  comm.write_message(time_to_rest )
  time.sleep(time_to_rest*60)
  print(f'Cannot kill for {time_to_rest} mintutes')