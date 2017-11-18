---
layout: post
title: "Chapter 5: Scrape a Website with a Frontend API"
---


We will discuss how to scrape a website that has a frontend API. Newer websites have began to separate their frontend and backend which communicate through an API. This allows for developers to work more independently, however it also allows web scrapers much easier access to their data.


## [Needed Items]({{ site.baseurl }}/building-a-webscraper-chapter-1)

- Google Chrome
- `requests`
- `xmltodict`
- Know how to [inspect a page]({{ site.baseurl }}/building-a-webscraper-chapter-2) in Google Chrome

## Case Study: DePaul University Course Catalog

### Before Writing Code: Analyze Network Traffic 

1\. Navigate to the following **[url](https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx)** with JavaScript turned **on** and **[inspect the page]({{ site.baseurl }}/building-a-webscraper-chapter-2)**. 

2\. Change the tab from **Elements** to **Network** because now we are interested in the network activity of the website. ![]({{ site.baseurl }}/images/chapter5/1.png "image")

3\. Reload the page. You will now see a lot of files/scripts in the network window. ![]({{ site.baseurl }}/images/chapter5/2.png "image")

4\. We are not interested in all of these. We are only interested in a certain type of file: **XHR**. Change the tab to **XHR** to see all **XMLHttpRequest's.** ![]({{ site.baseurl }}/images/chapter5/3.png "image")

5\. There is one request called **Lists.asmx**. After clicking on it and expanding out the XML, this is what we see. This seems to be the data that we are seeing on the page except coming from the **frontend API**. ![]({{ site.baseurl }}/images/chapter5/4.png "image")


### Let's Write Some Code

1\. We will use a tool that will convert this request into Python code, I call it [cURL to Python](https://curl.trillworks.com/). Let's copy this request as a cURL. ![]({{ site.baseurl }}/images/chapter5/5.png "image")

2\. Let's paste this request into [cURL to Python](https://curl.trillworks.com/) and copy the Python code generated. ![]({{ site.baseurl }}/images/chapter5/6.png "image")

```python
import requests

cookies = {
    '_ceg.s': 'oyg3ny',
    '_ceg.u': 'oyg3ny',
    'depaul.edu': 'datakey=db8321bb-ad00-4755-aed2-14cd059803b2&videokey=6aee44ac-78af-4b2d-b41a-27effbf73772&lectureid=300584',
    '_ga': 'GA1.2.2031229303.1508968351',
    '_gid': 'GA1.2.1097033466.1509740332',
    '__utmt_globalTracker': '1',
    '__utmt_siloTracker': '1',
    '__utma': '49792185.2031229303.1508968351.1509754293.1509760156.4',
    '__utmb': '49792185.4.10.1509760156',
    '__utmc': '49792185',
    '__utmz': '49792185.1509760156.4.4.utmcsr=localhost:4000|utmccn=(referral)|utmcmd=referral|utmcct=/building-a-webscraper-chapter-5',
}

headers = {
    'Pragma': 'no-cache',
    'Origin': 'https://www.depaul.edu',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    '$Content-Type': 'text/xml;charset=\'UTF-8\'',
    'Accept': 'application/xml, text/xml, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx',
}

data = '$<soap:Envelope xmlns:xsi=\'http://www.w3.org/2001/XMLSchema-instance\' xmlns:xsd=\'http://www.w3.org/2001/XMLSchema\' xmlns:soap=\'http://schemas.xmlsoap.org/soap/envelope/\'><soap:Body><GetListItems xmlns=\'http://schemas.microsoft.com/sharepoint/soap/\'><listName>Courses</listName><viewName></viewName><query><Query><Where><Eq><FieldRef Name=\'SUBJECT_NAME\'/><Value Type=\'Text\'><![CDATA[Accountancy]]></Value></Eq></Where><OrderBy><FieldRef Name=\'SUBJECT\' Ascending=\'True\' /><FieldRef Name=\'CATALOG_NBR\' Ascending=\'True\' /></OrderBy></Query></query><viewFields><ViewFields><FieldRef Name=\'Title\' /><FieldRef Name=\'SUBJECT\' /><FieldRef Name=\'CATALOG_NBR\' /><FieldRef Name=\'ACAD_CAREER\' /><FieldRef Name=\'DESCR\' /><FieldRef Name=\'Prerequisites\' /></ViewFields></viewFields><rowLimit>0</rowLimit><queryOptions><QueryOptions></QueryOptions></queryOptions></GetListItems></soap:Body></soap:Envelope>'

requests.post('https://www.depaul.edu/university-catalog/_vti_bin/Lists.asmx', headers=headers, cookies=cookies, data=data)
```

3\. Let's clean up the code block above, removing unneeded information. Through trial and error, I have removed all cookies and all but one of the headers to simplify the code a bit. **NOTE: After running once, a reformatting of the data variable was needed before depaul.edu would accept it.** Below is what the code looks like after reformatting.
```python
"""Import requests and xmltoduct
These will be contained in the env/ folder.
"""
import requests

"""The following url, headers and data come from analyzing the network activity of the website."""
url = 'https://www.depaul.edu/university-catalog/_vti_bin/Lists.asmx'
headers = {'Content-Type': "text/xml;charset='UTF-8'"}
data = '''<soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
            <soap:Body>
                <GetListItems xmlns='http://schemas.microsoft.com/sharepoint/soap/'>
                    <listName>Courses</listName>
                    <viewName></viewName>
                    <query>
                        <Query></Query>
                    </query>
                    <viewFields>
                        <ViewFields>
                            <FieldRef Name='Title' />
                            <FieldRef Name='SUBJECT' />
                            <FieldRef Name='CATALOG_NBR' />
                            <FieldRef Name='ACAD_CAREER' />
                            <FieldRef Name='DESCR' />
                            <FieldRef Name='Prerequisites' />
                        </ViewFields>
                    </viewFields>
                    <rowLimit>0</rowLimit>
                    <queryOptions>
                        <QueryOptions></QueryOptions>
                    </queryOptions>
                </GetListItems>
            </soap:Body>
        </soap:Envelope>'''
"""Send the data along with the headers to the url found while looking at the XHR reqquests."""
payload = requests.post(url, headers=headers, data=data).content
```

4\. (Optional) Currently sitting in the payload variable is the XML we saw at **step 5**. This is hard to work with in Python so let's convert it into a structure that is easier to work with. Using the code below, we iterate through all courses, creating a list of tuples representing the response from depaul.edu. 

```python
"""Parse the content returned. In this case, the path is complex so trial and error works best."""
import xmltodict
class_list = xmltodict.parse(payload)['soap:Envelope']['soap:Body']['GetListItemsResponse']['GetListItemsResult']['listitems']['rs:data']['z:row']

"""Format the response payload into a data structure that would want to be used later."""
courses = []
for c in class_list:
    courses.append([
            c['@ows_Title'].title(),
            c.get('@ows_SUBJECT'),
            c.get('@ows_CATALOG_NBR'),
            c.get('@ows_ACAD_CAREER'),
            c.get('@ows_DESCR'),
            c.get('@ows_Prerequisites'),
            c.get('@ows_Modified'),
            c.get('@ows_Created')
        ])
print courses
```


### Complete Script
```python
"""Import requests and xmltoduct
These will be contained in the env/ folder.
"""
import requests
import xmltodict

"""The following url, headers and data come from analyzing the network activity of the website."""
url = 'https://www.depaul.edu/university-catalog/_vti_bin/Lists.asmx'
headers = {'Content-Type': "text/xml;charset='UTF-8'"}
data = '''<soap:Envelope xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
            <soap:Body>
                <GetListItems xmlns='http://schemas.microsoft.com/sharepoint/soap/'>
                    <listName>Courses</listName>
                    <viewName></viewName>
                    <query>
                        <Query></Query>
                    </query>
                    <viewFields>
                        <ViewFields>
                            <FieldRef Name='Title' />
                            <FieldRef Name='SUBJECT' />
                            <FieldRef Name='CATALOG_NBR' />
                            <FieldRef Name='ACAD_CAREER' />
                            <FieldRef Name='DESCR' />
                            <FieldRef Name='Prerequisites' />
                        </ViewFields>
                    </viewFields>
                    <rowLimit>0</rowLimit>
                    <queryOptions>
                        <QueryOptions></QueryOptions>
                    </queryOptions>
                </GetListItems>
            </soap:Body>
        </soap:Envelope>'''
"""Send the data along with the headers to the url found while looking at the XHR reqquests."""
payload = requests.post(url, headers=headers, data=data).content

"""Parse the content returned. In this case, the path is complex so trial and error works best."""
class_list = xmltodict.parse(payload)['soap:Envelope']['soap:Body']['GetListItemsResponse']['GetListItemsResult']['listitems']['rs:data']['z:row']

"""Format the response payload into a data structure that would want to be used later."""
courses = []
for c in class_list:
    courses.append([
            c['@ows_Title'].title(),
            c.get('@ows_SUBJECT'),
            c.get('@ows_CATALOG_NBR'),
            c.get('@ows_ACAD_CAREER'),
            c.get('@ows_DESCR'),
            c.get('@ows_Prerequisites'),
            c.get('@ows_Modified'),
            c.get('@ows_Created')
        ])
print courses

```


## Helpful Links
- Download the completed scraper: [chapter5.py]({{ site.baseurl }}/sample-scripts/chapter5.py)
- [cURL to Python](https://curl.trillworks.com/)


## Checklist Before Completing the Chapter
- I have a Python Script that can circumnavigate a website and access its API directly
- I understand how to interact with this data after storing it in a variable
