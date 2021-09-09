# DiscordEmoji.com API Wrapper for Python | Documentation

### Installation:
To install with PIP, run this in your console:
```
pip install pydemoji
```
### Stats:

To fetch stats from [Emoji.gg](https://emoji.gg):
```py
from pydemoji import stats
...
await stats.fetch(endpoint)
```
Available Endpoints:

| Endpoint | Description                                            |
|----------|--------------------------------------------------------|
| emoji    | Fetch the number of available emoji on Emoji.gg.   |
| users    | Fetch the number of users on Emoji.gg.             |
| faves    | Fetch the total number of faves on Emoji.gg.       |
| pending  | Fetch the number of pending approvals on Emoji.gg. |

### Fetch Emoji:

To fetch emojis from [Emoji.gg](https://emoji.gg):
```py
from pydemoji import emoji
...
await emoji.fetch(option, query, endpoint) # endpoint is optional. if not provided, will return the whole JSON response.
```
Options:

| Option | Description                          |
|--------|--------------------------------------|
| title  | Fetch an emoji by the emoji's title. |
| id     | Fetch an emoji by the emoji's ID.    |
| slug   | Fetch an emoji by the emoji's slug.  |

Available Endpoints:

| Endpoint | Description                                                   |
|----------|---------------------------------------------------------------|
| title    | Fetch the emoji's title.                                      |
| id       | Fetch the emoji's id.                                         |
| slug     | Fetch the emoji's slug.                                       |
| image    | Fetch the emoji's image URL.                                  |
| category | Fetch the emoji's category.                                   |
| license  | Fetch the emoji's license. If none, will return 0.            |
| source   | Fetch the emoji's original source. If none, will return None. |
| faves    | Fetch the emoji's faves.                                      |
| author   | Fetch the emoji's submitter.                                  |

