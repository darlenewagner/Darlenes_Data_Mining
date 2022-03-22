import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.ncbi.nlm.nih.gov/'
url2 = 'https://www.gatech.edu/'
#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#res = urllib.request.urlopen(url).read().decode('utf-8')
res = requests.get(url2)
#charset = res.info().get_content_charset()
#content = req.read().decode(charset)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

for header in soup.find_all(re.compile("^h\d")):
    print(header.get_text())
