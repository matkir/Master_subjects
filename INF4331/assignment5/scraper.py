from re import *
import urllib.request
import sys



def find_emails(text):
    return findall(r"[a-zA-Z0-9\&\~._%\*\?\{\}+-]+@[a-zA-Z\&\~\_.-]+\.[a-zA-Z]{2,4}", text)


def url2html(url):
    with urllib.request.urlopen(url) as f:
        return f.read().decode('utf-8') #only the first 1000 symbols, if the text is to long


def find_hyperlinks(text):
    #here ive done something 'clever':
    #it turns out that you can make the regex pretty advanced, and the 'else' part is that.
    #the if part is much simpeler, and is therfore much faster.
    #when running the get_all_emails the faster regex is much smarter to run.

    if __name__=="__main__":
        #higher failure rate,but is faster!
        #no file exteniton. because of speed.
        protocol = "https?\:\/\/"
        domain = "[\w\.\,\~]+"
        sub = "[\w\.\,\~\/]+"
        return findall(r"href=\"({0}{1}{2})\">".format(protocol, domain, sub), text)
    else:
        protocol = "(?:http(?:s)?:\/\/)?"
        domain = "(?:(?:www\.)?[a-zA-Z0-9-\.+-]+\.\w{2,3}(?:\/| |$|\n))"
        sub = "(?:[a-zA-Z0-9+~-]+\/?)*"
        filetype = "(?:[a-z0-9A-Z]+\.[a-zA-Z]+)?"
        return findall(r"\<a href=\"({0}{1}{2}{3})\"".format(protocol, domain, sub, filetype), text)


def find_relative_hyperlinks(text, absurl):
    protocol = "(?:http(?:s)?:\/\/)?"
    domain = "(?:(?:www\.)?[a-zA-Z0-9-\.+-]+\.\w{2,3}(?:\/| |$|\n))"
    url = findall(r"{0}{1}".format(protocol, domain), absurl)[0]
    a = findall(r'<a href="\/?((?:[a-zA-Z0-9+~-]+\/?)+(?:\.[a-zA-Z0-9]*)?)', text)
    return [url + item for item in a if "http" not in item]


def get_all_emails(url, emails=set(), visited_adresses=[], maxsites=100, maxlevel=3, thislevel=0):
    """
    Finds all the emails on the first (length) websites on the url page

    input:
        url: input url, the start point
        in_file: the file the email adresses are written to.
        visited_adresses: empty list that is filled up with all the adresses previously visited. (think of this as a blacklist)
        length: number of sited visited
        verbatim: if it prints the results or not
    """
    if url in visited_adresses or len(visited_adresses) > maxsites or thislevel > maxlevel:
        return None

    if url not in visited_adresses:
        visited_adresses.append(url)

    try:
        html = url2html(url)
        url_emails = find_emails(html)

        print("visiting:", url, "\t\t- emails:", len(url_emails))

        for adress in url_emails:
            emails.add(adress)

        for urls in find_hyperlinks(html) + find_relative_hyperlinks(html, url):
            get_all_emails(urls, emails, visited_adresses, maxsites, maxlevel, thislevel + 1)

    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    except Exception as e:
        pass

    return visited_adresses, emails


if __name__=='__main__':
    urls, emails = get_all_emails("https://lucidtech.io/", maxsites=100, maxlevel=3)

    with open("test", mode='w') as f:
        for email in emails:
            f.write(email + "\n")

    print("Visited:", len(urls), "\nEmails:", len(emails))