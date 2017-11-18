"""Import BeautifulSoup and Selenium
These will be contained in the env/ folder.
"""
from BeautifulSoup import BeautifulSoup as Soup
from selenium import webdriver


"""Start the firefox browser and navigate to the url."""
driver = webdriver.Firefox()
driver.get("https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx")

"""Get all of the a tags that need to be clicked by Selenium
in order for you to be able to scrape all of the subjects.
"""
to_click_ids = []
html = driver.page_source
soup = Soup(html)
ul_tag = soup.find('ul', {'id':'letterBank'})
for a in ul_tag.findAll('a', {'class':'AZLetter'}):
	to_click_ids.append(a['id'])

"""Tell the driver to click on each of these elements and parse
the javascript generated html.
"""
subjects = []
for i in to_click_ids:
	driver.find_element_by_id(i).click()
	html = driver.page_source
	soup = Soup(html)
	for span in soup.findAll('span',{'class':'subject'}):
	    subjects.append(span.text)
print subjects

"""Close firefox."""
driver.close()
