from bs4 import BeautifulSoup
import html, json

INPUT_FILE = "politik_input.xml"
OUTPUT_FILE = "my_output_py.xml"

# read xml file
with open(INPUT_FILE) as file:
    soup = BeautifulSoup(file, features="lxml-xml")

items = soup.find_all("item", limit=3)

# create json
data = []

for item in items:
    data.append(
        {
            "headline": item.find("title").string,
            "subline": item.find("welt:topic").string,
            "text": html.escape(item.find("description").string),
            "img": html.escape(
                "https://weltooh.de/main/img736x414/some_generated_img.jpg"
            ),
            "source": f"Quelle: {item.find('dc:source').string}",
            "video": "",
        }
    )

# write json
with open(OUTPUT_FILE, "w") as f:
    json.dump(data, f, indent=2)
    print(f"New json file is created: {OUTPUT_FILE}")
