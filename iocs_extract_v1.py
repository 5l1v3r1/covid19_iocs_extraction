#Author: Santhosh Baswa
#Script in Under Construction

import requests

url = 'https://blocklist.cyberthreatcoalition.org/'
index = ['vetted','unvetted']
ioc_types = ['domain.txt','ip.txt','url.txt']

def url_list(url,index,ioc_types):
    urls_list = []
    for l in index:
        for x in ioc_types:
           url_a = (url+l+'/'+x)
           urls_list.append(url_a)
    return urls_list
print(url_list(url,index,ioc_types))
list_of_urls = url_list(url,index,ioc_types)

def url_request(url):
    r = requests.get(url)
    output_text = r.text
    parsed_text = output_text.splitlines()
    return parsed_text

for url_x in list_of_urls:
    print("URL:",url_x)
    print("-------- XXXXX --------")
    print(url_request(url_x))
    print("-------- XXXXX --------")
