"""
Runs the StopWastingTime App

How does the StopWastingTime app work?
1) looks at whitelist.txt to find good websites
2) checks the internet every 1 second to see if there exist sites not on the whitelist
  2a)If so, closes all internet browsers
"""
import sleep
from WhiteList import WhiteListCoR
from CheckWebsites import CheckWebsitesCoR
from CourseCorrect import CourseCorrectCoR


whitelist = WhiteListCor('base')
website_checker = CheckWebsitesCoR().get_object('base')
course_correction = CourseCorrectCoR().get_object('delete')

while True:
  if whitelist.website_in_whitelist(website_checker.get_current_websites()):
    pass
  else:
    course_correction.course_correct()

  time.sleep(1.)
