import requests


QUOTE_URL = "https://api.quotable.io/random"


def handler(event, context):
    quote = get_quote()
    return {
        "message": f"\"{quote['content']} - {quote['author']}\"",
    }


def get_quote():
    res = requests.get(QUOTE_URL)
    return res.json()
