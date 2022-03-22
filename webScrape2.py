import requests, bs4

res = requests.get('https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

#print(soup.prettify())

print('Page Title: "' + soup.title.string + '"')

print('List of Sections: ')
for section in soup.find_all('section'):
    print('-> ' + section.get('id') + '"')
    print('   Section Content:  ')
    for child in section.children:
        #print('----> ', child.string)
        for stringer in child.stripped_strings:
            print('----> ' + repr(stringer))


