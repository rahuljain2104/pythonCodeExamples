import xml.etree.ElementTree as ET
import urllib

data = '''
        <persons>
            <person>
                <name>Rahul Jain</name>
                <profession type="student">engineer</profession>
            </person>
            <person>
                <name>Mohit Jain</name>
                <profession type="all rounder">business person</profession>
            </person>
            <person>
                <name>Rishabh Jain</name>
                <profession type="ideal">business guy</profession>
            </person>
        </persons>
       '''

sample = "http://python-data.dr-chuck.net/comments_42.xml"  # (Sum=2553)
actual_data = "http://python-data.dr-chuck.net/comments_340268.xml"  # (Sum ends with 36)

data = urllib.urlopen(actual_data).read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
s = 0
for items in lst:
    s += int(items.find('count').text)

print s
