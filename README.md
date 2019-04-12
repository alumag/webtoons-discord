# Webtoon Hooks
discord webhooks package for webtoons.com information

## Installation
```bash
pip install WebtoonHook
```

## Usage
### Send complete designed webhook with all the daily releases
![Daily update](https://i.imgur.com/8oTTnhj.png)
```python
>>> from WebtoonHooks import ReleaseHook
>>> release = ReleaseHook()
>>> release.send("SECRET-WEBHOOK-URL")
```

### Send webhook with the weekly hot webtoons
![Weekly hot](https://i.imgur.com/akcHpKp.png)
```python
>>> from WebtoonHooks import WeeklyHotHook
>>> hot = WeeklyHotHook()
>>> hot.send("SECRET-WEBHOOK-URL")
```

### Get list of the dailies releases
```python
>>> WebtoonHooks.get_daily_releases()   # list(<WebtoonHooks.Card>)
[
    Card(Boyfriend of the Dead, Comedy, Ushio, linked),
    Card(My Giant Nerd Boyfriend, Slice of life, fishball, linked),
    Card(Muted, Drama, Miranda Mundt, linked),
    ...
]
```

### Get list of the weekly hot webtoons
```python
>>> WebtoonHooks.get_weekly_hot()   # list(<WebtoonHooks.Card>)
```

## Card object
Represent one `daily_card` from [dailySchedule](https://www.webtoons.com/en/dailySchedule) or [challenge](https://webtoons.com/en/challenge)
* Subject
* Author name
* Genre
* Link to episodes list
* Number of likes
* New / Paused / UP tags
```python
>>> card.href
'https://www.webtoons.com/en/comedy/boyfriend-of-the-dead/list?title_no=1102'
>>> card.subject
'Boyfriend of the dead'
>>> card.is_new
True
```

----
Made with 💗 for [LINE WEBTOON](https://discord.gg/RB53Z3) by Aluma Gelbard.
