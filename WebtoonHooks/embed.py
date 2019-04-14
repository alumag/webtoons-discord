from textwrap import wrap
import datetime
from DiscordHooks import (
    Hook, Embed, EmbedAuthor,
    Color, EmbedField, EmbedFooter
)

from WebtoonHooks.webtoon import get_daily_releases, get_weekly_hot
from WebtoonHooks.webtoon import genres

# Globals
webtoon_logo = "https://i.imgur.com/pFDz8Ixl.jpg"
labels = ["Slice of life", "Drama", "Action",
          "Comedy", "Romance", "Fantasy"]
emoji = "🌿🎭🎬😂💞✨"


def get_emoticon(genre):
    """Find the matching emoticon for genre"""
    if genre not in labels:
        return "⁉"
    return emoji[labels.index(genre)]


class EmbedFieldInline(EmbedField):
    """Inline version for EmbedField"""
    __items__ = ('name', 'value', 'inline')

    @property
    def inline(self) -> bool:
        return True


class WebtoonHook(object):
    """General webtoon hook class"""

    # Main embed params
    name = "Webtoon Update"
    description = "Webtoon description"
    color = Color.Lime
    author = None
    # get_cards function
    func = list

    def __init__(self):
        self.cards = self.get_cards()
        self.embed = Embed(
            author=self.author,
            title="",
            description=self.description,
            color=self.color,
        )
        self.embeds = [self.embed]
        self.create_message()

    @classmethod
    def get_cards(cls):
        """Get specific cards"""
        # cls.func is overrided
        return cls.func()

    def create_message(self):
        """Add embeds / fields and etc"""
        raise NotImplementedError

    def send(self, webhook):
        """Send hook"""
        Hook(
            hook_url=webhook,
            username=self.name,
            avatar_url=webtoon_logo,
            embeds=self.embeds
        ).execute()


class ReleaseHook(WebtoonHook):

    func = get_daily_releases
    author = EmbedAuthor(name="New Updates!", icon_url=webtoon_logo)
    description = "Here are the Webtoons updates for today!"

    def sort_by_genre(self):
        """Sort the cards by genre"""
        return {
            genre: [
                card for card in self.cards
                if card.genre == genre and not card.is_paused
            ]
            for genre in genres
        }

    @staticmethod
    def style_value(cards):
        text = ""
        for card in cards:
            name = "\n".join(wrap(card.subject, 26))
            text += "[{}]({})\n".format(name, card.href)
        return text if text != "" else "None for today!"

    def create_message(self):
        """Create embed message with all the releases"""
        # Sort the cards
        organized = self.sort_by_genre()

        # Add fields for every labled genre
        for genre in labels:
            name = " ".join([get_emoticon(genre), genre])
            value = self.style_value(organized.pop(genre))
            field = EmbedFieldInline(name=name, value=value)
            self.embed.fields.append(field)

        # Add one field for all the "Other"
        other = list()
        for cards in organized.values():
            other.extend(cards)

        name = " ".join([get_emoticon("Other"), "Other"])
        field = EmbedField(name=name, value=self.style_value(other))
        self.embed.fields.append(field)


class WeeklyHotHook(WebtoonHook):

    func = get_weekly_hot
    description = "Here are the Discover Webtoons updates for the week!"
    name = "Weekly HOT"

    def create_message(self):
        """Create embed message with the current weekly hot"""
        for card in self.cards:
            field = EmbedFieldInline(
                name=card.subject,
                value="[🔗]({}) | {} {}\n💗 {}\r"
                      .format(card.href, get_emoticon(card.genre),
                              card.genre, card.grade)
            )
            self.embed.fields.append(field)
