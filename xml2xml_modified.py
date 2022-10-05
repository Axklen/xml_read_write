from bs4 import BeautifulSoup
from yattag import Doc
from yattag import indent
import html

# read xml file
with open("./politik_input.xml") as file:
    soup = BeautifulSoup(file, features="lxml-xml")

items = soup.find_all("item", limit=3)

# create xml
doc, tag, text, line = Doc().ttl()
doc.asis('<?xml version="1.0" encoding="UTF-8"?>')
with tag('n24news'):
    for item in items:
        with tag('news'):
            with tag('subline'):
                text(item.find('welt:topic').string)
            with tag('headline'):
                text(item.find('title').string)
            with tag('source'):
                text(f"Quelle: {item.find('dc:source').string}")
            with tag('textmessage'):
                text(html.escape(item.find('description').string))
            with tag('published', type='timestamp'):
                text(item.find('pubDate').string)
            with tag('image', type='remotefile'):
                text('https://weltooh.de/main/img736x414/some_generated_image.jpg')
            doc.stag('thumb', type='timestamp')
            doc.stag('video', type='timestamp')
            with tag('webUrl'):
                text(html.escape(item.find('link').string))

result = indent(
    doc.getvalue(),
    indentation = '    ',
    newline = '\n',
    # indent_text = True
)

# write xml file
with open('my_output_py.xml', "w") as file:
    file.write(result)

print(result)
