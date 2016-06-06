from src.utils import garble_it
from jsmin import jsmin


def garble_js(js):
    """Runs the garble logic as a function using jsmin for minification rather than slimit
    Python 3 compatible.

    Takes a given JS string, garbles is and returns the output

    :param string js: A string contain the Javascript you wish to garble
    :return string: The garbled Javascript
    """
    return garble_it(js, minify_with_jsmin, quote_chars="'\"`" )


def minify_with_jsmin(js, quote_chars="'\"`"):
    """jsmin minification

    :param string js:
    :param string quote_chars:
    :return stringf:
    """
    return jsmin(js, quote_chars=quote_chars)
