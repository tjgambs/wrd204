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
