import bs4
import re
import urllib.request


class InfoPageScrapper:

    def __init__(self, page_url):
        self.page_url = page_url

    def get_paragraphs_text(self):
        whole_page_data = urllib.request.urlopen(self.page_url).read()
        data_paragraphs = bs4.BeautifulSoup(whole_page_data, "html.parser").find_all('p')
        data_text = ""

        for paragraph in data_paragraphs:
            data_text += paragraph.text.lower()

        data_text = re.sub(r"\s+", ' ', re.sub(r"\[[0-9]*]", ' ', data_text))

        return data_text
