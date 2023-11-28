"""
Kills all websites found on `blacklist.txt`
"""
import sys
sys.path.append('..')
from StopWastingTime.WhiteList.WhiteList import WhiteListCoR
from StopWastingTime.CourseCorrect.CourseCorrect  import CourseCorrectCoR
from StopWastingTime.WebsiteChecker.WebsiteChecker import WebsiteCheckerCoR
from StopWastingTime.TimedIterator.TimedIterator import TimedIteratorCoR
from StopWastingTime.Pause.Pause import PauseCoR


whitelist = WhiteListCoR().get_object('pids')
website_checker = WebsiteCheckerCoR().get_object('pids')
course_correction = CourseCorrectCoR().get_object('pids')
timed_iterator = TimedIteratorCoR().get_object(-1) #infinite
pause = PauseCoR().get_object() 

for _ in timed_iterator:
  message =  whitelist.website_in_whitelist(website_checker.get_current_websites())
  if message.course_correction_needed:
    course_correction.course_correct(message)
    timed_iterator.inform_on_intervals()

  #checking if update has been communicated to the system from outside
  #Will pause system for N minutes, then prevent pauses for N minutes afterwards
  if pause.done_waiting():
    if pause.check_for_updates():
      minutes_to_pause = pause.get_message()
      print(f'Pausing app for {minutes_to_pause} minutes')
      pause.pause(minutes_to_pause)
      pause.reset_pause(minutes_to_pause)
      pause.reset_message()