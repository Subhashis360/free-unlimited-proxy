import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from random import shuffle, choice

def Fetch_Proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies_list = []
    for row in soup.select("table tbody tr")[:100]:
        if 'yes' in row.select_one("td:nth-of-type(7)").text:
            proxy = ":".join([row.select_one("td:nth-of-type(1)").text, row.select_one("td:nth-of-type(2)").text])
            proxies_list.append(proxy)
    shuffle(proxies_list)
    return proxies_list

def Get_Valid_Proxy(proxies_list):
    header = Headers(headers=False).generate()
    agent = header['User-Agent']

    headers = {
        'User-Agent': f'{agent}',
    }

    url = 'http://icanhazip.com'
    while True:
        proxy = choice(proxies_list)
        proxies = {
            'http': f'http://{proxy}',
            'https': f'https://{proxy}',
        }
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=1)
            if response.status_code == 200:
                return proxy
        except:
            continue

def Generate_Proxy():
    proxies_list = Fetch_Proxies()
    proxy = Get_Valid_Proxy(proxies_list)
    return proxy


#usage 

#PROXY_URL = Generate_Proxy()
#proxies = {
#    "http": PROXY_URL,
#    "https": PROXY_URL
#}

#response = requests.post(url, data=json.dumps(data), headers=headers, proxies=proxies)












