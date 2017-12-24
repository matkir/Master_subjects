from re import *



def parse_nwodkram(text):
    """
    Taking a nwodkram doc and makes in to an HTML.
    INPUT: text (string)
    Output text (string)
    """
    t = text

    # bold
    t = sub(r'(?<!\\)%(.*?)(?<!\\)%', r"<b>\1</b>", t)
    t = sub(r'\\%', r"%", t)

    # italic
    t = sub(r'(?<!\\)\*(.*?)(?<!\\)\*', r"<i>\1</i>" , t)
    t = sub(r'\\\*', r"*", t)

    # wiki
    t = sub(r"\[wp:(\w+)\]", r"<a href={0}www.wikipedia.org/wiki/\1{0}>Search Wikipedia for \1</a>".format("\""), t)

    # hyperlink
    t = sub(r'\[(.*?)\]\((?:http)?(s?)(?:\://)?(.*?)\)', r"<a href='http\2://\3'>\1</a>", t)

    # image
    t = sub(r"\<((?:http|www).*)\>\(\w=(\d+),h=(\d+)\)",r"<img src={0}\1{0} style={0}width:\2px;height:\3px{0};>".format("\""),t)

    # blockqoute
    t = sub(r">>(.*)",r"<blockquote>\1</blockquote>", t)

    return t



if __name__=='__main__':

    sample_input = r"""
    This is some Nwodkram text. Note that *this* is in italic, and %this% is in bold.
    If you want to write an \* or an equal sign and not have the parser eat them,
    that's easy -  note that \* this \* is not in italic even though it's between two \*s,
    and \% this \% is not in bold.

    [here](www.google.com) is a hyperlink.
    [here](http://www.google.com) is another.
    [and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
    Follow it at your own peril.

    Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
    But don't worry too much if some weird combination is ambiguous or results in
    weird stuff.
    """

    expected_output = r"""
    This is some Nwodkram text. Note that <i>this</i> is in italic, and <b>this</b> is in bold.
    If you want to write an * or an equal sign and not have the parser eat them,
    that's easy -  note that * this * is not in italic even though it's between two *s,
    and % this % is not in bold.

    <a href='http://www.google.com'>here</a> is a hyperlink.
    <a href='http://www.google.com'>here</a> is another.
    <a href='https://www.weird?$|site.weird/path/'>and here</a> is a third with some weird characters.
    Follow it at your own peril.

    Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
    But don't worry too much if some weird combination is ambiguous or results in
    weird stuff.
    """

    print(parse_nwodkram(sample_input)==expected_output)

