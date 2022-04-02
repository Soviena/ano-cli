import re, scraper, json
from sys import prefix
from html import unescape
base_url = "https://anoboy.online/"

def querySearch(query:str):
    r = scraper.parse_web(base_url+"search/"+query)
    c = r.findAll("article")
    return c

def selectEpisode(animeUrl:str)->str:
    r = scraper.parse_web(animeUrl)
    epList = r.find('div',class_="eplister")
    episodes = epList.findAll('li')
    x = int(input("Pilih episode [1-{}] : ".format(len(episodes))))
    return episodes[x-1].find('a')['href']

def selectMirror(epUrl:str)->str:
    r = scraper.parse_web(epUrl)
    print(r)
    videoServer = r.find('select', class_="mirror").findAll('option')
    for i in range(1,len(videoServer)):
        print("[{}] ".format(i)+videoServer[i].text)
    x = int(input("Pilih source : "))
    return re.findall(r'src="(.*?)"', scraper.decode_base64(videoServer[x]['value']))[0]

def searchAnime():
    query = input("Cari anime : ")
    animes = querySearch(query)
    for i in range(len(animes)):
        print("[{}] ".format(i)+animes[i].find('a')['title'][13:])
    x = int(input("Pilih anime : "))
    Eplink = selectEpisode(animes[x].find('a')['href'])
    return selectMirror(Eplink)


