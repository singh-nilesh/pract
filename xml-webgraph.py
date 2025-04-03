import csv
import requests
import xml.etree.ElementTree as ET

# Function to load the RSS feed and save it to local file
def load_rss( url, filename):
    resp = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(resp.content)
    print( f" RSS feed loaded to {filename}")
    
# Function to pare the XML file
def parse_xml( xmlfile ):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems =[]
    
    for item in root.findall('.//item'):
        news = {child.tag: child.text for child in item if not child.tag.endswith(('thumbnail', 'content'))}
        media = next (child.attrib['url'] for child in item if child.tag.endswith('content')), 