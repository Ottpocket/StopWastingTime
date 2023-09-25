"""
Runs the StopWastingTime App

How does the StopWastingTime app work?
1) looks at whitelist.txt to find good websites
2) checks the internet every 1 second to see if there exist sites not on the whitelist
  2a)If so, closes all internet browsers
"""
import sleep
from WhiteList import WhiteListCoR
from CourseCorrect import CourseCorrectCoR
from WebsiteChecker import WebsiteCheckerCoR
from TimedIterator import TimedIteratorCoR


whitelist = WhiteListCor('base')
course_correction = CourseCorrectCoR().get_object('delete')
website_checker = WebsiteCheckerCoR().get_object('pids') #TODO: write this!
timed_iterator = TimedIteratorCoR().get_object('base') #TODO: write this

for timed_iterator:
  message =  whitelist.website_in_whitelist(website_checker.get_current_websites())
  if message.need_course_correction():
    course_correction.course_correct(message)

