
from bs4 import BeautifulSoup

html = """<html><head></head><body>
<h1>Hamlet</h1>
<h3>dramatis personae</h3>
<ul class="cast"> 
  <li>Hamlet</li>
  <li>Polonius</li>
  <li>Ophelia</li>
  <li>Claudius</li>
</ul>
</body></html"""

soup = BeautifulSoup(html, "lxml")

for ul in soup.find_all('ul'):
    if "cast" in ul.get('class', []):
        for item in ul.find_all('li'):
            print(item.get_text(), end=", ")
