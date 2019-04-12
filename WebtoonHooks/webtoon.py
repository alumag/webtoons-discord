import time
import requests
from bs4 import BeautifulSoup as bs

base_link = "https://www.webtoons.com/en/"
genres = [
    "Drama", "Fantasy", "Comedy",
    "Action", "Slice of life", "Romance",
    "Superhero", "Historical", "Thriller", "Sports",
    "SCI-FI", "Horror", "Informative"
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
    def get(url=""):
        return Session.session.get(url, data=Session.data).content

    @staticmethod
    def get_page(page=""):
        return Session.get(base_link + page)


class Card(object):
    """Release card object"""
    def __init__(self, data):
        """
        :data: soup <li> object
        """
        self.subject = data.find(class_="subj").get_text()
        self.genre = data.find(class_="genre").get_text()
        try:
            self.author = data.find(class_="author").get_text()
        except AttributeError:
            self.author = None
        try:
            self.grade = data.find(class_="grade_num").get_text()
        except AttributeError:
            self.grade = None
        self.href = data.find("a")['href']
        self._data = data

    @property
    def is_up(self):
        if self._data.find(class_="txt_ico_up2"):
            return True
        return False

    @property
    def is_paused(self):
        if self._data.find(class_="txt_ico_hiatus2"):
            return True
        return False

    @property
    def is_new(self):
        if self._data.find(class_="txt_ico_new2"):
            return True
        return False

    def __repr__(self):
        return "Card({}, {}, {})".format(
            self.subject, self.genre, self.author
        )


def get_daily_releases():
    day = time.strftime("%A")
    soup = bs(Session.get_page("dailySchedule"), "lxml")

    # Find the daily and split to cards
    daily = soup.find("div", {'class': "daily_section _list_" + day.upper()})
    cards = daily.find_all("li")

    data = [
        Card(card) for card in cards
    ]

    return data


def get_weekly_hot():
    soup = bs(Session.get_page("challenge"), "lxml")
    # Find the daily and split to cards
    daily = soup.find("div", {'class': "weekly_hot_area"})
    cards = daily.find_all("li")

    data = [
        Card(card) for card in cards
    ]

    return data
