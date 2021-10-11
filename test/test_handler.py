from app import handler


def test_get_quote():
    res = handler.get_quote()

    assert "author" in res
    assert "content" in res


def test_handler():
    res = handler.handler({}, {})

    assert "message" in res
