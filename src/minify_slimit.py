from src.utils import garble_it
from slimit import minify


def garble_js(js):
    """Runs the garble logic as a function using jsmin for minification rather than slimit
    Python 3 compatible.

    Takes a given JS string, garbles is and returns the output

    :param string js: A string contain the Javascript you wish to garble
    :return string: The garbled Javascript
    """
    return garble_it(js, minify_with_slimit, mangle=False, mangle_toplevel=False )


def minify_with_slimit(js, mangle=False, mangle_toplevel=False):
    """slimit minification

    :param string js:
    :param string quote_chars:
    :return string:
    """
    return minify(js, mangle=mangle, mangle_toplevel=mangle_toplevel)
