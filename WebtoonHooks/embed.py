from textwrap import wrap
from DiscordHooks import Hook, Embed, EmbedAuthor, Color, EmbedField

from WebtoonHooks.webtoon import get_daily_releases, genres

img = "https://i.imgur.com/pFDz8Ixl.jpg"


class EmbedFieldInline(EmbedField):
    """Inline version for EmbedField"""
    __items__ = ('name', 'value', 'inline')

    @property
    def inline(self) -> bool:
        return True


class ReleaseHook(object):

    def __init__(self, webhook):
        self.webhook = webhook
        self.cards = get_daily_releases()

    def genre_sort(self):
        """Sort the cards by genre"""
        ret = dict()
        for genre in genres:
            ret[genre] = [card for card in self.cards
                          if card.genre == genre]
        return ret

    @staticmethod
    def _text(cards):
        text = ""
        for card in cards:
            name = "\n".join(wrap(card.subject, 28))
            text += "[{}]({})\n".format(name, card.href)
        return text if text != "" else "None for today!"

    def add_fields(self, embed):
        organized = self.genre_sort()

        # Add labeled genres
        labels = ["Slice of life", "Drama", "Action",
                  "Comedy", "Romance", "Fantasy"]
        emoji = "🌿🎭🎬😂💞✨"
        for genre, emo in zip(labels, emoji):
            field = EmbedFieldInline(name=emo + " " + genre,
                                     value=self._text(organized.pop(genre)))
            embed.fields.append(field)

        # Add "Other" category
        other = list()
        for cards in organized.values():
            other.extend(cards)

        field = EmbedField(name= "⁉ Other", value=self._text(other))
        embed.fields.append(field)

    def send(self):
        """Make embed message with all the release and send them with hooks"""
        embed = Embed(description="Here are the Webtoons updates for today!",
                      color=Color.Lime,
                      author=EmbedAuthor(name="New Updates!", icon_url=img),
                      title="")
        self.add_fields(embed)

        # Send
        hook = Hook(
            hook_url=self.webhook,
            username="Webtoons Update",
            avatar_url=img,
            embeds=[embed]
        )
        hook.execute()
