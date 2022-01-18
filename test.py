import anoboy
import scraper


print(anoboy.searchAnime())


# import scraper, re,json
# from html import unescape

# query = "abyss"

# base_url = "https://anoboy.live/"

# data = {
#     "page": 1,
#     "limit": 10,
#     "action": "load_search_movie",
#     "keyword": query,
# }

# enc_url = scraper.urlEncode(base_url+'my-ajax',data)
# animes = eval(scraper.api_get(enc_url).content)
# for i in range(len(animes['data'])):
#     print('[{0}] {1}'.format(i,unescape(animes['data'][i]['post_title'])))
# x = int(input('select anime : '))
# anime = animes['data'][x]

# s = scraper.parse_web(base_url+anime['post_name'])
# episodes = s.find('ul', id='episodebox').findAll('a')
# x = int(input("Select episode [1-{episode}] : ".format(episode=len(episodes))))
# s = scraper.parse_web(episodes[len(episodes)-x]['href'])
# gomu = str(s.find('iframe')['src'])
# id = re.findall(r'#(.*)',gomu)[0]
# print("https://app.opencdn.co/munime?id="+id)
# s = eval(scraper.api_get("https://app.opencdn.co/munime?id="+id).content)
# embed = str(s['fembed']['link']).replace('\\','')
# print(embed)

# if "animepl" in embed:
#     v_id = re.findall(r'v\/(.*)',embed)[0]
#     head = {
#         "referer": "https://animepl.xyz",
#         "x-requested-with": "XMLHttpRequest"
#     }
#     data = {
#         'r':'',
#         'd':'animepl.xyz'
#     }

#     r = json.loads(scraper.api_get('https://animepl.xyz/api/source/'+v_id,headers=head,data=data,post=True).content)['data']
#     print(r)
#     for i in r:
#         print(i['file'])
        
# elif "mp4upload" in embed:
#     s = scraper.parse_web(embed)
#     garb = s.find('script', text= re.compile("'(\|\|.*?)'"))
#     id = re.findall(r'\|([^|]{56})\|',str(garb))[0]
#     link = "https://www4.mp4upload.com:282/d/"+id+"/video.mp4"
#     print(link)
