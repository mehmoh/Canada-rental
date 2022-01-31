# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:30:31 2022

@author: mehdi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url=f'https://www.rew.ca/rentals/areas/vancouver-bc/page/{page}'
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup


def transform(soup):
    divs=soup.find_all('div',class_='displaypanel-content')
    for item in divs:
        price=item.find('div',class_='displaypanel-title hidden-xs').text.strip().replace('/n','').lstrip(',').split('/')[0]
        address=item.find('li').text
        moreinfo=item.find('div',class_='displaypanel-section clearfix').text.strip()
        types=item.find('div',class_='clearfix hidden-xs').text.strip().replace('/n','')
        rental={'price':price,
                'Address':address,
                'moreinfo':moreinfo,
                'types':types
            }
        rentallist.append(rental)
         
    return
rentallist=[]
for i in range(1,14):
    print(f'getting page,{i}')
    c=extract(i)
    transform(c)
print(len(rentallist))
df=pd.DataFrame(rentallist)
df.to_csv('rentallist')