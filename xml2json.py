from bs4 import BeautifulSoup
from yattag import Doc
from yattag import indent
import html, json

from yattag.simpledoc import html_escape

# read xml file
with open("./politik_input.xml") as file:
    soup = BeautifulSoup(file, features="lxml-xml")

items = soup.find_all("item", limit=3)

# create json
data = []

for item in items:
    data.append({
        "headline": item.find('title').string,
        "subline": item.find('welt:topic').string,
        "text": html.escape(item.find('description').string),
        "img": html.escape("https://weltooh.de/main/img736x414/some_generated_img.jpg"),
        "source": f"Quelle: {item.find('dc:source').string}",
        "video": ""
        })

# write json
with open('my_output_py.json', 'w') as f:
    json.dump(data, f, indent=2)
    print("New json file is created")

