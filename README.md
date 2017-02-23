# Usage

```python
from SlackClientWrapper import Client, Reciever

r = Reciever()

@r.match('Hello world')
def matcher(post):
    response = "some messages"
    return post['channel'], response

@r.full_recieve
def reciever(post):
    response "some messages"
    return None, response
```
