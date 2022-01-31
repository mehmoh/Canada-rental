# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:11:17 2022

@author: mehdi
"""

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
#print('what is the first page')
first_url=input('first url such as https://www.rew.ca/rentals/areas/toronto-on/page')
number_pages=input('number of pages')
number_pages=int(number_pages)
number_pages=number_pages+1
city_name=input('city name?')
def extract(page):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url=f'{first_url}/{page}'
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
               'city':city_name
                
            }
        rentallist.append(rental)
         
    return
rentallist=[]

for i in range(1,number_pages):
    try:
        print(f'getting page,{i}')
        c=extract(i)
        transform(c)
    except:
        print('there is an error in that page')
        pass
print(len(rentallist))
df=pd.DataFrame(rentallist)
print(df)
a=input ('Press 1 if you wanna extract it to csv otherwise press any other number')
a=int(a)
if a==1:
    df.to_csv(city_name+".csv")
    print('it is extracted')
if a!=1:
    print ('What is the')
