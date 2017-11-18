"""Import BeautifulSoup and requests
These will be contained in the env/ folder.
"""
from BeautifulSoup import BeautifulSoup as Soup
import requests

"""1) Get the content using the requests library
2) Parse the HTML with BeautifulSoup
3) Ask BeautifulSoup to give us all a tags with class 'courseLink'
4) Return a de-nullified list of courses
"""
url = ('http://www.depaul.edu/university-catalog/academic-handbooks/'
            'undergraduate/university-information/liberal-studies-program/'
            'liberal studies learning domains/Pages/arts-and-literature.aspx')
html = requests.get(url).content
soup = Soup(html)
courses = []
for a in soup.findAll('a', {'class':'courseLink'}):
    courses.append(a.text)
print filter(None, courses)
