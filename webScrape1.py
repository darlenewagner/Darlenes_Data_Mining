import requests, bs4

res = requests.get('https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

#print(soup.prettify())

print('Page Title: "' + soup.title.string + '"')

print('List of Sections: ')
for section in soup.find_all('section'):
    print('-> ' + section.get('id') + '"')

print('List of Headers: ')
for head1 in soup.find_all('h1'):
    print(head1.get_text())

for head2 in soup.find_all('h2'):
    print(head2.get_text())

