import feedparser
import requests

rss_url = 'http://127.0.0.1:5000/poc30'
r = requests.get(rss_url, verify=False)
p = feedparser.parse(r.text)
if 'bozo_exception' in p:
    print 'occur bozo_exception'
print p
