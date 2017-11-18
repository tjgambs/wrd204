---
layout: post
title: "Chapter 3: Scrape a Static HTML Website"
---

In this chapter, we will discuss how to scrape a static HTML website. A static HTML website is one where the content on the page never changes. The scraper simply looks at an HTML path then pulls out its information.




<!-- Each chapter needs specific software or python packages, this is where they go. -->

## [Needed Items]({{ site.baseurl }}/building-a-webscraper-chapter-1)
- Google Chrome
- `requests`
- `BeautifulSoup`
- Know how to [inspect a page]({{ site.baseurl }}/building-a-webscraper-chapter-2) in Google Chrome




<!-- The actual tutorial explaining things. -->

## Case Study: DePaul University Arts & Literature Courses 

### Before Writing Code: Find the HTML Tag


<!-- Step 1 -->
1\. Navigate to the following **[url](https://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/arts-and-literature.aspx)** and **[inspect the page]({{ site.baseurl }}/building-a-webscraper-chapter-2)**. 

<!-- Step 2 -->
2\. Select the **small square** in the upper left of the window such that it turns **blue**. **Hover** over the HTML you want to scrape and **click**. The HTML of that element will appear in the inspect window. ![]({{ site.baseurl }}/images/chapter3/3.png "image") 
_In this example, we hovered over and clicked the element containing "**ABD 221 ROMANCE, GENDER, AND RACE.**" We will use the information about this tag (i.e. **class** and **id**) to scrape the contents of all courses on this page._

```html
<!-- The selected tag -->
<a id="l249-c014074" class="courseLink">ABD 221 ROMANCE, GENDER, AND RACE</a>
```


### Let's Write Some Code


1\. Import the needed python packages: `requests` and `BeautifulSoup`.
- `requests` - asks the URL for the page HTML
- `BeautifulSoup` - transforms the page HTML into a structured tree

```python
from BeautifulSoup import BeautifulSoup as Soup
import requests
```

2\. Get the page HTML using the `requests` library.

```python
url = ('http://www.depaul.edu/university-catalog/academic-handbooks/'
            'undergraduate/university-information/liberal-studies-program/'
            'liberal studies learning domains/Pages/arts-and-literature.aspx')
html = requests.get(url).content
```

3\. Convert the HTML into a structured tree with `BeautifulSoup`

```python
soup = Soup(html)
```

4\. Ask `BeautifulSoup` to `findAll` tags with a class of `courseLink`, then add the text of each tag to a list.

```python
courses = []
for a in soup.findAll('a', {'class':'courseLink'}):
    courses.append(a.text)
```

5\. Before completing the script, we want to filter out empty strings from the list. 

```python
filter(None, courses)
```

### Complete Script

```python
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
```



<!-- Helpful Links Section -->

## Helpful Links
- Download the completed scraper: [chapter3.py]({{ site.baseurl }}/sample-scripts/chapter3.py)
- [BeautifulSoup Cheat Sheet](http://akul.me/blog/2016/beautifulsoup-cheatsheet/)



<!-- Checklist to confirm the reader successfully finished the chapter -->

## Checklist Before Completing the Chapter
- I have a python script that can programmatically parse an HTML page 
- My script can return the content I am interested in
