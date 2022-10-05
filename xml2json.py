from bs4 import BeautifulSoup
import html, json

INPUT_FILE = "politik_input.xml"
OUTPUT_FILE = "my_output_py.xml"

# read xml file
def read_xml_file(filename:str) -> BeautifulSoup:
    with open(filename, "r") as file:
        return BeautifulSoup(file, features="lxml-xml")


# create json
def gen_json(items:list) -> list:
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
    return data


# write json
def write_json(data:list) -> None:
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=2)
        print(f"New json file is created: {OUTPUT_FILE}")


def main() -> None:
    soup = read_xml_file(INPUT_FILE)
    items = soup.find_all("item", limit=3)
    #TODO: get images, crop and save
    new_json = gen_json(items)
    write_json(new_json)


if __name__ == "__main__":
    main()
