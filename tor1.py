import requests
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
def get_tor_session():
    session = requests.session()
        # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5h://127.0.0.1:9150',
                           'https': 'socks5h://127.0.0.1:9150'}
    return session

def torSearcher(url):
    # BEFORE YOU START - RUN tor.exe !!!!

    # Make a request through the Tor connection
    # IP visible through Tor
    
    #url = "http://httpbin.org/ip"
    #url = "http://x.onion/"

    ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
    ,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
    ,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    ,"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
    ua = random.choice(ua_list)
    headers = {'User-Agent': ua}
    print("Getting ...", url)
    result = session.get(url).text
    # Above should print an IP different than your public IP
    # Following prints your normal public IP
    #print(requests.get("http://httpbin.org/ip").text)

    #>>> url = "http://x.onion/"
    #>>> url = url.replace("http://","")
    #>>> url = url.replace(".onion","")
    #>>> url = url.replace("/","")
    # or  u can use the name
    
    import string
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    with open(f"{filename}.txt","w+", encoding="utf-8") as newthing:
        newthing.write(result)

num = int(input())


for i in range(num):
    if num==1:
        url = "http://teclqm5qcfue7tnkpwkj63nodq77kppaqtacvr2gdubxx24kjadt55ad.onion"
        session = get_tor_session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        torSearcher(url)
    else:
        url = "http://hmuidcgzsjlcsxe6rdluskevjtgynhupixpb7g5czmjpuftlhrl42bid.onion"
        session = get_tor_session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        torSearcher(url)


with open('sites5323.txt', 'r') as file:
    List = file.readlines()
    for line in (List[:num]):
        url = "http://" + line
        session = get_tor_session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        torSearcher(url)
    session.close()