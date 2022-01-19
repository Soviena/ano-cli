import re, scraper, json
from sys import prefix
from html import unescape
base_url = "https://anoboy.live/"

def querySearch(query:str,page:int=1)->dict:
    data = {
        "page": page,
        "limit": 21,
        "action": "load_search_movie",
        "keyword": query,
    }
    enc_url = scraper.urlEncode(base_url+'my-ajax',data)
    return eval(scraper.api_get(enc_url).content)

def selectEpisode(anime_url:str)->str:
    s = scraper.parse_web(anime_url)
    episodes = s.find('ul', id='episodebox').findAll('a')
    x = int(input("Select episode [1-{episode}] : ".format(episode=len(episodes))))    
    return episodes[len(episodes)-x]['href']

def iframe(url:str)->str:
    s = scraper.parse_web(url)
    gomu = str(s.find('iframe')['src'])
    id = re.findall(r'#(.*)',gomu)[0]
    print("https://app.opencdn.co/munime?id="+id)
    s = eval(scraper.api_get("https://app.opencdn.co/munime?id="+id).content)
    return str(s['fembed']['link']).replace('\\','')

def mp4upload(url:str)->str:
    print(url)
    s = scraper.parse_web(url)
    garb = s.find('script', text= re.compile("'(\|\|.*?)'"))
    id = re.findall(r'\|([^|]{56})\|',str(garb))[0]
    prefix = re.findall(r'\|embed\|(.*?)\|',str(garb))[0]
    return "https://"+prefix+".mp4upload.com:282/d/"+id+"/video.mp4"
    # --http-header-fields="Referer: www.mp4upload.com"

def animepl(url:str)->str:
    print(url)
    v_id = re.findall(r'v\/(.*)',url)[0]
    head = {
        "referer": "https://animepl.xyz",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        'r':'',
        'd':'animepl.xyz'
    }

    return json.loads(scraper.api_get('https://animepl.xyz/api/source/'+v_id,headers=head,data=data,post=True).content)['data']

def searchAnime()->str:
    query = input("Cari anime : ")
    animes = querySearch(query)
    for i in range(len(animes['data'])):
        print('[{0}] {1}'.format(i,unescape(animes['data'][i]['post_title'])))
    x = int(input('select anime : '))
    anime = animes['data'][x]
    print(base_url+anime['post_name'])
    url = selectEpisode(base_url+anime['post_name'])
    embed_link = iframe(url)
    if "animepl" in embed_link:
        vlink = animepl(embed_link)
    elif "mp4upload" in embed_link:
        vlink = mp4upload(embed_link)
    else:
        print("Untested", embed_link)
        raise Exception("UNTESTED")
    return vlink


