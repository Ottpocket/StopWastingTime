# StopWastingTime
A program to give popups if I am wasting time on the internet

### Important Notes
Unless the Lord builds the house/pgm, they labor in vain who build it.
Unless the Lord guards the city/browser, the watchmen stay awake in vain.

### Next Steps
At pgm start, find time of last chrome pid
Delete each subsequent new pid 
> get-process | select name, starttime | findstr chrome
> 
> PS C:\Users\aott py ./subprocess_check.py
>
Then kill the tasks w/ `taskkill /F /PID *PIDNumber*`.

### Adding Popups
https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
