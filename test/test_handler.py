import app


def test_get_quote():
    res = app.get_quote()

    assert "author" in res
    assert "content" in res

    assert "thisWillFailPytestAndMakeFlake8FailAswell..............................." in res


def test_handler():
    res = app.handler({}, {})

    assert "message" in res
