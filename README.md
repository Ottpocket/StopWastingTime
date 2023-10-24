# StopWastingTime
A program to delete new windows in web browsers.  

### System reqs 
1. Only works in Windows currently.
2. python 3. needed

### Using
in cmd
> git clone https://github.com/Ottpocket/StopWastingTime.git
> cd StopWastingTime
> py main.py

This will start the program for 8 hours.  If you desire to terminate it before this, simply
> get-process py | format-table pids
(find the pid for this process)
> killtask \F \PIDS <pid for this task>

### Important Notes
Unless the Lord builds the house/pgm, they labor in vain who build it.
Unless the Lord guards the city/browser, the watchmen stay awake in vain.

### Next Steps
1) Make this app a gui for ease of use.
2) Inside gui, have **Halt for N minutes** option: 
2a) pgm saves PIDS
2b) halts the deletion for N minutes
2c) after N minutes, it takes N minutes to repeat this process

Alternative: Find out how to install selenium and get back to that sweet sweet whitelist https://www.geeksforgeeks.org/opening-and-closing-tabs-using-selenium/
