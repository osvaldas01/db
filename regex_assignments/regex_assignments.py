import re
from constants_file.retext import TEXT
import requests


class RegProgram:
    def __init__(self, text):
        self.text = text

    def change_date(self):
        pattern = r'(\d{2})\.(\d{2})\.(\d{4})'
        result = re.sub(pattern, r'\3 \2 \1', self.text)
        return result

    def print_date(self):
        pattern = re.compile(r'[A-Z]\w+ \d{1,2},\s\d{4}')
        result = pattern.findall(TEXT)
        return result

    def event_date(self):
        date = re.findall(r'([A-Za-z]+ \d{1,2}, \d{4})', TEXT)
        name = re.findall(r'(.+?(?=:))', TEXT)
        for nr in range(len(date)):
            print(f'{nr+1}.\nEvent: {name[nr]}\nDate: {date[nr]}\n')

    def censorship(self, *args):
        text = "baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys"
        for word in args:
            censored_word = word[0] + '*' * (len(word) - 2) + word[-1]
            text = re.sub(r'\b' + re.escape(word) + r'\b', censored_word, text)
        return text


class RequestProgram:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/robotautas/kursas/master/RegEx/most_visited.html"

    def get_html(self):
        response = requests.get(self.url)
        return response.text

    def get_links(self):
        domain = re.compile(r'\w+\.\w+|\.\w+')
        links = domain.findall(self.get_html())
        return links
