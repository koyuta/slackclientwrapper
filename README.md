# Usage

```python
from SlackClientWrapper import Client, Reciever


BOT_NAME, BOT_ICON_URL = "botname", "http://hogebot.png"

r = Reciever()

@r.match('Hello world')
def matcher(post):
    response = "some messages"
    return post['channel'], response

@r.full_recieve
def reciever(post):
    response "some messages"
    return None, response

if __name__ == '__main__':
    m = Client(BOT_NAME, BOT_ICON_URL)
    m.connect()
```
