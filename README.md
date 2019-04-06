# webtoon Hooks
webtoon discord webhooks

![Webtoon](https://i.imgur.com/PdTgcjE.png)

## Installation
```
pip install WebtoonHooks
```

## Usage
Send complete designed webhook with all the daily releases

```python
>>> from WebtoonHooks import ReleaseHook
>>> ReleaseHook("SECRET-WEBHOOK-URL").send()
```

Get list of the dailies releases
```python
>>> WebtoonHooks.get_daily_releases()   # list(<WebtoonHooks.Card>)
[
    Card(Boyfriend of the Dead, Comedy, Ushio, linked),
    Card(My Giant Nerd Boyfriend, Slice of life, fishball, linked),
    Card(Muted, Drama, Miranda Mundt, linked),
    ...
]
```

## Card object
Represent one `daily_card` from [dailySchedule](https://www.webtoons.com/en/dailySchedule)
* Subject
* Author name
* Genre
* Link to episodes list
```
>>> card.href
'https://www.webtoons.com/en/comedy/boyfriend-of-the-dead/list?title_no=1102'
>>> card.subject
'Boyfriend of the dead'
```
