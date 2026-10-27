import requests
from _config import getPath

url = "https://raw.githubusercontent.com/Phoenix-Programming/web-scraping-workshop/refs/heads/main/example-files/index.html"

# open the file, write contents we get from the URL into the file
# The idea is to only send as many requests as are necessary. We can cache
# results instead of constantly requesting it from the server (especially when
# testing or debugging code).
with open(getPath("example.html"), 'w') as example:
    example.write(requests.get(url).text)
