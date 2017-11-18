---
layout: post
title: "Chapter 4: Scrape a JavaScript Generated Website"
---

In this chapter, we will discuss how to scrape a JavaScript generated website. Not all websites are static, they may change as a user interacts with them. The scraper will become a little more complicated because we must replace `requests` with `Selenium`.




<!-- Each chapter needs specific software or python packages, this is where they go. -->

## [Needed Items]({{ site.baseurl }}/building-a-webscraper-chapter-1)
- Google Chrome
- Firefox
- `Selenium`
- `BeautifulSoup`
- Know how to [turn off JavaScript]({{ site.baseurl }}/building-a-webscraper-chapter-2) in Google Chrome




<!-- The actual tutorial explaining things. -->

## Case Study: DePaul University Course Catalog

Sanity Check: Navigate to this [url](https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx) and [turn off JavaScript]({{ site.baseurl }}/building-a-webscraper-chapter-2). Confirm that what you see matches the image below. ![]({{ site.baseurl }}/images/chapter4/1.png "image") _The content is gone which is an indicator that the content was generated using JavaScript._


### Before Writing Code: Find the HTML Tag



<!-- Step 1 -->
1\. Navigate to the following **[url](https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx)** with JavaScript turned **on** and **[inspect the page]({{ site.baseurl }}/building-a-webscraper-chapter-2)**. 

<!-- Step 2 -->
2\. Select the **small square** in the upper left of the window such that it turns **blue**. **Hover** over the HTML you want to scrape and **click**. The HTML of that element will appear in the inspect window. ![]({{ site.baseurl }}/images/chapter4/2.png "image")
_In this example, we hovered over and clicked the element containing "**ACC 101.**" We will use the information about this tag (i.e. **class**) to scrape the contents of all courses on this page._

```html
<!-- The selected tag -->
<span class="subject">ACC 101</span>
```





### Let's Write Some Code

1\. Import the needed python packages: `Selenium` and `BeautifulSoup`.
- `Selenium` - get the HTML from the JavaScript generated page
- `BeautifulSoup` - transform the page HTML into a structured tree

```python
from BeautifulSoup import BeautifulSoup as Soup
from selenium import webdriver
```

2\. Open Firefox and get the url. Store the page HTML, then close Firefox.

```python
driver = webdriver.Firefox()
driver.get("https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx")
html = driver.page_source
driver.close()
```

3\. Parse the HTML with BeautifulSoup then ask for all span's with class `subject`. We know we want this class because of what we did **Before Writing Code**.

```python
soup = Soup(html)
subjects = []
for span in soup.findAll('span',{'class':'subject'}):
    subjects.append(span.text)
```

_**NOTE: There is a problem with this code. We only get subjects that begin with the letter 'A.' What if we want all subjects? This is where we must start programmatically interacting with the website.**_









### Let's Do Better

Note: We will modify our code such that the Firefox browser doesn't close until it has selected and scraped **all** courses on the page.

1\. Import the needed python packages (same as before): **Selenium** and **BeautifulSoup**.

```python
from BeautifulSoup import BeautifulSoup as Soup
from selenium import webdriver
```

2\. Open Firefox and get the url **however**, don't do anything else, keep it open.

```python
driver = webdriver.Firefox()
driver.get("https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx")
```


3\. Find the tags that contain the letters we want `Selenium` to click on. ![]({{ site.baseurl }}/images/chapter4/3.png "image")

```html
<!-- The tag for the 'C' in the navigation bar. -->
<ul class="tabs a-z-courses" id="letterBank">
    <li class="tab-mid">
        <a onclick="..." id="..." class="AZLetter" href='...'>C</a>
    </li>
</ul>
```


4\. Let's use `BeautifulSoup` to store the ids of all tags that `Selenium` needs to click in order to scrape all subjects. 

```python
to_click_ids = []
html = driver.page_source
soup = Soup(html)
ul_tag = soup.find('ul', {'id':'letterBank'})
for a in ul_tag.findAll('a', {'class':'AZLetter'}):
    to_click_ids.append(a['id'])
``` 
_Note: All letters are contained in an "a" tag, all of which are contained in an "ul" tag.
If we can get the "ul" tag, then ask for all of their "a" tags, then we will know what tags to tell `Selenium` to click._ 

4\. Let's tell Selenium to click each of the tags we just collected and scrape **all** the subjects for each.

```python
subjects = []
for i in to_click_ids:
    driver.find_element_by_id(i).click()
    html = driver.page_source
    soup = Soup(html)
    for span in soup.findAll('span',{'class':'subject'}):
        subjects.append(span.text)
print subjects
```

### Complete Script
```python
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
```




<!-- Helpful Links Section -->

Helpful Links
- Download the completed scraper: [chapter4.py]({{ site.baseurl }}/sample-scripts/chapter4.py)
- [Selenium Cheat Sheet](http://akul.me/blog/2016/selenium-cheatsheet/)




<!-- Checklist to confirm the reader successfully finished the chapter -->

**Checklist Before Completing the Chapter**
- I have a python script that can programmatically parse a JavaScript HTML page 
- My script can interact with the browser to initialize the JavaScript generation
- My script can return the content I am interested in
