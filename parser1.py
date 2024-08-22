from bs4 import BeautifulSoup

def get_posts(page):
    soup = BeautifulSoup(page.text, "html.parser")
    page_tag_content = soup.findAll("div", class_="cit")
    obj = []
    for i in page_tag_content:

        cit = i.find("p")
        item = {
            f"cit": cit.text.strip()
        }
        obj.append(item)
    return obj




