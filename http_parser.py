from bs4 import BeautifulSoup

html_file = open("test.html", "r")

source_code = html_file.read()

soup = BeautifulSoup(source_code, 'html.parser')

_title = soup.title.string
_content = soup.content.string
_name = soup.find('name').string
_receiver = soup.receiver.string
_job = soup.receiver.string

print(_title, _content, _name, _receiver, _job)