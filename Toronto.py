# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:08:41 2022

@author: mehdi
"""

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
    url=f'https://www.rew.ca/rentals/areas/toronto-on/page/{page}'
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup


def transform(soup):
    divs=soup.find_all('div',class_='displaypanel-content')
    for item in divs:
        price=item.find('div',class_='displaypanel-title hidden-xs').text.strip().replace('/n','').lstrip(',').split('/')[0].replace('$','')
        address=item.find('li').text
        moreinfo=item.find('div',class_='displaypanel-section clearfix').text.strip()
        bedroom=item.find('div',class_='displaypanel-section clearfix').text.strip().replace('V Tour','').split('bd')[0].strip()
        bathroom=item.find('div',class_='displaypanel-section clearfix').text.strip().replace('V Tour','').split('\n')[1].split('ba')[0].strip()
        try:
            size_sqf=item.find('div',class_='displaypanel-section clearfix').text.strip().replace('V Tour','').replace('\n','').split('ba')[1].split(' ')[0]
        except:
            size_sqf=''
        types=item.find('div',class_='clearfix hidden-xs').text.strip().replace('/n','').replace('V Tour','')
        rental={'price':price,
               'Address':address,
               'moreinfo':moreinfo,
               'bedroom':bedroom,
               'bathroom':bathroom,
               'size_sqf':size_sqf,
               'types':types,
               'city':'Toronto'
                
            }
        rentallist.append(rental)
         
    return

rentallist=[]

print(rentallist)
for i in range(1,26):
    print(f'getting page,{i}')
    c=extract(i)
    transform(c)
print(len(rentallist))
df=pd.DataFrame(rentallist)
df.to_csv('rentallist_Toronto.csv')
print(df)