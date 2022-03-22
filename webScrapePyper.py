import re
import requests
import pyperclip
from bs4 import BeautifulSoup

viewSource = pyperclip.paste()

soup = BeautifulSoup(viewSource, "html.parser")

for header in soup.find_all(re.compile("^h\d")):
    print(header.get_text())

