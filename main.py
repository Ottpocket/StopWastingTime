"""
Runs the StopWastingTime App

How does the StopWastingTime app work?
1) looks at whitelist.txt to find good websites
2) checks the internet every 1 second to see if there exist sites not on the whitelist
  2a)If so, closes all internet browsers
"""
import sys
for directory in ['WhiteList', 'CourseCorrect', 'TimedIterator', 'WebsiteChecker']:
  sys.path.append(directory)
from WhiteList import WhiteListCoR
from CourseCorrect import CourseCorrectCoR
from WebsiteChecker import WebsiteCheckerCoR
from TimedIterator import TimedIteratorCoR



whitelist = WhiteListCoR().get_object('pids')
website_checker = WebsiteCheckerCoR().get_object('pids')
course_correction = CourseCorrectCoR().get_object('pids')
timed_iterator = TimedIteratorCoR().get_object(8 * 60 * 60) #~8 hours 

for _ in timed_iterator:
  message =  whitelist.website_in_whitelist(website_checker.get_current_websites())
  if message.course_correction_needed:
    course_correction.course_correct(message)
    timed_iterator.inform_on_intervals()

