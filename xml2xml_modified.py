from bs4 import BeautifulSoup
from yattag.doc import Doc
from yattag.indentation import indent
import html

INPUT_FILE = "politik_input.xml"
OUTPUT_FILE = "my_output_py.xml"

# read xml file
def read_xml_file(filename) -> BeautifulSoup:
    with open(filename) as file:
        soup = BeautifulSoup(file, features="lxml-xml")
    return soup


# create xml
def gen_new_xml(items: list) -> list:
    doc, tag, text, line = Doc().ttl()
    doc.asis('<?xml version="1.0" encoding="UTF-8"?>')

    with tag("n24news"):
        for item in items:
            with tag("news"):
                with tag("subline"):
                    text(item.find("welt:topic").string)
                with tag("headline"):
                    text(item.find("title").string)
                with tag("source"):
                    text(f"Quelle: {item.find('dc:source').string}")
                with tag("textmessage"):
                    text(html.escape(item.find("description").string))
                with tag("published", type="timestamp"):
                    text(item.find("pubDate").string)
                with tag("image", type="remotefile"):
                    text("https://weltooh.de/main/img736x414/some_generated_image.jpg")
                doc.stag("thumb", type="timestamp")
                doc.stag("video", type="timestamp")
                with tag("webUrl"):

                    text(html.escape(item.find("link").string))
    result = indent(
        doc.getvalue(),
        indentation="    ",
        newline="\n",
        # indent_text = True
    )
    return result


# write xml file
def write_json_file(data) -> None:
    with open(OUTPUT_FILE, "w") as file:
        file.write(data)
        print("New json file is created")


def main() -> None:
    soup = read_xml_file(INPUT_FILE)
    items = soup.find_all("item", limit=3)
    # TODO: get images, crop and save
    new_xml_data = gen_new_xml(items)
    write_json_file(new_xml_data)


if __name__ == "__main__":
    main()
