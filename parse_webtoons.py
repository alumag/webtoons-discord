import time
import requests
from bs4 import BeautifulSoup as bs

link = "https://www.webtoons.com/en/dailySchedule"
genres = [
    "Drama", "Fantasy", "Comedy",
    "Action", "Slice of life", "Romance",
    "Superhero", "Historical", "Thriller", "Sports"
]


class Session:
    """requests session with valid headers"""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                      "/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
                      "Safari/537.36"
    })
    data = {
        "timezoneOffset": -4,
        "locale": "en"
    }

    @staticmethod
    def get(url=link):
        return Session.session.get(url, data=Session.data).content


class Card(object):
    """Release card object"""
    def __init__(self, data):
        """
        :data: soup <li> object
        """
        self.subject = data.find(class_="subj").get_text()
        self.genre = data.find(class_="genre").get_text()
        self.author = data.find(class_="author").get_text()
        self.href = data.find(class_="daily_card_item")['href']

    def __repr__(self):
        return "Card({}, {}, {}, {})".format(
            self.subject, self.genre, self.author,
            "linked" if self.href else "unlinked"
        )


def get_daily_releases():
    day = time.strftime("%A")
    soup = bs(Session.get(), "lxml")

    # Find the daily and split to cards
    daily = soup.find("div", {'class': "daily_section _list_" + day.upper()})
    return daily.find_all("li")


def parse_releases():
    cards = get_daily_releases()

    data = [
        Card(card) for card in cards
    ]

    return data


print(parse_releases())
