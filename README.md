# StopWastingTime
A program to give popups if I am wasting time on the internet

### Next Steps
At pgm start, find time of last chrome pid
Delete each subsequent new pid 
> get-process | select name, starttime | findstr chrome

### Adding Popups
https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
