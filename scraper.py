import urllib.parse 
import cloudscraper, re, base64, requests, random
from bs4 import BeautifulSoup

def decode_base64(text,lossless=False):
    base64_bytes = text.encode('ascii')
    if lossless:
        base64_bytes += b'=='
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

def parse_web(url,headers=None,raw=False):
    try:
        scraper = cloudscraper.create_scraper()
        page = scraper.get(url,headers=headers).content
    except:
        page = requests.get(url,headers=headers).content
    if raw:
        return page
    return BeautifulSoup(page, "html.parser")

def api_get(url,json=None,headers=None,data=None,post=False):
    try:
        scraper = cloudscraper.create_scraper()
        if post:
            page = scraper.post(url,headers=headers,json=json,data=data)
        else:
            page = scraper.get(url,headers=headers,json=json,data=data)
    except:
        if post:
            page = requests.post(url,headers=headers,json=json,data=data)    
        else:
            page = requests.get(url,headers=headers,json=json,data=data)
    return page


def urlEncode(url, data):
    param = urllib.parse.urlencode(data)
    return url+"?"+param

