from bs4 import BeautifulSoup, Tag
from _config import getPath

# If it can't find the file make sure to run 00-example-download.py

# use the cached file and print it out
example_doc = open(getPath("example.html"), encoding="utf-8").read()
print(example_doc)

# soup time
soup = BeautifulSoup(example_doc, "html.parser")

# get the first header
# the reason we have to check if it exists is because the website could have
# changed (we cannot expect or guarantee that a header element will exist)
h1Elem = soup.find("h1")
if h1Elem is not None:
    print(h1Elem.text) # should print Good morning!

# second row, first column
trElems = soup.find_all("tr")
print(trElems[1].find_all("td")[0].text) # should print Python

aElem = soup.find("a")
if isinstance(aElem, Tag):
    print(aElem["href"]) # prints the URL of a cool YouTube video
